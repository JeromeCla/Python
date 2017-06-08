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
Data,Regime,parameters=rb.readbinary(DataFileName) 
sql.toSQL(Data,Regime,parameters)
#
#Name = 'MUT'
#data=sql.fromSQL(Name)
#
#plt.plot(data1)



#list_parameters = ','.join(parameters)
#
#for k in range(0,len(parameters)):
#    print("`"+parameters[k]+"` DECIMAL(10) DEFAULT NULL,")