# -*- coding: utf-8 -*-
"""
Created on Thu Apr 09 17:55:32 2015

@author: MaGesh
"""

import scipy
import random
import numpy as np
from scipy import io
from scipy.io import wavfile
from scipy import ff2t
from sklearn.preprocessing import normalize
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix

final_input=np.load('F:/fft_data.npy')#change the path to the file - Used the existing file to get the data
first_class=np.array(final_input[:100,:]) #splitted class wise for each classes classical
second_class=final_input[100:200,:] #second class jazz
third_class=final_input[200:300,:]#thrid class country
fourth_class=final_input[300:400,:]#fourth class pop
fifth_class=final_input[400:500,:]#fifth class rock
sixth_class=final_input[500:,:]#sixth class metal
"""finding the standard deviation of each matrices"""
"""finding the nearest value to the standard deviation of fft value and then taking the argsort of it"""
first_class_std=np.std(first_class) 
x1=np.argsort(np.argmin((first_class-first_class_std),axis=0)) 
x1=(x1[:20]) #Taking the top twenty 
second_class_std=np.std(second_class)
x2=np.argsort(np.argmin((second_class-second_class_std),axis=0))
x2=(x2[:20]) #Taking the top twenty
third_class_std=np.std(third_class)
x3=np.argsort(np.argmin((third_class-third_class_std),axis=0))
x3=(x3[:20]) #Taking the top twenty
fourth_class_std=np.std(fourth_class)
x4=np.argsort(np.argmin((fourth_class-fourth_class_std),axis=0))
x4=(x4[:20]) #Taking the top twenty
fifth_class_std=np.std(fifth_class)
x5=np.argsort(np.argmin((fifth_class-fifth_class_std),axis=0))
x5=(x5[:20]) #Taking the top twenty
sixth_class_std=np.std(sixth_class)
x6=np.argsort(np.argmin((sixth_class-sixth_class_std),axis=0))
x6=(x6[:20]) #Taking the top twenty
input_indicies=np.concatenate((x1,x2,x3,x4,x5,x6)) #Concatenate all the matrices
final_matrix=final_input[:,input_indicies] #taking up those values and saving it in a file called top_20
np.save('F:/top_20.npy',final_matrix)
