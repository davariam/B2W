import csv

# open the file in universal line ending mode
x = input("input yor file name".title())
x = x + '.csv'

with open(x,'r') as infile:
    # read the file as a dictionary for each row ({header : value})
    print('file is reading'.title())
    reader = csv.DictReader(infile)
    data = {}
    for row in reader:
        for header,value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]

# extract the variables you want
acc_id = data['acct_id']
bill_id = data['bill_id']
payment_id = data['payment_id']
# print(names[0])

from collections import defaultdict


def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)

    return tally


uniq_key = list(list_duplicates(acc_id).keys())
# print(uniq_key)
# print(uniq_key[0])
counter_dict = list_duplicates(acc_id).__len__()
counter = 0
str = ""
str2 = ""
while counter < counter_dict:
    print('please wait'.title())
    str = str + uniq_key[counter] + ","
    duplicate_index = list_duplicates(acc_id).pop(uniq_key[counter])
    for i in range(0,duplicate_index.__len__()):
        if i == 0:
            str = str + bill_id[duplicate_index[i]] + "," + payment_id[duplicate_index[i]] + ","
            # print(str)
        else:
            str = str + payment_id[duplicate_index[i]] + ","
            # print(str2)
    str = str + '\n'
    counter += 1
print("generating file".title())
flines = open("B2W_Report_Result.csv","w")
flines.write(str)
flines.close()
print('file under the name of:'.title() + " " + "B2W_Report_Result.csv")
