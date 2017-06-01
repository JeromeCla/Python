# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:45:10 2017

@author: i0A103166
"""

import readbinary as rb
import matplotlib.pyplot as plt
#import testsql as sql
import numpy as np

#
l = [1, 5, 8]
sql_data = [1,2,3]
sql_query = "select name from studens where id in ({" + "},{".join((str(i) for i in range(0,3)))  + "})"
rep = "INSERT into `new_table` ("+str(l)+") VALUES ({" + "},{".join((str(i) for i in range(0,3)))  + "})".format(*sql_data[:] )

print (sql_query)
print(rep)

#DataFileName="_dataint32.bin"
#
#Data,parameters=rb.readbinary(DataFileName) 
#sql.toSQL(Data,parameters)
##Some cleaning 
#Name = 'Main_USA'
#data=sql.fromSQL(Name)