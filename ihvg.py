### AUTHOR
# jacopo iacovacci 2019

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

f = open('edge_list_ihvg.txt', 'w')

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
            k=i+1
            for r in range(i+2,n_rows):
                cond=1
                for l in range(k,r):
                    if M[l,j] >= M[i,j] or M[l,j] >= M[r,j]:
                        cond=0
                        k=l
                        break
                if M[l,j] >= M[i,j]:
                    break

                if cond==1:
                    #edge_list.append([n_columns*i+j,n_columns*r+j])
                    f.write(str(n_columns*i+j) + '\t' + str(n_columns*r+j) +'\n')
   # along row

        if j < n_columns-2:
            k=j+1
            for c in range(j+2,n_columns):
                cond=1
                for l in range(k,c):
                    if M[i,l] >= M[i,j] or M[i,l] >= M[i,c]:
                        cond=0
                        k=l
                        break
                if M[i,l] >= M[i,j]:
                     break

                if cond==1:
                     #edge_list.append([n_columns*i+j,n_columns*i+c])
                     f.write(str(n_columns*i+j) + '\t' + str(n_columns*i+c) +'\n')

    # along diag 1
        if  j < n_columns-2 and i < n_rows-2:
            kj=j+1
            ki=i+1
            diag_lenght=min(n_rows-1-i,n_columns-1-j)
            r=ki
            for c in range(j+2,j+diag_lenght+1):
                r=r+1
                cond=1
                li=ki-1
                for lj in range(kj,c):
                    li=li+1

                    if M[li,lj] >= M[i,j] or M[li,lj] >= M[r,c]:
                        cond=0
                        ki=li
                        kj=lj
                        break

                if M[li,lj] >= M[i,j]:
                    break

                if cond==1:
                    #edge_list.append([n_columns*i+j,n_columns*r+c])
                    f.write(str(n_columns*i+j) + '\t' + str(n_columns*r+c) +'\n')


       # along diag 2
        if  j > 1 and i < n_rows-2:

            kj=j-1
            ki=i+1

            diag_lenght=min(n_rows-1-i,j)
            c=kj

            for r in range(i+2,i+diag_lenght+1):

                c=c-1
                cond=1

                lj=kj+1

                for li in range(ki,r):

                    lj=lj-1

                    if M[li,lj] >= M[i,j] or M[li,lj] >= M[r,c]:
                        cond=0
                        ki=li
                        kj=lj
                        break

                if M[li,lj] >= M[i,j]:
                    break

                if cond==1:
                    #edge_list.append([n_columns*i+j,n_columns*r+c])
                    f.write(str(n_columns*i+j) + '\t' + str(n_columns*r+c) +'\n')

f.close