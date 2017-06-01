# -*- coding: utf-8 -*-
"""
Created on Tue May 30 13:28:49 2017

@author: i0A103166
"""

import scipy.io
import matplotlib.pyplot as plt
import pymysql
import numpy as np
import math
import mmap


# -------------------------------------------------strfindfile--------------------------------- 
# Input : DataFileName=String of full path of the binary file .bin
#         SigName = String of the parameter to find
# Output : k = Position of the parameter's name in the .ini file


def strfindfile(DataFileName,SigName):
    k=[0,0]
    SigName = SigName + ' ' #The whitespace is necessary to search the exact variable     
    FileNameIni = DataFileName[0:-3] + "ini"   
    with open(FileNameIni, 'r') as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        b = bytearray()
        b.extend(SigName.encode())
        k[0]=s.find(b) 
        k[1]=s.find(b,k[0]+1) 
    return k

# -------------------------------------------------GetTraceFromFile--------------------------------- 
# Input : SigName = String of the parameter to find 
#         FileIniName = String of full path of the file .ini
#         DataFileName = String of full path of the binary file .bin
#         vars = 
#         idx_deb = index of first sample
#         idw__fin = index of last sample (value can be inf to be sure to get all the samples)
#         Signe = Whether this parameter is (un)signed          
# Output : Trace = Array of array representing a matrix MxN where M:Number of parameters
#                                                                 N: Number of samples
# Work : 

def GetTraceFromFile(SigName, FileIniNames, DataFileName, vars, idx_deb, idx_fin, Signe):
    UndefinedVal=int('cafecafe',16)

    if Signe == 'pp':   Signe='+'
    if Signe == 'p':   Signe='+'
    if Signe == 'm':   Signe='-'
    
    k=strfindfile(DataFileName,SigName)
    
    if not k:
        print ('La variable ' +SigName+ ' n''existe pas dans le fichier .ini')
    elif len(k)<2:
        print ('Le gain de la variable ' +SigName+ 'n''est pas défini dans le fichier .ini')

    LenIniFile = len(FileIniNames);

# Exctract the vparameter's number (i.e id)
    substr=FileIniNames[k[0]:min(k[0]+100,LenIniFile)]
    substr_st = ''.join([chr(item) for item in substr])
    eq=substr_st.find('=')
    cr=substr_st.find(';')
    list_char=[chr(i) for i in FileIniNames[k[0]+np.arange(eq+1,cr)]]
    list_char=''.join(list_char)
    VarNr=int(list_char)

# Extract the gain (or unit) of the parameter
    substr=FileIniNames[k[1]:min(k[1]+100,LenIniFile)]
    substr_st = ''.join([chr(item) for item in substr])
    eq=substr_st.find('=')
    cr=substr_st.find(';')
    list_char=[chr(i) for i in FileIniNames[k[1]+np.arange(eq+1,cr)]]
    list_char=''.join(list_char)
    VarGain=float(list_char)
    
    fid=open(DataFileName, 'r');
    skip_deb=vars*(idx_deb);
    n_samples = idx_fin - idx_deb + 1;
    fid.seek(skip_deb*4)  # *4 : conv offset int32 -> bytes
    FenetreLecture_size = 10000 * vars;    
    if np.isinf(n_samples): Trace=np.zeros(1e6)
    else: Trace=np.zeros(n_samples,1)
    
    n=0    
    while (1):
      Data0=scipy.fromfile(fid,'uint32', FenetreLecture_size)
      if len(Data0)==0: 
          n_samples=n 
          break
      Data0 = Data0[VarNr::vars]
      Trace[n:n+len(Data0)] = Data0
      n=n+len(Data0)
      if n >= n_samples:
        break
      
    
    Trace=Trace[0:n_samples-1];
    fid.close()
    
    Trace[Trace==UndefinedVal]=np.nan;
    if Signe=='-': 
        Trace = Trace - 2**32*(Trace>=2**31)
    Trace = Trace * VarGain;
    
    return Trace

# -------------------------------------------------readbinary--------------------------------- 
# Input : DataFileName=String of full path of the binary file .bin
# Output : Variable = Array of array representing a matrix MxN where M:Number of parameters
#                                                                    N: Number of samples
#          Example: Data[i][j] calls the value representing the ith parameter for the jth sample
# Work : 1) The function open a file "Variable.txt" representing :
#               a. All the parameters' name : data[i][0]
#               b. Their corresponding number (i.e id) : data[i][1] (not used here)
#               c. If they are signed or unsigned data[i][2]
#        2) The function fills the array Variable with the function GetTraceFromFile 
#           that returns all the samples for a given parameter    
       
def readbinary(DataFileName):

    FileNameIni = DataFileName[0:-3] + "ini"
        
    fid=open(FileNameIni, 'r')
    FileIniNames=np.fromfile(fid, dtype=np.uint8)    
    fid.close()
    
    vars = 235
    Te   = 0.004
    
    with open('Variable.txt','r') as fd:
        data = np.loadtxt(fd, delimiter=' ', dtype={'names': ('col1', 'col2', 'col3'), 'formats': ('S30', 'f8', 'S1')})
    
    data=data.astype(str)
    index_start = 0 ;
    index_end = math.inf ;
    
    Variable = []
    
    for i in range (0,len(data)): 
        Variable.append(GetTraceFromFile(data[i][0], FileIniNames, DataFileName, vars, index_start, index_end, data[i][2]))
    return Variable,data
    


