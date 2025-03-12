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
fileName=sys.argv[1]

I = imread(fileName, as_gray=True)
I=I.astype(float)

n_rows=I.shape[0]
n_cols=I.shape[1]

# if n_rows != n_cols:
#     print("Warning ! : Image is not square")
#     sys.exit(0)

# stride param (set to 1)
stride=1
# patch size param (set to 3x3)
motif_size=3
pow2=[1,2,4,8,16,32,64,128]


Freq=np.zeros(256)
count=0

for i in range(0,n_rows-motif_size+1,stride):
    for j in range(0,n_cols-motif_size+1,stride):

        count=count+1
        string=np.zeros(8)

        M=I[i:i+motif_size,j:j+motif_size]

        if M[0,0]>M[0,1] and M[0,2]>M[0,1]:
            string[0]=1

        if M[0,2]>M[1,2] and M[2,2]>M[1,2]:
            string[1]=1

        if M[2,0]>M[2,1] and M[2,2]>M[2,1]:
            string[2]=1

        if M[0,0]>M[1,0] and M[2,0]>M[1,0]:
            string[3]=1

        if M[0,1]>M[1,1] and M[2,1]>M[1,1]:
            string[4]=1

        if M[1,0]>M[1,1] and M[1,2]>M[1,1]:
            string[5]=1

        if M[0,0]>M[1,1] and M[2,2]>M[1,1]:
            string[6]=1

        if M[0,2]>M[1,1] and M[2,0]>M[1,1]:
            string[7]=1


        label=np.int16(sum(string*pow2)+1)
        Freq[label-1]+=1


Freq=Freq/count

# output patch frequency sequence
f = open('patch_seq_ihvg.txt', 'w')
for i in range(0,256):
     f.write(str(Freq[i]) + '\n')
f.close
