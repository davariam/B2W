import csv
from collections import defaultdict
import progressbar
# from time import sleep
import os


def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return tally


# open the file in universal line ending mode
CSV_Name = input("input yor file name\n".title())
CSV_Name += '.csv'
ColA = input('Please input you first col name\n'.title())
ColB = input('Please input you first col name\n'.title())
ColC = input('Please input you first col name\n'.title())

with open(CSV_Name,newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open(CSV_Name,'w',newline='') as f:
    w = csv.writer(f)
    w.writerow([ColA,ColB,ColC])
    w.writerows(data)
    f.close()

with open(CSV_Name,'r') as infile:
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

header_in_csv_list = list(data.keys())
# extract the variables you want
acc_id = data[header_in_csv_list[0]]
bill_id = data[header_in_csv_list[1]]
payment_id = data[header_in_csv_list[2]]
uniq_key = list(list_duplicates(acc_id).keys())
counter_dict = list_duplicates(acc_id).__len__()
counter = 0
str = ""
print('please wait'.title())
print("generating file".title())
bar = progressbar.ProgressBar(maxval=counter_dict, \
                              widgets=[progressbar.Bar('=','[',']'),' ',progressbar.Percentage()])
bar.start()
while counter < counter_dict:

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
    bar.update(counter + 1)
    counter += 1

bar.finish()
str = ColA + ',' + ColB + ',' + ColC + '\n' + str
flines = open("B2W_Report_Result.csv","w")
flines.write(str)
flines.close()
print('file under the name of:'.title() + " " + "B2W_Report_Result.csv")
os.system('pause')
