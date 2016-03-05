from numpy import *
from kNN import kNN

def classify(trainSet, trainLabels, testSet,k=50):
	
	predictedLabels = zeros(testSet.shape[0])	
     
     # Use kNN algorithm in order to predict the labels
	for i in range(testSet.shape[0]):
			predictedLabels[i] = kNN(k, trainSet, trainLabels, testSet[i])

	return predictedLabels