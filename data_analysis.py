import xlrd
import xlwt

inat_fieldname_date = "observed_on"
sds_fieldname_year = "encounter.year"
sds_fieldname_month = "encounter.month"
sds_fieldname_day = "encounter.day"
new_excel_filename = "relevant_iNaturalist_entries.xls"


def split_comma_separated_line(line):
    lst = []
    cur = ''
    currently_inside_quotes = False
    for c in line:
        if c == '"':
            currently_inside_quotes = not currently_inside_quotes
        elif c == ',' and not currently_inside_quotes:
            lst.append(cur)
            cur = ''
        else:
            cur += c
    lst.append(cur)
    return lst


def format_date(year, month, day):
    if len(year) == 2:
        year = '20' + year
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    return year + '-' + month + '-' + day


def analyse_data_files(sds_filename, inat_filenames):
    # Ensure that the arguments passed to 'main' are provided in the correct format
    
    if not isinstance(sds_filename, str):
        return [False, "The Seadragon Search filename passed to analyse_data_files was not of type 'string'"]
    
    if not isinstance(inat_filenames, list):
        return [False, "The list of iNaturalist filenames passed to analyse_data_files was not of type 'list'"]

    if len(inat_filenames) == 0:
        return [False, "The list of iNaturalist filenames passed to analyse_data_files was empty"]

    for inat in inat_filenames:
        if not isinstance(inat, str):
            if len(inat_filenames == 1):
                return [False, "The iNaturalist filename in the list passed to analyse_data_files was not of type 'string'"]
            else:
                return [False, "The iNaturalist filenames in the list passed to analyse_data_files were not all of type 'string'"]

    
    
    # Open the iNaturalist csv file
    inat_files = []
    for inat in inat_filenames:
        try:
            f = open(inat, "r")
        except:
            return [False, "The iNaturalist file '" + inat + "' cannot be found or cannot be opened"]
        inat_files.append(f)
    
    # Read in the data from the iNaturalist csv files
    inat_data = []
    each_file_inat_field_date = []
    for i in range(len(inat_files)):
        this_file = inat_files[i]

        this_file_inat_data = [] # index 0 is the headings
        for line in this_file:
            line = split_comma_separated_line(line.strip().lower())
            this_file_inat_data.append(line)
        this_file.close()

        # Find the position of the relevant fieldname in this iNat file
        try:
            this_file_inat_field_date = this_file_inat_data[0].index(inat_fieldname_date)
        except:
            return [False, "Could not find column heading '" + inat_fieldname_date + "' in iNaturalist file '" + inat_filenames[i] + "'"]
        
        inat_data.append(this_file_inat_data)
        each_file_inat_field_date.append(this_file_inat_field_date)
    
    # Open the Seadragon Search Excel file
    try:
        sds_wb = xlrd.open_workbook(sds_filename)
    except:
        return [False, "The Seadragon Search file cannot be found or cannot be opened as an Excel file"]
    try:
        sds_ws = sds_wb.sheet_by_index(0)
    except:
        return [False, "The Seadragon Search Excel file does not contain any worksheets"]
        
    
    # Find the minimum row and minimum column in the Seadragon Search Excel file
    sds_min_row = -1
    done = False
    for r in range(0, sds_ws.nrows):
        for c in range(0, sds_ws.ncols):
            if sds_ws.cell_value(rowx=r,colx=c) is not None:
                sds_min_row = r
                done = True
                break
        if done:
            break

    sds_min_column = -1
    done = False
    for c in range(0, sds_ws.ncols):
        for r in range(0, sds_ws.nrows):
            if sds_ws.cell_value(rowx=r,colx=c) is not None:
                sds_min_column = c
                done = True
                break
        if done:
            break
    
    if sds_min_row == -1:
        assert(sds_min_column == -1)
        return [False, "The (first worksheet in the) Seadragon Search Excel file is empty"]

    # Find the maximum row and maximum column in the Seadragon Search Excel file (worksheet.nrows-1 and worksheet.ncols-1 may be too high)
    sds_max_row = 0
    for r in range(sds_min_row, sds_ws.nrows):
        empty_row = True
        for c in range(sds_min_column, sds_ws.ncols):
            if sds_ws.cell_value(rowx=r,colx=c) is not None:
                empty_row = False
                break
        if empty_row:
            break
        sds_max_row = r

    sds_max_column = 0
    for c in range(sds_min_column, sds_ws.ncols):
        empty_column = True
        for r in range(sds_min_row, sds_ws.nrows):
            if sds_ws.cell_value(rowx=r,colx=c) is not None:
                empty_column = False
                break
        if empty_column:
            break
        sds_max_column = c


    # Read in the data from the Seadragon Search Excel file
    sds_data = [] # index 0 is the headings
    for r in range(sds_min_row, sds_max_row + 1):
        line = []
        for c in range(sds_min_column, sds_max_column + 1):
            line.append(sds_ws.cell_value(rowx=r,colx=c).lower())
        sds_data.append(line)
    assert(sds_data)



    # Find the position of the relevant fieldnames in the Seadragon Search Excel file
    try:
        sds_field_year = sds_data[0].index(sds_fieldname_year)
    except:
        return [False, "Could not find column heading '" + sds_fieldname_year + "' in Seadragon Search file"]
    try:
        sds_field_month = sds_data[0].index(sds_fieldname_month)
    except:
        return [False, "Could not find column heading '" + sds_fieldname_month + "' in Seadragon Search file"]
    try:
        sds_field_day = sds_data[0].index(sds_fieldname_day)
    except:
        return [False, "Could not find column heading '" + sds_fieldname_day + "' in Seadragon Search file"]
    
    # Find the date of each iNaturalist entry
    each_file_inat_entries_on_this_day = []
    each_file_inat_rows_missing_valid_date = []
    for i in range(len(inat_files)):
        this_file_inat_data = inat_data[i]
        this_file_inat_field_date = each_file_inat_field_date[i]
        this_file_inat_entries_on_this_day = {}
        this_file_inat_rows_missing_valid_date = []
        for j in range(1, len(this_file_inat_data)):
            row = this_file_inat_data[j]
            date = row[this_file_inat_field_date]

            date_delimiter = "not_set_yet"
            for c in date:
                if c not in "0123456789":
                    date_delimiter = c
                    break
            if date_delimiter == "not_set_yet":
                this_file_inat_rows_missing_valid_date.append(j)
                continue
            if date.count(date_delimiter) != 2:
                this_file_inat_rows_missing_valid_date.append(j)
                continue
            day, month, year = date.split(date_delimiter)

            try:
                int(year)
                int(month)
                int(day)
            except:
                this_file_inat_rows_missing_valid_date.append(j)
                continue

            my_date_string = format_date(year, month, day)

            if my_date_string not in this_file_inat_entries_on_this_day:
                this_file_inat_entries_on_this_day[my_date_string] = []
            this_file_inat_entries_on_this_day[my_date_string].append(j)
        each_file_inat_entries_on_this_day.append(this_file_inat_entries_on_this_day)
        each_file_inat_rows_missing_valid_date.append(this_file_inat_rows_missing_valid_date)

        
    
    # Find the date of each Seadragon Search entry
    num_sds_entries_on_this_day = {}
    sds_rows_missing_date = []
    for i in range(1, len(sds_data)):
        row = sds_data[i]
        year = row[sds_field_year]
        month = row[sds_field_month]
        day = row[sds_field_day]
        try:
            int(year)
            int(month)
            int(day)
        except:
            sds_rows_missing_date.append(i)
            continue

        my_date_string = format_date(year, month, day)

        if my_date_string not in num_sds_entries_on_this_day:
            num_sds_entries_on_this_day[my_date_string] = 0
        num_sds_entries_on_this_day[my_date_string] += 1

    # Find the number of iNaturalist entries on each date
    num_inat_entries_on_this_day = {}
    for f in each_file_inat_entries_on_this_day:
        for date, entries in f.items():
            if date not in num_inat_entries_on_this_day:
                num_inat_entries_on_this_day[date] = 0
            num_inat_entries_on_this_day[date] += len(entries)

    # See which dates have more iNaturalist entries than Seadragon Search entries (and by how many entries)
    dates_flagged = {}
    for date, num_inat_entries in num_inat_entries_on_this_day.items():
        num_sds_entries = num_sds_entries_on_this_day.get(date, 0)
        diff = num_inat_entries - num_sds_entries
        if diff > 0:
            dates_flagged[date] = diff

    if dates_flagged:
        preview = "The Seadragon Search database appears to be missing:\n"
        for date, diff in dates_flagged.items():
            if diff == 1:
                preview += str(diff) + " iNaturalist entry from " + date + "\n"
            else:
                preview += str(diff) + " iNaturalist entries from " + date + "\n"
    else:
        preview = "The Seadragon Search database appears to be up to date"


    # Make a new Excel file for the results
    new_wb = xlwt.Workbook()

    style = xlwt.easyxf("pattern: pattern solid, fore_colour yellow")

    for i in range(len(inat_files)):
        new_ws = new_wb.add_sheet(inat_filenames[i])
        this_file_inat_data = inat_data[i]
        
        # Store precisely which rows should be highlighted in this worksheet of the new Excel file
        should_highlight_row = []
        for j in range(len(this_file_inat_data)):
            should_highlight_row.append(False)
        for date in dates_flagged:
            if date in each_file_inat_entries_on_this_day[i]:
                for row in each_file_inat_entries_on_this_day[i][date]:
                    should_highlight_row[row] = True
        
        # Fill this worksheet of the new Excel file with data from the corresponding iNaturalist csv file, highlighting rows appropriately
        for r in range(len(this_file_inat_data)):
            for c in range(len(this_file_inat_data[0])):
                if should_highlight_row[r]:
                    new_ws.write(r, c, this_file_inat_data[r][c], style)
                else:
                    new_ws.write(r, c, this_file_inat_data[r][c])

    # Save the new Excel file
    new_wb.save(new_excel_filename)

    return [True, preview]



    # DEBUG
    print("\nDaily iNaturalist entries:")
    print(num_inat_entries_on_this_day)
    print("Daily Seadragon Search entries:")
    print(num_sds_entries_on_this_day)

# analyse_data_files("Seadragon Search sample.xls", ["iNat sample.csv"])