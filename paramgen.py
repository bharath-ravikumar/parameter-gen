# paramgen.py>

import os
import sys
import numpy as np

#function

def FFpara (Ntype,toss,nbtypes):
    Aatt = np.zeros((Ntype))
    for i in range(Ntype):
        Aatt[i] = np.round(np.random.uniform(-10,-120),decimals=2)
    Brep = np.round(np.random.uniform(10,80),decimals=2)
    gamma = np.round(np.random.uniform(12,16),decimals=2)
    rD = np.round(np.random.uniform(1.0,1.7),decimals=2)
    Fsrp = np.round(np.random.uniform(25,100),decimals=1)
    Rsrp = np.round(np.random.uniform(1.0,1.1),decimals=2)

    file3 = open("parameters.settings","w")

    for i in range(1,Ntype+1):
        file3.write('pair_coeff  '+str(i)+' '+str(i)+' mdpd/rhosum 0.75 ')
        file3.write('\n')
    if Ntype>1:
        for i in range(1,Ntype+1):
            for j in range(i+1,Ntype+1):
                file3.write('pair_coeff  '+str(i)+' '+str(j)+' mdpd/rhosum 0.75 ')
                file3.write('\n')

    for i in range(1,Ntype+1):
        Aii = Aatt[i-1]
        file3.write('pair_coeff  '+str(i)+' '+str(i)+' mdpd/diffcut '+str(Aii)+' '+str(Brep)+' '+str(gamma)+' 1.0 0.75 '+str(rD)+' 1.00 1.00')
        file3.write('\n')
    if Ntype>1:
        for i in range(1,Ntype+1):
            for j in range(i+1,Ntype+1):
                ff = np.round(np.random.uniform(0.1,2.5),decimals=2)
                Aij = np.round(ff*Aatt[i-1],decimals=2)
                file3.write('pair_coeff  '+str(i)+' '+str(j)+' mdpd/diffcut '+str(Aij)+' '+str(Brep)+' '+str(gamma)+' 1.0 0.75 '+str(rD)+' 1.00 1.00')
                file3.write('\n')

    if toss==1:
        file3.write('\n')
        for i in range(1,Ntype+1):
            file3.write('pair_coeff '+str(i)+' '+str(Ntype+1)+' none')
            file3.write('\n')
        file3.write('pair_coeff '+str(Ntype+1)+' '+str(Ntype+1)+' srp '+str(Fsrp)+' '+str(Rsrp))
        file3.write('\n')
        for j in range(nbtypes):
            kfene = np.round(np.random.uniform(10,60),decimals=1)
            file3.write('bond_coeff '+str(j+1)+' '+str(kfene)+' 1.5 1 1.0 ')
            file3.write('\n')

    else:
        file3.write('bond_coeff 1 '+str(0.0)+' 1.0 1 1.0 ')
        file3.write('\n')
        for i in range(1,Ntype+2):
            file3.write('pair_coeff '+str(i)+' '+str(Ntype+1)+' none')
            file3.write('\n')



