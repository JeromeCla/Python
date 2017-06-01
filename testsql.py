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
                cursor.execute("INSERT into `new_table` ("+list_parameters+") \
                VALUES ({0}, {1} , {2} , {3} , {4} , {5} , {6} , {7} , {8} , {9} , {10} , {11} , {12} , {13} , {14} , {15} , {16} , {17} , {18} , {19} , {20} , {21} , {22} , {23} , {24} , {25} , {26} , {27} , {28} , {29} , {30} , {31} , {32} , {33} , {34} , {35} , {36} , {37} , {38} , {39} , {40} , {41} , {42} , {43} , {44} , {45} , {46}\
                , {47} , {48} , {49} , {50} , {51} , {52} , {53} , {54} , {55} , {56} , {57} , {58} , {59} , {60} , {61} , {62} , {63} , {64} , {65} , {66} , {67} , {68} , {69} , {70} , {71} , {72} , {73} , {74} , {75} , {76} , {77} , {78} , {79} , {80} , {81} , {82} , {83} , {84} , {85} , {86} , {87} , {88} , {89} , {90} , {91} , {92} , {93}\
                , {94} , {95} , {96} , {97} , {98} , {99} , {100} , {101} , {102} , {103} , {104} , {105} , {106} , {107} , {108} , {109} , {110} , {111} , {112} , {113} , {114} , {115} , {116} , {117} , {118} , {119} , {120} , {121} , {122} , {123} , {124} , {125} , {126} , {127} , {128} , {129} , {130} , {131} , {132} , {133} , {134} , {135}\
                , {136} , {137} , {138} , {139} , {140} , {141} , {142} , {143} , {144} , {145} , {146} , {147} , {148} , {149} , {150} , {151} , {152} , {153} , {154} , {155} , {156} , {157} , {158} , {159} , {160} , {161} , {162} , {163} , {164} , {165} , {166} , {167} , {168} , {169} , {170} , {171} , {172} , {173} , {174} , {175} , {176} , {177}\
                , {178} , {179} , {180} , {181} , {182} , {183} , {184} , {185} , {186} , {187} , {188} , {189} , {190} , {191} , {192} , {193} , {194} , {195} , {196} , {197} , {198} , {199} , {200} , {201} , {202} , {203} , {204} , {205} , {206} , {207} , {208} , {209} , {210} , {211} , {212} , {213} , {214} , {215} , {216} , {217} , {218} , {219}\
                , {220} , {221} , {222} , {223} , {224} , {225} , {226} , {227} , {228},{229})".format(*sql_data[k,:] ))
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