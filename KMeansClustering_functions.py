#Please place your FUNCTION code for step 4 here.

#import statements
import numpy as np
import matplotlib.pyplot as plt
import random
import math

#custom functions
def openckdfile():
#opens ckd.csv and returns the values
#no parameters
#void
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
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
    
def random_centroids(k):
#creates random normalized centroids to use in testing
#1 parameter, k
#void
    centroids = []
    for i in range(k):
        glucose = random.randint(70, 490)
        hemoglobin = random.uniform(3.1, 17.8)        
        normal_glucose = (glucose - 70)/(490 - 70)       
        normal_hemoglobin = (hemoglobin - 3.1)/(17.8 - 3.1)
        centroids.append([normal_glucose, normal_hemoglobin])
    cent_array = np.array(centroids)
    return cent_array

def centroidDistanceArray(cent_array, glucose, hemoglobin):
    distance = []
    for i in range(len(cent_array)):
        dist = math.sqrt((cent_array[i][0] - glucose)**2 + (cent_array[i][1] - hemoglobin)**2)
        distance.append(dist)
    
    DistanceArray = np.array(distance)
    return DistanceArray

def centroid_class(centroids, glucose, hemoglobin):
    classes = []
    
    
    
    
    
def graphingKMeans(glucose, hemoglobin, assignment, centroids):
    plt.figure()
    for i in range(assignment.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    