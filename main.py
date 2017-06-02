# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:45:10 2017

@author: i0A103166
"""

import readbinary as rb
import matplotlib.pyplot as plt
import testsql as sql
import numpy as np

DataFileName="_dataint32.bin"

Data,parameters=rb.readbinary(DataFileName) 

# Handle the regime parameter #
offset = 105-np.uint(Data[162][0]/(2**24))
Regime=[]
for i in range (offset,105):
    a=(np.uint64(Data[162][i::105]) & 65535)
    Regime.append(a)    
for i in range (0,offset):
    a=(np.uint64(Data[162][i::105]) & 65535)
    Regime.append(a)    


#sql.toSQL(Data,parameters)
##Some cleaning 
#Name = 'MUS'
#data=sql.fromSQL(Name)
#
#Name = 'Main_EO_CLEN_Ctxte'
#data1=sql.fromSQL(Name)


#list_parameters = ','.join(parameters)
#
#for k in range(0,len(parameters)):
#    print("`"+parameters[k]+"` DECIMAL(10) DEFAULT NULL,")