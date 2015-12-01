# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 16:33:58 2015

@author: MaGesh
"""
import scipy
import random
import numpy as np
from scipy import io
from scipy.io import wavfile
from sklearn.preprocessing import normalize
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix
from scikits.talkbox.features import mfcc #mfcc function imported
value_matrix=[];
for i in range(0,100):
    if  i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\classical\\classical.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X) #mfcc function
        count_ceps=ceps.shape[0] #to find the rows
        fft_classical=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0) #taking mean of the function omitting 1 and last values
        value_matrix.append(fft_classical)        
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\classical\\classical.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X)
        count_ceps=ceps.shape[0]
        fft_classical=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0)
        value_matrix.append(fft_classical)
"""#For Jazz Music"""
for i in range(0,100):
    if  i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\jazz\\jazz.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X) #mfcc function
        count_ceps=ceps.shape[0] #to find the number of rows
        fft_jazz=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0)#taking mean of the function omitting 1 and last values
        value_matrix.append(fft_jazz)
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\jazz\\jazz.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X)
        count_ceps=ceps.shape[0]
        fft_jazz=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0)
        value_matrix.append(fft_jazz)
#For Country Music
for i in range(0,100):
    if  i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\country\\country.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X) #mfcc function 
        count_ceps=ceps.shape[0] #to find the number of rows
        fft_country=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0)#taking mean of the function omitting 1 and last values
        value_matrix.append(fft_country)
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\country\\country.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X) #mfcc function
        count_ceps=ceps.shape[0] #to find the number of rows
        fft_country=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0)
        value_matrix.append(fft_country)
#For Pop Music
for i in range(0,100):
    if  i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\pop\\pop.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X) #mfcc function
        count_ceps=ceps.shape[0] #to find the number of rows
        fft_pop=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0) #taking mean of the function omitting 1 and last values
        value_matrix.append(fft_pop)
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\pop\\pop.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X)
        count_ceps=ceps.shape[0]
        fft_pop=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0)
        value_matrix.append(fft_pop)    
#For Rock Music
for i in range(0,100):
    if  i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\rock\\rock.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X) #mfcc function
        count_ceps=ceps.shape[0] #to find the number of rows
        fft_rock=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0) #taking mean of the function omitting 1 and last values
        value_matrix.append(fft_rock)        
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\rock\\rock.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X)
        count_ceps=ceps.shape[0]
        fft_rock=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0) #taking mean of the function omitting 1 and last values
        value_matrix.append(fft_rock)
#For Metal Music
for i in range(0,100):
    if  i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\metal\\metal.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X) #Used MFCC function
        count_ceps=ceps.shape[0] #to find the number of rows 
        fft_metal=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0) #taking mean of the function omitting 1 and last values
        value_matrix.append(fft_metal)
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\metal\\metal.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        ceps, mspec, spec = mfcc(X)
        count_ceps=ceps.shape[0]
        fft_metal=np.mean(ceps[int(count_ceps*1/10):int(count_ceps*9/10)],axis=0)
        value_matrix.append(fft_metal)
np.save('F:/ceps_data.npy',value_matrix) #Saving it in a file ceps_data.npy
#End of the Program
