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
import pymysql
import numpy as np


# -------------------------------------------------toSQL--------------------------------- 
# Input : Data=Data to store to the database
#         parameters=Name of parameters corresponding to the data to store 
# Output : -
# Work :   
def toSQL(Data,Regime,parameters):
        
    # For query we need to get all the name of the columns
    list_parameters = ','.join(parameters)
    #The name are in the list and list_parameters contains the name as name1,name2,name3 etc...
    
    #we connect to the database
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='testdb')
    
    try:
        with connection.cursor() as cursor:
            Data=np.nan_to_num(Data) #All nan values are set to 0
    #We store all the data (all the 4500 samples for each of the 230 parameters)         
            for k in range (0,len(Data[0])):
                querry_d="INSERT into `table_regime` ("+list_parameters+") VALUES ({" + "},{".join((str(i) for i in range(0,len(Data)+len(Regime))))  + "})" ;
                regime_curr = [item[k] for item in Regime]
                # The 'Nan' values are replaced by the value "NULL" to be stored in the DB properly
                regime_curr2 = []
                for x in regime_curr:
                    if str(x) == 'nan': regime_curr2.append("NULL")
                    else: regime_curr2.append(str(x))    
                cursor.execute(querry_d.format(*np.transpose(Data)[k],*regime_curr2))
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
            cursor.execute ("select "+Name+ " from new_table_regime")
            # fetch all of the rows from the query
            data = cursor.fetchall ()
            
    finally:
        connection.close()        
    return data