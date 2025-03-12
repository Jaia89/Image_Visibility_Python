### AUTHOR
# jacopo iacovacci

### DATE 
# 2019

### LIBRARIES
import pandas as pd
import numpy as np
from skimage.io import imread
import sys

### MAIN
# image file name to be passed as argument 1 in command line
fileName=sys.argv[1]
M=imread(fileName, as_gray=True)
M=M.astype(float)

n_rows=M.shape[0]
n_columns=M.shape[1]

if n_rows != n_columns:
    print("Warning ! : Image is not square")
    sys.exit(0)

f = open('edge_list_ivg.txt', 'w')

for i in range(0,n_rows):
    for j in range(0,n_columns):
  
    
####### first neighbors        
#        if j < n_columns-1:  
#            #print([n_columns*i+j,n_columns*i+j+1])
#            edge_list.append([n_columns*i+j,n_columns*i+j+1])
#               
#        if i < n_rows-1 and j < n_columns-1:
#            #print([n_columns*i+j,n_columns*(i+1)+j+1])
#            edge_list.append([n_columns*i+j,n_columns*(i+1)+j+1])
#      
#        if i < n_rows-1:
#            #print([n_columns*i+j,n_columns*(i+1)+j])
#            edge_list.append([n_columns*i+j,n_columns*(i+1)+j])
#    
#        if i < n_rows-1 and j > 0 :
#            #print([n_columns*i+j,n_columns*(i+1)+j-1])
#            edge_list.append([n_columns*i+j,n_columns*(i+1)+j-1])
#
####### visibility

    # along column  
        if i < n_rows-2:                     
            for r in range(i+2,n_rows):
                cond=1                
                for l in range(i+1,r):                      
                    if (M[l,j] >= M[i,j]+(M[r,j]-M[i,j])*(l-i)/(r-i)):
                        cond=0
                        break
                               
                if cond==1:
                    #edge_list.append([n_columns*i+j,n_columns*r+j])
                    f.write(str(n_columns*i+j) + '\t' + str(n_columns*r+j) +'\n')

 
   # along row
    
        if j < n_columns-2:                                   
            for c in range(j+2,n_columns):
                cond=1           
                for l in range(j+1,c): 
                    if (M[i,l] >= M[i,j]+(M[i,c]-M[i,j])*(l-j)/(c-j)):
                        cond=0
                        break      
                                 
                if cond==1:      
                     #edge_list.append([n_columns*i+j,n_columns*i+c])
                     f.write(str(n_columns*i+j) + '\t' + str(n_columns*i+c) +'\n')


    # along diag 1   
        if j < n_columns-2 and i < n_rows-2:
            diag_lenght=min(n_rows-1-i,n_columns-1-j)            
            r=i+2
            
            for c in range(j+2,j+diag_lenght+1):                                               
                cond=1                
                li=i+1
                
                for lj in range(j+1,c):                                        
                    if (M[li,lj] >= M[i,j]+(M[r,c]-M[i,j])*(lj-j)/(c-j)):
                        cond=0
                        break
                    li+=1
                    
                if cond==1:
                    #edge_list.append([n_columns*i+j,n_columns*r+c])
                    f.write(str(n_columns*i+j) + '\t' + str(n_columns*r+c) +'\n')
                r+=1
    
        
       # along diag 2 
        if  j > 1 and i < n_rows-2:
            diag_lenght=min(n_rows-1-i,j)         
            c=j-2
            
            for r in range(i+2,i+diag_lenght+1):
                cond=1                
                lj=j-1
                
                for li in range(i+1,r):                    
                    
                    if (M[li,lj] >= M[i,j]+(M[r,c]-M[i,j])*(lj-j)/(c-j)):
                        cond=0
                        break
                    lj=lj-1
                                
                if cond==1:                   
                    #edge_list.append([n_columns*i+j,n_columns*r+c])
                    f.write(str(n_columns*i+j) + '\t' + str(n_columns*r+c) +'\n')
                c-=1
f.close