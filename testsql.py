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

# ------------------ddd-------------------------------fromSQL--------------------------------- 
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
                , {220} , {221} , {222} , {223} , {224} , {225} , {226} , {227} , {228},{229})".format(sql_data[k,0], sql_data[k,1] , sql_data[k,2] , sql_data[k,3] , sql_data[k,4] , sql_data[k,5] , sql_data[k,6] , sql_data[k,7] , sql_data[k,8] , sql_data[k,9] , sql_data[k,10] , sql_data[k,11] , sql_data[k,12] , sql_data[k,13] , sql_data[k,14] , sql_data[k,15] , sql_data[k,16] , sql_data[k,17] , sql_data[k,18] \
                , sql_data[k,19] , sql_data[k,20] , sql_data[k,21] , sql_data[k,22] , sql_data[k,23] , sql_data[k,24] , sql_data[k,25] , sql_data[k,26] , sql_data[k,27] , sql_data[k,28] , sql_data[k,29] , sql_data[k,30] , sql_data[k,31] , sql_data[k,32] , sql_data[k,33] , sql_data[k,34] , sql_data[k,35] , sql_data[k,36]\
                , sql_data[k,37] , sql_data[k,38] , sql_data[k,39] , sql_data[k,40] , sql_data[k,41] , sql_data[k,42] , sql_data[k,43] , sql_data[k,44] , sql_data[k,45] , sql_data[k,46] , sql_data[k,47] , sql_data[k,48] , sql_data[k,49] , sql_data[k,50] , sql_data[k,51] , sql_data[k,52] , sql_data[k,53] , sql_data[k,54]\
                , sql_data[k,55] , sql_data[k,56] , sql_data[k,57] , sql_data[k,58] , sql_data[k,59] , sql_data[k,60] , sql_data[k,61] , sql_data[k,62] , sql_data[k,63] , sql_data[k,64] , sql_data[k,65] , sql_data[k,66] , sql_data[k,67] , sql_data[k,68] , sql_data[k,69] , sql_data[k,70] , sql_data[k,71] , sql_data[k,72]\
                , sql_data[k,73] , sql_data[k,74] , sql_data[k,75] , sql_data[k,76] , sql_data[k,77] , sql_data[k,78] , sql_data[k,79] , sql_data[k,80] , sql_data[k,81] , sql_data[k,82] , sql_data[k,83] , sql_data[k,84] , sql_data[k,85]\
                , sql_data[k,86] , sql_data[k,87] , sql_data[k,88] , sql_data[k,89] , sql_data[k,90] , sql_data[k,91] , sql_data[k,92] , sql_data[k,93] , sql_data[k,94] , sql_data[k,95] , sql_data[k,96] , sql_data[k,97] , sql_data[k,98] , sql_data[k,99] , sql_data[k,100] , sql_data[k,101] , sql_data[k,102]\
                , sql_data[k,103] , sql_data[k,104] , sql_data[k,105] , sql_data[k,106] , sql_data[k,107] , sql_data[k,108] , sql_data[k,109] , sql_data[k,110] , sql_data[k,111] , sql_data[k,112] , sql_data[k,113] , sql_data[k,114] , sql_data[k,115] , sql_data[k,116] , sql_data[k,117] , sql_data[k,118]\
                , sql_data[k,119] , sql_data[k,120] , sql_data[k,121] , sql_data[k,122] , sql_data[k,123] , sql_data[k,124] , sql_data[k,125] , sql_data[k,126] , sql_data[k,127] , sql_data[k,128] , sql_data[k,129] , sql_data[k,130] , sql_data[k,131] , sql_data[k,132] , sql_data[k,133] , sql_data[k,134]\
                , sql_data[k,135] , sql_data[k,136] , sql_data[k,137] , sql_data[k,138] , sql_data[k,139] , sql_data[k,140] , sql_data[k,141] , sql_data[k,142] , sql_data[k,143] , sql_data[k,144] , sql_data[k,145] , sql_data[k,146] , sql_data[k,147] , sql_data[k,148] , sql_data[k,149] , sql_data[k,150]\
                , sql_data[k,151] , sql_data[k,152] , sql_data[k,153] , sql_data[k,154] , sql_data[k,155] , sql_data[k,156] , sql_data[k,157] , sql_data[k,158] , sql_data[k,159] , sql_data[k,160] , sql_data[k,161] , sql_data[k,162] , sql_data[k,163] , sql_data[k,164] , sql_data[k,165]\
                , sql_data[k,166] , sql_data[k,167] , sql_data[k,168] , sql_data[k,169] , sql_data[k,170] , sql_data[k,171] , sql_data[k,172] , sql_data[k,173] , sql_data[k,174] , sql_data[k,175] , sql_data[k,176] , sql_data[k,177] , sql_data[k,178] , sql_data[k,179] , sql_data[k,180] , sql_data[k,181]\
                , sql_data[k,182] , sql_data[k,183] , sql_data[k,184] , sql_data[k,185] , sql_data[k,186] , sql_data[k,187] , sql_data[k,188] , sql_data[k,189] , sql_data[k,190] , sql_data[k,191] , sql_data[k,192] , sql_data[k,193] , sql_data[k,194] , sql_data[k,195] , sql_data[k,196] , sql_data[k,197]\
                , sql_data[k,198] , sql_data[k,199] , sql_data[k,200] , sql_data[k,201] , sql_data[k,202] , sql_data[k,203] , sql_data[k,204] , sql_data[k,205] , sql_data[k,206] , sql_data[k,207] , sql_data[k,208] , sql_data[k,209] , sql_data[k,210] , sql_data[k,211] , sql_data[k,212] , sql_data[k,213]\
                , sql_data[k,214] , sql_data[k,215] , sql_data[k,216] , sql_data[k,217] , sql_data[k,218] , sql_data[k,219] , sql_data[k,220] , sql_data[k,221] , sql_data[k,222] , sql_data[k,223] , sql_data[k,224] , sql_data[k,225] , sql_data[k,226] , sql_data[k,227] , sql_data[k,228],sql_data[k,229] ))
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