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


def main(sds_filename, inat_filename):
    if not verify_input_data(sds_filename, inat_filename):
        return
    
    try:
        sds_file = open(sds_filename)
    except:
        print("The Seadragon Search file cannot be found or cannot be opened")
        return
    
    sds_header = sds_file.readline().strip().lower().split("\t")
    sds_data = []

    for line in sds_file:

        line = line.strip().split("\t")

        # Read in each piece of data on this line
        row = {}
        for i in range(len(line)):
            row[sds_header[i]] = line[i]
        sds_data.append(row)

    sds_file.close()



    try:
        inat_file = open(inat_filename)
    except:
        print("The iNaturalist file cannot be found or cannot be opened")
        return
    
    inat_header = inat_file.readline().strip().lower().split("\t")
    inat_data = []
    
    for line in inat_file:
        
        # THIS NEEDS TO BE CHANGED, DEPENDING HOW .numbers FILES (IN MACS) CREATE THEIR .csv FILES
        # e.g. what about when the file contains ',' and/or ';'
        line = line.strip().split("\t")

        # Read in each piece of data on this line
        row = {}
        for i in range(len(line)):
            row[inat_header[i]] = line[i]
        inat_data.append(row)

    inat_file.close()

    print(sds_data)
    print()
    print(inat_data)





main("Seadragon Search sample.txt", "iNat sample.txt")