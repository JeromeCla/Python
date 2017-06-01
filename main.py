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

#Data,parameters=rb.readbinary(DataFileName) 
#sql.toSQL(Data,parameters)
#Some cleaning 
Name = 'Main_USA'
data=sql.fromSQL(Name)