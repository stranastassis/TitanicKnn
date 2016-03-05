from math import *

def euclideanDistance(passenger1, passenger2):
    
	# Computes the euclidean distance between two vectors. The
	# two vectors must have the same size.

    len1 = len(passenger1) 
    len2 = len(passenger2) 
	
    assert len1 == len2, 'The two passengers must have the same attributes'
	
    distance = 0
    # 
    weights = []
    weights.append(1)   # Weight of Pclass
    weights.append(0.5) # Weight of Title
    weights.append(1)   # Weight of Sex
    weights.append(0.3) # Weight of Family = SibSp + Parch
    weights.append(0.5) # Weight of Alone ( if alone 1 else 0)
    weights.append(1)   # Weight of Fare
    
    # Compute distances 
    for i in range(len1):
		distance = distance + pow(weights[i]*(float(passenger1[i])-float(passenger2[i])),2)
		
    distance = sqrt(distance)
	
    return distance

