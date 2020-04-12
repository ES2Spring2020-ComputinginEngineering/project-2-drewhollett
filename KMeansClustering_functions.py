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
    
def select(K):
#Creates the random centroids based on amount user wants    
#takes 1 parameter, K
#void
    return np.random.random((K, 2))

def assign(cent_array, glucose, hemoglobin):
#assigns the centroid array a classification and calculates distance for it
#3 parameters cent_array, glucose, hemoglobin
#void
    K = cent_array.shape[0]
    distances = np.zeros((K, len(hemoglobin)))
    for i in range(K):
        g = cent_array[i,1]
        h = cent_array[i,0]
        distances[i] = np.sqrt((hemoglobin-h)**2+(glucose-g)**2)
        
    assignments = np.argmin(distances, axis = 0)    
    return assignments

def updateK(assignments, glucose, hemoglobin, cent_array):
#updates location of centroid points by taking mean
#of all the data points that are assigned to that centroid
#4 parameters, assignments, glucose, hemoglobin, cent_array
#void
    assign = assignments.sort()
    K = cent_array.shape[0]
    newcent = np.zeros((K, 2))
    for i in range(K):
        glucosecent = np.mean(glucose[assign==i])
        hemoglobincent = np.mean(hemoglobin[assign==i])
        newcent[i] = np.append(glucosecent, hemoglobincent)
    return newcent
    
def iteration(assignments, newcent):
#keeps repeating assign and update functions for 100 times
#2 parameters assignments, newcent
#void
    iterations = 0
    while iterations < 100:
        assignments = assign(cent_array, glucose, hemoglobin)
        newcent = updateK(assignments, glucose, hemoglobin, cent_array)
        iterations += 1
    return assignments, newcent

def graphingKMeans(glucose, hemoglobin, assignment, newcent):
#graphs the ckd points as well as the centroids
#4 parameters glucose, hemoglobin, assignment, newcent
#void
    plt.figure()
    for i in range(assignment.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(newcent[i, 0], newcent[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()    

def accuracy(glucose, hemoglobin, classification, assignments):
#calculates true positive and negative diagnoses as well as false negatives and positives
#4 parameters glucose, hemoglobin, classification, assignments
#prints all percents for each catagory
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(158):
        if assignments[i]==0 and classification[i]==0:
            TP += 1
        if assignments[i]==1 and classification[i]==1:
            TN += 1
        if assignments[i]==1 and classification[i]==0:
            FN += 1
        if assignments[i]==0 and classification[i]==1:
            FP += 1
    TrueP = int((TP/158)*100)
    TrueN = int((TN/158)*100)
    FalseN = int((FN/158)*100)
    FalseP = int((FP/158)*100)
    print("Percentage of correct positive diagnoses " + str(TrueP) + "%")
    print("Percentage of correct negative diagnoses " + str(TrueN) + "%")
    print("Percentage of false negative diagnoses " + str(FalseN) + "%")
    print("Percentage of false positive diagnoses " + str(FalseP) + "%")
    
#Main script


glucose, hemoglobin, classification = openckdfile()
glucose, hemoglobin, classification = normalizeData(glucose, hemoglobin, classification)
cent_array = select(2)
assignments = assign(cent_array, glucose, hemoglobin)
newcent = updateK(assignments, glucose, hemoglobin, cent_array)
assignments, newcent = iteration(assignments, newcent)

graphingKMeans(glucose, hemoglobin, assignments, newcent)   
accuracy(glucose, hemoglobin, classification, assignments)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    