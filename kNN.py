from numpy import *
from euclideanDistance import euclideanDistance

def kNN(k, X, labels, y):
    # Assigns to the test instance the label of the majority of the labels of the k closest 
	# training examples using the kNN with euclidean distance.

    m = X.shape[0] # number of training examples
    n = X.shape[1] # number of attributes

    closest = zeros(k) # stores the k closest to the test instance training examples and the distances
    
    # Compute distances
    distances = zeros(m)
    for i in range(m):
        distances[i] = euclideanDistance(X[i],y)
	
    
    # Find k closest neighbors
    for i in range(0,k):
        min = 0
        for j in range(0,m):
            if( distances[j] <= distances[min]):
                min = j
            
        
        closest[i] = labels[min]
        distances[min] = 10000
        min = 0
        m = m - 1


    survived = 0
    died = 0
    
    

    # Compute how many neighbors belong to each class
    for i in range(0,k): 
        if closest[i] == 1:
            survived += 1
        else:
            died += 1
            
            
    
    label = 0
    
    # Compute to which class belong the majority of the neighbors
    if survived >= died:
        label = 1
    else:
        label = 0
    
    return label

 
