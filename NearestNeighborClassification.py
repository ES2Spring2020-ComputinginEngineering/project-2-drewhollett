#Please put your code for Step 2 and Step 3 in this file.

#import statements
import numpy as np
import matplotlib.pyplot as plt
import random
import math

#Custom variables
filename = 'ckd.csv'

# FUNCTIONS
def openckdfile(filename):
    glucose, hemoglobin, classification = np.loadtxt(filename, delimiter=',', skiprows=1, unpack=True)
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

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
    distance = []
    scal_glu = (newglucose - 70)/(490 - 70)
    scal_hemo = (newhemoglobin - 3.1)/(17.8 - 3.1)
    classification = 0
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
    for i in range(158):
        dist = math.sqrt((scal_glu - glucose[i])**2 + (scal_hemo - hemoglobin[i])**2)
        distance.append(dist)
    distanceArray = np.array(distance)
    return distanceArray
        
def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distanceArray = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin, classification)
    min_index = np.argmin(distanceArray)
    nearest_class = classification[min_index]
    return nearest_class

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
    plt.figure()
    glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Confirmed non-CKD")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Confirmed CKD")
    plt.plot(((newhemoglobin - 3.1)/(17.8 - 3.1)), ((newglucose - 70)/(490 - 70)), "b.", markersize = 15)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Hemoglobin vs. Glucose correlation in CKD patients")
    plt.legend()
    plt.show()

def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
    distanceArray = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin)
    sorted_indices = np.argsort(distanceArray)
    k_indices = sorted_indices[:k]
    k_classifications = classification[k_indices]
    total = 0
    for i in range(len(k_classifications)):
        if k_classifications[i] == 1:
            total += 1
    k_av = float(total/len(k_classifications))
    return print(k_av)
    
 #Main script
 
glucose, hemoglobin, classification = openckdfile(filename)
newglucose, newhemoglobin = createTestCase()
kNearestNeighborClassifier(7, newglucose, newhemoglobin, glucose, hemoglobin, classification)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    