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
#opens file and returns data
#1 parameter filename
#void      
    glucose, hemoglobin, classification = np.loadtxt(filename, delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
#normalizes the data from the file
#3 parameters glucose, hemoglobin, classification
#void
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
#graphs the arrays
#3 parameters glucose, hemoglobin, classification
#displays the graph
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Confirmed non-CKD")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Confirmed CKD")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.title("Hemoglobin vs. Glucose correlation in CKD patients")
    plt.legend()
    plt.show()

def createTestCase():
#creates a random hemoglobin and glucose
#no parameters
#void    
    newglucose = random.randint(70, 490)
    newhemoglobin = random.uniform(3.8, 17.8)
    return newglucose, newhemoglobin

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
#calculates distance from random point to all other points
#4 parameters newglucose, newhemoglobin, glucose, hemoglobin
#void
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
#classifies point as ckd or non-ckd based on promiximity to other points
#5 parameters newglucose, newhemoglobin, glucose, hemoglobin, classification
#void
    distanceArray = calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin, classification)
    min_index = np.argmin(distanceArray)
    nearest_class = classification[min_index]
    return nearest_class

def graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification):
#graphs the random points and all other points
#5 parameters newglucose, newhemoglobin, glucose, hemoglobin, classification
#void
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
#returns a number based on index of 0 to 1 in proximity to points 0 being ckd, 1 being non-ckd
#6 parameters k, newglucose, newhemoglobin, glucose, hemoglobin, classification
#prints the k average
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
 #Uses all functions to predict a random point having ckd or not
 
glucose, hemoglobin, classification = openckdfile(filename)
newglucose, newhemoglobin = createTestCase()
kNearestNeighborClassifier(7, newglucose, newhemoglobin, glucose, hemoglobin, classification)
graphTestCase(newglucose, newhemoglobin, glucose, hemoglobin, classification)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    