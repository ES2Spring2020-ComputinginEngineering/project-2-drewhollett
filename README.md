This project is based on an example and dataset from Data Science course developed at Berkeley (Data8.org).

Use: nothing required to do for all parts, simply run the program as many times as you wish, no inputs

ckd.csv contains dataset from which the programs were based. It contains the glucose, hemoglobin, and classification values for 158 different patients. NearestNeighborClassifier contains all programs and functions related to the nearest neighbor classifier as well as the k-nearest neighbor classifier. The KMeansClustering function file contains all functions useful for K-means clustering. The driver conatains the use of those functions to achieve the goal of clustering patients.

All data is derived from the files, with the exception of the centroids. The glucose, hemoglobin, and classification values are obtained from ckd.csv. These values are then standardized and can be used when comparing random test cases. 

Functions in KMeansClustering:
openckdfile - takes no arguements. This function opens the ckd.csv file and extracts the values from the tables, which it returns. 
normalizeData - it takes 3 arguements; glucose, hemoglobin, classification. This functions takes the values that were extracted from ckd.csv and scales them to values between 0 and 1 making it easier for the algorithims to use. Returns the scaled values
select - takes 1 arguement; K. This function creates a centroid array based on the arguement the user puts in. The length is what the user inputs while it will always be a 2d array. It will return the array.
assign - takes 4 arguements; cent_array, glucose, hemoglobin. This function assigns the centroid array a classification and calculates the distances to other points from the centroid. It returns the assignments of the centroids.
updateK - takes 4 arguements; assignments, glucose, hemoglobin, cent_array. This function will update the centroid points by taking the mean of all data points assigned to that centroid point. It will return the new centroid points. 
iteration - takes 2 arguements; assignments and newcent. This function will call assign and updateK in order to continuously be collecting data until the end point is reached, in my case 99. It will return the updated versionss of assignments and newcent
graphingKMeans - takes 4 arguements; glucose, hemoglobin, assignments, newcent. This function will graph all the ckd.csv points as well as the centroid group they are assigned to which gives it a classification of either ckd positive or negative. This function returns the graph.
accuracy - takes 4 arguements; glucose, hemoglobin, classification, and assignments. This function will calculate the percentage of correct positive and negative diagnoses, as well as the percentage of false positives and negatives. This function will return the percents for each positive and negative.























