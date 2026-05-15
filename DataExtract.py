import os
import sys
import numpy as np

file1 = open("Batch9data.txt","w")

begfile = 1901
endfile = 2300

for i in range(begfile,endfile+1,1):
    Fname = open("run"+str(i)+'/Finaldata.txt',"r")
    data = Fname.readlines()
    for line in data:
        columns = line.split()
        if len(columns)==33 and float(columns[2])>=0 and float(columns[0])>=0:
            for j in range(len(columns)):
                file1.write(str(columns[j]))
                file1.write(' ')
            file1.write("\n")


