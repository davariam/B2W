# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 21:42:03 2020

@author: A.DAVARI
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:54:45 2020

@author: A.DAVARI
"""
import os 
import gzip
import datetime
import py_compile
py_compile.compile('CreatingVerfFile_PY2.6_Version.py')

def get_date():
    today = datetime.datetime.now()
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    today_str = yesterday.strftime("%Y%m%d")
    yesterday_str = today.strftime("%Y%m%d%H%M%S")
    return today_str,yesterday_str
    

def get_size(file_name=[]):
    size_list=[]
    for size in file_name:
        size_list.append(os.path.getsize(size))
    return size_list

def list_of_file():
    list_gz_file=[]
    for x in os.listdir('.'):
        if x.endswith('.gz'):
            list_gz_file.append(x)
    return list_gz_file

def number_of_column(a_list_of_file=[]):
    columns = []
    for file in a_list_of_file:
        f = gzip.open(file, "rt")
        count = 0
        counter=0
        for line in f:
            line = line.strip('\n')
            if count == 1:
                counter = line.count('|')
                columns.append(counter+1)
                f.close()
                break
            count = count+1
    return columns

def number_of_line(a_list_of_file=[]):
    number_line = []
    for file in a_list_of_file:
        f = gzip.open(file, "rt")
        line_count = sum(1 for line in f)
        number_line.append(line_count)
        f.close()
    return number_line

def name_of_verf(name_of_file):
    name_of_verf = name_of_file
    name_of_verf_comlete = ''
    for char in name_of_verf:
        if char.isdigit():
            break
        name_of_verf_comlete = name_of_verf_comlete + char
    name_of_verf_comlete = name_of_verf_comlete+get_date()[0]+'_'+get_date()[1]+'.verf'
    return name_of_verf_comlete


list_of_gz_file = sorted(list_of_file())
size_of_gz_file = get_size(list_of_gz_file)
numb_of_gz_file = number_of_line(list_of_gz_file)
colu_of_gz_file = number_of_column(list_of_gz_file)

f = open(name_of_verf(list_of_gz_file[0]),"w") 
for name,size,num,col in zip(list_of_gz_file,size_of_gz_file,numb_of_gz_file,colu_of_gz_file):
   f.write(name+'|'+str(size)+'|'+str(num)+'|'+str(col)+'|'+get_date()[0]+'|'+get_date()[1]+'\n')
f.close()



    

