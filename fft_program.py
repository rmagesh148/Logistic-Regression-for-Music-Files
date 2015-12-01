# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scipy
import random
import numpy as np
from scipy import io
from scipy.io import wavfile
from scipy import fft #fft function
from sklearn.preprocessing import normalize
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix

final_input=np.load('F:/fft_data.npy') #change the file path to fft_data.NPY - fft data, please read the readme file 
class_matrix_final=np.load('F:/class_label.npy') #class files for the classifier

training_input=[];
testing_input=[];

kf=KFold(600,n_folds=10,shuffle=True) #cross-validation having 10 folds
for train,test in kf:
    training_input.append(train),testing_input.append(test)

penalty=0.001
final_confusion=np.zeros((6,6)) #final_confusion matrix declaring as zeros
neta=0.01

for value in range (0,len(kf)):
    probability_of_model=np.zeros((6,540)) 
    delta_matrix=np.zeros((6,540))
    weights=np.zeros((6,1001)) #weights initializing to zeros
    shuffle_train=np.random.permutation(training_input[value]) #used random permutation technique to shuffle the folded data and storing the indices of it
    shuffle_test=np.random.permutation(testing_input[value])
    training_data=final_input[shuffle_train] #with the shuffled indices calling the input matrix
    max_value=np.max(training_data,axis=0) #Normalizing the data by taking the maximum value of each rows
    training_data=np.true_divide(training_data,max_value) #Training data gets normalized
    input_matrix=np.ones((540,1001))
    input_matrix[:,1:]=training_data #Adding Bias weight
    training_data_t=input_matrix.transpose() 
    values_delta=class_matrix_final[shuffle_train]#passing the class matrix with the same indices what I have shuffled for training data
    k=len(values_delta)
    """ Creation of Delta Matrix"""
    for i in range(0,k):
        if (values_delta[i] == 0):
            delta_matrix[0,i]=1
        else:
            if (values_delta[i]==1):
                delta_matrix[1,i]=1
            else:
                if (values_delta[i]==2):
                    delta_matrix[2,i]=1
                else:
                    if (values_delta[i]==3):
                        delta_matrix[3,i]=1
                    else:
                        if (values_delta[i]==4):
                            delta_matrix[4,i]=1
                        else:
                            if (values_delta[i]==5):
                                delta_matrix[5,i]=1
    for j in range(0,2000):#2000 Epochs - Number of Epochs used
        neta=neta/(1+(j/2000)) #calculation of neta value
        output_matrix=weights.dot(training_data_t) #Logistic Regression Method
        output_matrix=np.exp(output_matrix) #Exponential of Weight * Training matrix
        output_matrix[5:,:]=1 
        sum_value=np.sum(output_matrix,axis=0)
        #sum_value=sum_value+1;
        probability_of_model=np.true_divide(output_matrix,sum_value) #Finding the probability matrix P(Y|X)
        difference=(delta_matrix)-(probability_of_model)
        difference=np.array(difference)
        weights=weights+(((neta)*(difference.dot(input_matrix)))-((neta*penalty)*weights)) #gradient descent
    testing_data=final_input[shuffle_test] #Using Test Data to classify
    max_value_test=np.max(testing_data,axis=0) #Normalizing the test data, so finding the maximum of it
    testing_data=np.true_divide(testing_data,max_value_test) #Normalized test data
    input_test_matrix=np.ones((60,1001))
    input_test_matrix[:,1:]=testing_data
    testing_data_t=input_test_matrix.transpose()
    test_output_matrix=weights.dot(testing_data_t) #Updated weights for each epochs goes here and multiplied with the testing data
    test_output_matrix=np.exp(test_output_matrix) #Exponential of Weight * Test data
    test_output_matrix[5:,:]=1
    sum_value_test=np.sum(test_output_matrix,axis=0)
    predict_model=np.true_divide(test_output_matrix,sum_value_test) #Finding the predict_model 
    predict_model=np.argmax(predict_model,axis=0) #Taking the argmax of the predict model 
    actual_model=class_matrix_final[shuffle_test] #using the same indices to classify the test data
    c1 =confusion_matrix(actual_model,predict_model) #Confusion matrix to find the accuracy
    final_confusion=c1+final_confusion # Summing up the confusion matrix for each folds
print final_confusion
acc=sum(final_confusion.diagonal())/float(600) # Final accuracy calculated with the final confusion matrix
acc=acc*100 #Accuracy converted to percentage
print "Accuracy Percentage",acc 
