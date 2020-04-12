#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions

glucose, hemoglobin, classification = kmc.openckdfile()
glucose, hemoglobin, classification = kmc.normalizeData(glucose, hemoglobin, classification)
cent_array = kmc.select(2)
assignments = kmc.assign(cent_array, glucose, hemoglobin)
newcent = kmc.updateK(assignments, glucose, hemoglobin, cent_array)
assignments, newcent = kmc.iteration(assignments, newcent)

kmc.graphingKMeans(glucose, hemoglobin, assignments, newcent)   
kmc.accuracy(glucose, hemoglobin, classification, assignments)    
    
    