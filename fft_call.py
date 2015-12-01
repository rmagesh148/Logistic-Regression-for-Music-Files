# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 18:15:13 2015

@author: MaGesh

This program just stores the FFT data into NPY format and also stores the class labels in NPY format which will be used in LR_3.PY
"""
import scipy
import random
import numpy as np
from scipy import io
from scipy.io import wavfile
from scipy import fft
from sklearn.preprocessing import normalize
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix
class_matrix=[]

#For classical Music
n=np.zeros((1000,100))
for i in range(0,100):
    if i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\classical\\classical.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_classical=abs(fft(X1)[:1000]) #Taking the fft of classical 
        n[:1000,i]=fft_classical #Taking first 1000 rows of it
        class_matrix.append(int(0)) #Class_label matrix creation
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\classical\\classical.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_classical=abs(fft(X1)[:1000]) #Taking the fft of classical
        n[:1000,i]=fft_classical
        class_matrix.append(int(0))
n=n.transpose()
"""#For Jazz Music"""
n2=np.zeros((1000,100))
for i in range(0,100):
    if i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\jazz\\jazz.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_jazz=abs(fft(X1)[:1000]) #Taking the fft of Jazz
        n2[:1000,i]=fft_jazz #1000 rows
        class_matrix.append(int(1)) #Class label matrix
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\jazz\\jazz.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_jazz=abs(fft(X1)[:1000]) 
        n2[:1000,i]=fft_jazz
        class_matrix.append(int(1))
n2=n2.transpose()
#For Country Music
n3=np.zeros((1000,100))
for i in range(0,100):
    if i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\country\\country.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_country=abs(fft(X1)[:1000]) #Taking the fft of Country
        n3[:1000,i]=fft_country #first 1000 rows
        class_matrix.append(int(2)) #Class label matrix
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\country\\country.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_country=abs(fft(X1)[:1000])
        n3[:1000,i]=fft_country
        class_matrix.append(int(2))
n3=n3.transpose()
#For Pop Music
n4=np.zeros((1000,100))
for i in range(0,100):
    if i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\pop\\pop.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_pop=abs(fft(X1)[:1000]) #Taking the fft of pop
        n4[:1000,i]=fft_pop #Taking 1000 rows
        class_matrix.append(int(3)) #Class Matrix
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\pop\\pop.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_pop=abs(fft(X1)[:1000])
        n4[:1000,i]=fft_pop
        class_matrix.append(int(3))
n4=n4.transpose()
#For Rock Music
n5=np.zeros((1000,100))
for i in range(0,100):
    if i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\rock\\rock.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_rock=abs(fft(X1)[:1000]) #Taking the fft of rock
        n5[:1000,i]=fft_rock #Taking 1000 rows
        class_matrix.append(int(4)) #Class matrix
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\rock\\rock.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_rock=abs(fft(X1)[:1000])
        n5[:1000,i]=fft_rock
        class_matrix.append(int(4))
n5=n5.transpose()
#For Metal Music
n6=np.zeros((1000,100))
for i in range(0,100):
    if i in range(0,10):
        print i;
        X="C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\metal\\metal.0000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_metal=abs(fft(X1)[:1000]) #Taking the fft of metal
        n6[:1000,i]=fft_metal
        class_matrix.append(int(5)) #Class matrix
    else:
        print i
        X = "C:\\Users\\MaGesh\\Desktop\\LR_Project3\\opihi.cs.uvic.ca\\sound\\genres\\metal\\metal.000"+str(i)+".wav"
        sample_rate, X = scipy.io.wavfile.read(X)
        X1=np.array(X);
        fft_metal=abs(fft(X1)[:1000])
        n6[:1000,i]=fft_metal
        class_matrix.append(int(5))
n6=n6.transpose()
#Concatenate All the Normalized matrices to one
final_input=np.concatenate((n,n2,n3,n4,n5,n6))
class_matrix_final=np.array(class_matrix)
np.save('F:/fft_data.npy',final_input) #saivng it in a file named fft_data.npy
np.save('F:/class_label.npy',class_matrix) #saving it in a file named class_label.npy
