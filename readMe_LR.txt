README
Magesh Rajasekaran
mrajasekaran@unm.edu
04/10/2015

"""Use this readme file for all the Python programs mentioned below"""

Logistic Regression Music files Classifier

File Structure:
readme.txt
fft_call.py
fft_program.py
mfcc_call.py
mfcc_program.py
top_20.py
top_20_program.py
fft_data.NPY
ceps_data.NPY
top_20.NPY
class_label.NPY


Development Environment:
Logistic Regression Implementation for the music files classification was implemented in Python 2.7 which has Numpy, Scipy, Talkbox(skicits) Installed.  

Usage:
My python program is NOT compatible with Python 3.x, and I have not checked compatibility with any other versions. To run my program, please change the path file in the program(fft_program.py, mfcc_program.py, top_20_program.py) to give input for fft data, mfcc data and class label files. When you run the program, you'll be able to see the program printing Confusion_Matrix and the accuracy for the classification.  I have attached fft_data.NPY, ceps_data.NPY, top_20.NPY, class_labels.NPY please change the path in the respective programs to call these data directly and then run the program.

To change the path of the files for the fft or mfcc call, please do it in the line 18 for all the programs fft_program, top_20_program.py and mfcc_program.py. Also, please change the file path in the line 19 to read the class label files in the above mentioned programs. My program reads both the file at the same time and gives you the output. Each method, what I have defined, has the comments posted before the start of the method, kindly read through that. And, if you have any questions please write it to the above specified mail id. 

Output:

For FFT:
print the confusion matrix(you can see that in the report)
Accuracy : 47.83%

For MFCC:
print the confusion matrix(you can see that in the report)
Accuracy : 63.66%

For Top 20 features:
print the confusion matrix(you can see that in the report)
Accuracy : 40.13%