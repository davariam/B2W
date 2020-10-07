#! Python 3.4
import csv

"""
Open a file dialog window in tkinter using the filedialog method.
Tkinter has a prebuilt dialog window to access files.
This example is designed to show how you might use a file dialog askopenfilename
and use it in a program.
"""

from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

root = Tk()


# This is where we lauch the file manager bar.
def OpenFile():
    name = askopenfilename(initialdir="C:",
                           filetypes=(("Text File","*.csv"),("All Files","*.*")),
                           title="Choose a file."
                           )

    with open(name,'r') as infile:
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

    # Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
    except:
        print("No file exists")


Title = root.title("File Opener")
label = ttk.Label(root,text="Please open a CSV file:".title(),foreground="red",font=("Helvetica",16))
label.pack()

# Menu Bar

menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)

file.add_command(label='Open',command=OpenFile)
file.add_command(label='Exit',command=lambda: exit())

menu.add_cascade(label='File',menu=file)

root.mainloop()
