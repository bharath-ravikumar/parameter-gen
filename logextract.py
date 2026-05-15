import os
import sys
import numpy as np

total_atoms = 0

for i in range(1901,2301,1):
    C = dict()
    C['M1'] = 1.0
    C['M2'] = 0.0
    C['M3'] = 0.0
    C['M4'] = 0.0
    C['M5'] = 0.0
    #print(os.getcwd()+"/run"+str(i))
    os.chdir(os.getcwd()+"/run"+str(i))
    file1 = open("log1.out","r")
    if file1 is False:
        continue
    data = file1.readlines()
    for line in data:
        if line.rstrip():
           columns = line.split()
           if len(columns)==5 and columns[4] in C.keys():
               C.update({columns[4]:columns[0]})
    Atom_array = np.fromiter(C.values(),dtype=float)
    total_atoms = np.sum(Atom_array)
    Atom_array = Atom_array/total_atoms
    file2 = open("Conc.txt","w")
    for i in range(np.size(Atom_array)):
        file2.write(str(np.round(Atom_array[i],decimals=3)))
        file2.write(" ")
    file1.close()
    file2.close()
    os.chdir("../")

