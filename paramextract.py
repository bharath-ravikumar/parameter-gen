import os
import sys
import numpy as np

file1 = open("parameters.settings","r")
data = file1.readlines()
m=5
n=5
Aatt=np.zeros((m,n))
fsize = int(m*(m+1)/2)
Afinal=np.zeros((fsize))
kb = 0.0
Fsrp = 0.0
Rsrp = 0.0
ind = 0
for line in data:
    if line.rstrip():
        columns = line.split()
        if columns[3]=='mdpd/diffcut':
            Aatt[int(columns[1])-1][int(columns[2])-1] = float(columns[4])
            B = float(columns[5])
            G = float(columns[6])
            rD = float(columns[9])
        if columns[0]=='bond_coeff':
            if float(columns[2])>0.0:
                kb = float(columns[2])
        if columns[3]=='srp':
            Fsrp = float(columns[4])
            Rsrp = float(columns[5])

for i in range(m):
    for j in range(i,n):
        Afinal[ind] = Aatt[i][j]
        ind += 1


file2 = open("Xdata1.txt","w")
for i in range(fsize):
    file2.write(str(Afinal[i]))
    file2.write(" ")
file2.write(str(B)+" ")
file2.write(str(G)+" ")
file2.write(str(rD)+" ")
file2.write(str(kb)+" ")
file2.write(str(Fsrp)+" ")
file2.write(str(Rsrp)+" ")
