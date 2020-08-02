# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:54:45 2020

@author: A.DAVARI
"""
import os 
import gzip

def get_size(file_name=[]):
    size_list=[]
    for size in file_name:
        print(size)
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
        with gzip.open(file, "rt") as f:
            count = 0
            counter=0
            for line in f:
                line = line.strip('\n')
                if count == 1:
                    counter = line.count('|')
                    columns.append(counter+1)
                    print(counter)
                    break
                count = count+1
    return columns

def number_of_line(a_list_of_file=[]):

    
 


    

