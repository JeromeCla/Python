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



def strfindfile(DataFileName,SigName):
    k=[0,0]    
    FileNameIni = DataFileName[0:-3] + "ini"   
    with open(FileNameIni, 'r') as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
        b = bytearray()
        b.extend(SigName.encode())
        k[0]=s.find(b) 
        k[1]=s.find(b,k[0]+1) 
#    k=open(FileNameIni, 'r').read().find(SigName.astype(str),0)
    return k


def GetTraceFromFile(SigName, FileIniNames, DataFileName, vars, idx_deb, idx_fin, Signe):
    UndefinedVal=int('cafecafe',16)

    if Signe == 'pp':   Signe='+'
    if Signe == 'p':   Signe='+'
    if Signe == 'm':   Signe='-'
    

    SigName = SigName.astype(str) + ' ' 
    k=strfindfile(DataFileName,SigName)
    
    if not k:
        print ('La variable ' +SigName+ ' n''existe pas dans le fichier .ini')
    elif len(k)<2:
        print ('Le gain de la variable ' +SigName+ 'n''est pas défini dans le fichier .ini')

    LenIniFile = len(FileIniNames);

    substr=FileIniNames[k[0]:min(k[0]+100,LenIniFile)]
    substr_st = ''.join([chr(item) for item in substr])
    eq=substr_st.find('=')
    cr=substr_st.find(';')
    list_char=[chr(i) for i in FileIniNames[k[0]+np.arange(eq+1,cr)]]
    list_char=''.join(list_char)
    VarNr=int(list_char)

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


def readbinary(DataFileName):

    FileNameIni = DataFileName[0:-3] + "ini"
    
    
    fid=open(FileNameIni, 'r')
    FileIniNames=np.fromfile(fid, dtype=np.uint8)
    
    fid.close()
    
    vars = 235
    Te   = 0.004
    
    fd = open('Variable.txt','r');
    data = np.loadtxt(fd,
               delimiter=' ',
               dtype={'names': ('col1', 'col2', 'col3'),
               'formats': ('S30', 'f8', 'S1')})
    fd.close() 
    
    k1 = 0 ;
    k2 = math.inf ;
    
    Variable = []
    i=0 ;
    
    while i<len(data): 
        Variable.append(GetTraceFromFile(data[i][0], FileIniNames, DataFileName, vars, k1, k2, data[i][2].astype(str)))
    #    print(data[i][0].astype(str))
        i=i+1    
        print(i)
    return Variable,data.astype(str)
    


