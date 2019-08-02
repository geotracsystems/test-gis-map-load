import csv
from utils.csvhelper import *

# Get total rows, column names and lists of columns
column_names = []
wellid = []
uwi = []
origsourceid = []
sour = []
operator = []
spuddate = []
licdate = []
haccuracy = []
dls_address = []
nts_address = []
provstate = []
lastmodified = []
gid = []
surface_loc = []
field = []
geo = []
with open('well_can.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    lc = 0
    for row in csv_reader:
        if lc == 0:
            for item in row:
                column_names.append(item)
            lc = lc + 1
        else:
            wellid.append(row[0])
            uwi.append(row[1])
            origsourceid.append(row[2])
            sour.append(row[5])
            operator.append(row[8])
            spuddate.append(row[9])
            licdate.append(row[10])
            haccuracy.append(row[11])
            # dls_address.append(row[12])
            # nts_address.append(row[13])
            provstate.append(row[14])
            lastmodified.append(row[16])
            gid.append(row[20])
            # surface_loc.append(row[21])
            field.append(row[22])
            geo.append(row[24])
            lc = lc + 1

total_rows = lc - 1
print(total_rows)
total_columns = len(column_names)
print(total_columns, column_names)

print("All wellid unique") if all_unique(wellid) else print("not all unique")

print("No nulls wellid") if isall_notnull(wellid) else print("some nulls")

print("No nulls uwi") if isall_notnull(uwi) else print("some nulls")

print("No nulls origsourceid") if isall_notnull(origsourceid) else print("some nulls")

print("All nulls in sour") if isall_null(sour) else print("some values")

print(isvalid_datelist(spuddate))

print(isvalid_datelist(licdate))

print(isall_notnull(haccuracy))

print(isvalid_datelist(lastmodified))

print(isall_notnull(gid))

print(isall_null(field))

print(isall_notnull(geo))

rn = 0
for item in geo:
    rn = rn + 1
    if 'POINT (' not in item:
        print(rn,item)


with open('well_can.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    lc = 0
    invalid_flags = []
    for row in csv_reader:
        if lc == 0:
            lc = lc + 1
            continue
        else:
            invalid_flags.append(False)
            if row[14] == 'MB':
                if row[12] != '':
                    invalid_flags[lc - 1] = True
                if row[13] != '':
                    invalid_flags[lc - 1] = True
                if row[21] != '':
                    invalid_flags[lc - 1] = True
            elif row[14] == 'BC':
                if row[12] != '':
                    invalid_flags[lc - 1] = True
                if row[21] != '':
                    invalid_flags[lc - 1] = True
            elif row[14] == 'YT':
                if row[12] != '':
                    invalid_flags[lc - 1] = True
                if row[13] != '':
                    invalid_flags[lc - 1] = True
            else:
                if row[13] != '':
                    invalid_flags[lc - 1] = True
                if row[21] != '':
                    invalid_flags[lc - 1] = True

            lc = lc + 1

rn = 0
for stuff in invalid_flags:
    rn = rn + 1
    if stuff:
        print(rn, stuff)

