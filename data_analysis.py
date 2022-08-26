delimiter = "\t"
inat_fieldname_date = "observed_on"
sds_fieldname_year = "encounter.year"
sds_fieldname_month = "encounter.month"
sds_fieldname_day = "encounter.day"

# THE DELIMITER IS CURRENTLY A TAB CHARACTER "\t". THIS NEEDS TO BE CHANGED, DEPENDING HOW .numbers FILES (IN MACS) CREATE THEIR .csv FILES
# Also, we have to deal with the data containing the delimiter character

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
    if not verify_input_data(sds_filename, inat_filename):
        return
    
    try:
        sds_file = open(sds_filename)
    except:
        print("The Seadragon Search file cannot be found or cannot be opened")
        return
    
    sds_data = [] # index 0 is the headings

    for line in sds_file:
        line = line.strip().lower().split(delimiter)
        sds_data.append(line)

    sds_file.close()
    if not sds_data:
        print("No data found in the Seadragon Search file")
        return


    try:
        inat_file = open(inat_filename)
    except:
        print("The iNaturalist file cannot be found or cannot be opened")
        return
    
    inat_data = [] # index 0 is the headings
    
    for line in inat_file:
        # THIS NEEDS TO BE CHANGED, DEPENDING HOW .numbers FILES (IN MACS) CREATE THEIR .csv FILES
        # e.g. what about when the file contains the delimiter?
        line = line.strip().lower().split(delimiter)
        inat_data.append(line)

    inat_file.close()
    if not inat_data:
        print("No data found in the iNaturalist file")
        return
    


    try:
        inat_field_date = inat_data[0].index(inat_fieldname_date)
    except:
        print("Could not find column heading '" + inat_fieldname_date + "' in iNaturalist file")
        print(inat_data[0])
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
    
    # Analyse each iNaturalist entry
    inat_entries_per_day = {}
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
        inat_entries_per_day[my_date_string] = inat_entries_per_day.get(my_date_string, 0) + 1
    
    # Analyse each Seadragon Search entry
    sds_entries_per_day = {}
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
        sds_entries_per_day[my_date_string] = sds_entries_per_day.get(my_date_string, 0) + 1

    # See which dates have more iNaturalist entries than Seadragon Search entries
    dates_flagged = {}
    for date, cnt in inat_entries_per_day.items():
        diff = cnt - sds_entries_per_day.get(date, 0)
        if diff > 0:
            dates_flagged[date] = diff

    if dates_flagged:
        print("The Seadragon Search database appears to be missing:")
        for date, diff in dates_flagged.items():
            print(diff, "iNaturalist entries from", date)
    else:
        print("The Seadragon Search database appears to be up to date")
    




    print()
    print(sorted(inat_entries_per_day))
    print()
    print(sorted(sds_entries_per_day))




main("Seadragon Search sample.txt", "iNat sample.txt")