from __future__ import print_function
import numpy as np
import time
import math
#import tensorflow as tf
from six.moves import cPickle as pickle
from six.moves import range

from PIL import Image
from scipy.misc import imsave

dpath='/home/msingh/Documents/svhn/train_30/'

import csv
f=open(dpath+'digitStruct.csv','rb')

reader=csv.reader(f)
counter=0
mystruct={}
for row in reader:
    if counter==0:
        #print header
        #print (row)
        counter=counter+1
        continue
    else:
        #
        if row[0] in mystruct.keys():
            tmp=mystruct[row[0]]
            tmp['label']=tmp['label']*10+int(row[1])
            tmp['left']=min(tmp['left'],int(row[2]))
            tmp['top']=min(tmp['top'],int(row[3]))
            tmp['right']=max(tmp['right'],int(row[2])+int(row[4]))
            tmp['bottom']=max(tmp['bottom'],int(row[3])+int(row[5]))
        else:
            temp={}
            temp['name']=row[0]
            if row[1]=='10':
                row[1]='0'
            temp['label']=int(row[1])
            temp['left']=int(row[2])
            temp['top']=int(row[3])
            temp['width']=int(row[4])
            temp['height']=int(row[5])
            temp['bottom']=int(row[3])+int(row[5])
            temp['right']=int(row[2])+int(row[4])
            mystruct[row[0]]=temp

mykeys=mystruct.keys()
mykeys.sort()
for k in mykeys:
    tmpdict=mystruct[k]
    #print(tmpdict)

    filename=tmpdict['name']
    fpath=dpath+filename
    fpng=Image.open(fpath)
    fpng=fpng.convert('L')
    fpng_crop=fpng.crop((tmpdict['left'],tmpdict['top'],tmpdict['right'],tmpdict['bottom']))
    fpng_resized = fpng_crop.resize((28,28),Image.BICUBIC)
    fpng_data=np.array(fpng_resized, dtype='float32')
    if k =='5.png':
        print (k)        
        print(tmpdict)
        #print(fpng_data)
        fpng_resized.save('result.png')





#close file    
f.close()




