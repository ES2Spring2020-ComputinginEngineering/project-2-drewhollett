#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random


# FUNCTIONS
def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
    newglucose = []
    newhemoglobin = []
    
    for line in glucose:
        g_normal = (line-70)/(490-70)
        newglucose.append(g_normal)
    
    for line in hemoglobin:
        h_normal = (line-3.1)/(17.8-3.1)
        newhemoglobin.append(h_normal)    
   
    glucose_norm = np.array(newglucose)
    hemoglobin_norm = np.array(newhemoglobin)
    classification = np.array(classification)
    
    return glucose_norm, hemoglobin_norm, classification
    
def graphData(glucose, hemoglobin, classification):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Confirmed non-CKD")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Confirmed CKD")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Hemoglobin vs. Glucose correlation in CKD patients")
    plt.legend()
    plt.show()

def createTestCase():
    newglucose = random.randint(70, 490)
    newhemoglobin = random.uniform(3.8, 17.8)
    return newglucose, newhemoglobin
