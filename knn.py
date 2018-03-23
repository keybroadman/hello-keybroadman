# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:02:35 2018

knn mnist
文件为图片格式，文件名包含了标签和一些其他信息

/////////其中有问题，就是num1,num2的值不对。

@author: Administrator
"""
from numpy import *
from os import listdir

def classify(indt,dataset,labels,k):
    datasize=dataset.shape[0]
    diff=numpy.tile(indt,(datasize,1))-dataset
    diffsq=(diff**2)
    diffsqrt=(diffsq.sum(axis=1))**0.5
    sortsquence=diffsqrt.argsort()
    classcount={}
    for i in range(k):
        votelabel=labels(sortsquence[i])
        classcount[votelabel]=classcount.get(votelabel,0)+1
    sortclass=sorted(classcount.values, reverse= True )
    return sortclass[0][0]
    

def img2vector(filename):
    image=open (filename)    
    num1=len(image[0])
    num2=len(image[1])
    revector=numpy.zeros((1,num1*num2))
    for i in range(num1):
        imagestr=image.readline()
        for j in range(len(num2)):
            revector[0,num2*i+j]=int (imagestr[j])
    return revector

    
def knnclass():
    hwlable=[]
    trainlist=listdir('trainingdigits')
    m=len(trainlist)
    hwimages=numpy.zeros((m,num1*num2))    #wonder has problem
    for i in range(m):
        filenamestr=trainlist[i]
        fileinfor=filenamestr.split('.')[0]
        filelabel=fileinfor.split('_')[0]
        hwlable.append(filelabel)
        hwimages[i,:]=img2vector(filenamestr)
    #above is read the iamges
    # next are calculate the distance
    testlist=listdir('testdata')
    nt=len(testlist)
#    testimage=numpy.zeros(nt,num1*num2)
    labelsknn=[]
    error=0
    for j in range(nt):
        testfile=testlist[1]
        testimage=img2vector(testfile)
        testinfor=testfile.split('.')[0]
        testlabel=testinfor.split('_')[0]
        callabel=classify(testimage,hwimages,hwlable,3)
        labelsknn.append(callabel)
        if testlabel!=callabel:
            error+=1
        
        
    
            
        
    
