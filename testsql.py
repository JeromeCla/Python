# -*- coding: utf-8 -*-
"""
Created on Tue May 30 09:52:06 2017

@author: i0A103166
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:48:31 2017

@author: i0A103166
"""
import scipy.io
import matplotlib.pyplot as plt
import pymysql
import numpy as np

# -------------------------------------------------fromSQL--------------------------------- 
def toSQL(Data,parameters):
    
    # For query we need to get all the name of the columns
    list_parameters = ','.join(parameters)
    #The name are in the list and list_parameters contains the name as name1,name2,name3 etc...
    
    #we connect to the database
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='testdb')
    
    #Define sql_data as matrix NxM with N=number of sample (4500) and M= number of features/parameters
    sql_data=np.zeros((len(Data[0]),len(Data)))
    
    try:
        with connection.cursor() as cursor:
            j=0
            while j<len(Data)-1: #We fill the matrix sql_data following the model defined above
                sql_data[:,j]=Data[j]
                j=j+1
            sql_data=np.nan_to_num(sql_data) #All nan values are set to 0
    
    #We store all the data (all the 4500 samples for each of the 228 parameters)         
            for k in range (0,len(Data[0])):
                print("INSERT into `new_table` ("+list_parameters+") VALUES ({" + "},{".join((str(i) for i in range(0,len(Data))))  + "})".format(*sql_data[k,:] ))
                cursor.execute("INSERT into `new_table` ("+list_parameters+") VALUES ({" + "},{".join((str(i) for i in range(0,len(Data))))  + "})".format(*sql_data[k,:] ))
        connection.commit()
    
    finally:
        connection.close()

# -------------------------------------------------fromSQL--------------------------------- 
# Input : Name=String of the parameter's name we want to retrieve
# Output : k = Position of the parameter's name in the .ini file        
def fromSQL(Name):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='testdb')            
    try:
        with connection.cursor() as cursor:
            # execute the SQL query using execute() method.
            cursor.execute ("select "+Name+ " from new_table")
            # fetch all of the rows from the query
            data = cursor.fetchall ()
            
    finally:
        connection.close()        
    return data