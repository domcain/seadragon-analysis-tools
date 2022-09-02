import openpyxl as xl

inat_fieldname_date = "observed_on"
sds_fieldname_year = "encounter.year"
sds_fieldname_month = "encounter.month"
sds_fieldname_day = "encounter.day"
new_excel_filename = "relevant_iNaturalist_entries"


# This doesn't yet account for whatever happens when a field contains a double-quotation symbol
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


def verify_input_data(sds_filename, inat_filename):

    if not isinstance(sds_filename, str):
        print("The Seadragon Search filename passed to main was not of type 'string'")
        return False
    
    if not isinstance(inat_filename, str):
        print("The iNaturalist filename passed to main was not of type 'string'")
        return False
    
    return True


def format_date(year, month, day):
    if len(year) == 2:
        year = '20' + year
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    return year + '-' + month + '-' + day


def main(sds_filename, inat_filename):
    # Ensure that the arguments passed to 'main' are provided in the correct format
    if not verify_input_data(sds_filename, inat_filename):
        return
    
    # Open the iNaturalist csv file
    try:
        inat_file = open(inat_filename)
    except:
        print("The iNaturalist file cannot be found or cannot be opened")
        return
    
    # Read in the data from the iNaturalist csv file
    inat_data = [] # index 0 is the headings
    for line in inat_file:
        line = split_comma_separated_line(line.strip().lower())
        inat_data.append(line)
    inat_file.close()


    # Open the Seadragon Search Excel file
    try:
        sds_wb = xl.load_workbook(sds_filename)
    except:
        print("The Seadragon Search file cannot be found or cannot be opened as an Excel file")
        return
    try:
        sds_ws = sds_wb.worksheets[0]
    except:
        print("The Seadragon Search Excel file does not contain any worksheets")
        return
    
    # Find the minimum row and minimum column in the Seadragon Search Excel file
    sds_min_row = 0
    done = False
    for r in range(1, sds_ws.max_row + 1):
        for c in range(1, sds_ws.max_column + 1):
            if sds_ws.cell(row=r,column=c) is not None:
                sds_min_row = r
                done = True
                break
        if done:
            break

    sds_min_column = 0
    done = False
    for c in range(1, sds_ws.max_column + 1):
        for r in range(1, sds_ws.max_row + 1):
            if sds_ws.cell(row=r,column=c) is not None:
                sds_min_column = c
                done = True
                break
        if done:
            break

    # Find the maximum row and maximum column in the Seadragon Search Excel file (worksheet.max_row and worksheet.max_column can be too high)
    sds_max_row = 0
    for r in range(sds_min_row, sds_ws.max_row + 1):
        empty_row = True
        for c in range(sds_min_column, sds_ws.max_column + 1):
            if sds_ws.cell(row=r,column=c) is not None:
                empty_row = False
                break
        if empty_row:
            break
        else:
            sds_max_row = r

    sds_max_column = 0
    for c in range(sds_min_column, sds_ws.max_column + 1):
        empty_column = False
        for r in range(sds_min_row, sds_ws.max_row + 1):
            if sds_ws.cell(row=r,column=c) is not None:
                empty_column = False
                break
        if empty_column:
            break
        else:
            sds_max_column = c
    
    if sds_min_row == 0:
        assert(sds_min_column == 0)
        assert(sds_max_row == 0)
        assert(sds_max_column == 0)
        print("The (first worksheet in the) Seadragon Search Excel file is empty")
        return


    # Read in the data from the Seadragon Search Excel file
    sds_data = [] # index 0 is the headings
    for r in range(sds_min_row, sds_max_row + 1):
        line = []
        for c in range(sds_min_column, sds_max_column + 1):
            line.append(sds_ws.cell(row=r,column=c))
        sds_data.append(line)
    assert(sds_data)



    # Find the position of the relevant fieldnames
    try:
        inat_field_date = inat_data[0].index(inat_fieldname_date)
    except:
        print("Could not find column heading '" + inat_fieldname_date + "' in iNaturalist file")
        return
    try:
        sds_field_year = sds_data[0].index(sds_fieldname_year)
    except:
        print("Could not find column heading '" + sds_fieldname_year + "' in Seadragon Search file")
        return
    try:
        sds_field_month = sds_data[0].index(sds_fieldname_month)
    except:
        print("Could not find column heading '" + sds_fieldname_month + "' in Seadragon Search file")
        return
    try:
        sds_field_day = sds_data[0].index(sds_fieldname_day)
    except:
        print("Could not find column heading '" + sds_fieldname_day + "' in Seadragon Search file")
        return
    
    # Find the date of each iNaturalist entry
    inat_entries_on_this_day = {}
    inat_rows_missing_date = []
    for i in range(1, len(inat_data)):
        row = inat_data[i]
        date = row[inat_field_date]

        date_delimiter = "not_set_yet"
        for c in date:
            if c not in "0123456789":
                date_delimiter = c
                break
        if date_delimiter == "not_set_yet":
            inat_rows_missing_date.append(i)
            continue
        
        if date.count(date_delimiter) == 2:
            year, month, day = date.split(date_delimiter)
        else:
            inat_rows_missing_date.append(i)
            continue

        try:
            int(year)
            int(month)
            int(day)
        except:
            inat_rows_missing_date.append(i)
            continue

        my_date_string = format_date(year, month, day)

        if my_date_string not in inat_entries_on_this_day:
            inat_entries_on_this_day[my_date_string] = []
        inat_entries_on_this_day[my_date_string].append(i)
    
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

    # See which dates have more iNaturalist entries than Seadragon Search entries
    dates_flagged = {}
    for date, entries in inat_entries_on_this_day.items():
        num_inat_entries = len(entries)
        num_sds_entries = num_sds_entries_on_this_day.get(date, 0)
        diff = num_inat_entries - num_sds_entries
        if diff > 0:
            dates_flagged[date] = diff

    if dates_flagged:
        print("The Seadragon Search database appears to be missing:")
        for date, diff in dates_flagged.items():
            print(diff, "iNaturalist entries from", date)
    else:
        print("The Seadragon Search database appears to be up to date")
    
    # Make an Excel version of the iNaturalist csv file
    new_wb = xl.Workbook()
    new_ws = new_wb.active()

    for r in range(len(inat_data)):
        for c in range(len(inat_data[0])):
            new_ws.cell(row=r+1,column=c+1).value = inat_data[r][c]
    
    # TODO: Highlight rows in the new Excel file
    

    # Save the new Excel file
    new_wb.save(new_excel_filename)

    

    new_wb.close()
    sds_wb.close()



    print()
    print(sorted(inat_entries_on_this_day))
    print()
    print(sorted(num_sds_entries_on_this_day))




main("Seadragon Search sample.txt", "iNat sample.txt")