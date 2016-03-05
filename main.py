from numpy import *
from sklearn import cross_validation
import csv as csv
from classify import classify
from preprocess import preprocess


# Load data
csv_file_object = csv.reader(open('train.csv', 'rb')) # Load in the csv file
header = csv_file_object.next() 					  # Skip the fist line as it is a header
data=[] 											  # Create a variable to hold the data

for row in csv_file_object: # Skip through each row in the csv file,
    data.append(row[0:]) 	# adding each row to the data variable
X = array(data) 		    # Then convert from a list to an array.

y = X[:,1].astype(int) # Save labels to y 

X = delete(X,1,1) # Remove survival column from matrix X

# Manipulate our data
data = preprocess(X,y,True)
  
# Kaggle Submit --------------------------------------------------------------
trainSet1 = data
trainLabels1 = y

csv_file_object2 = csv.reader(open('test.csv', 'rb')) # Load in the csv file
header = csv_file_object2.next() 

data1 = []
for row in csv_file_object2: # Skip through each row in the csv file,
    data1.append(row[0:]) 	# adding each row to the data variable
G = array(data1) 

passId = G[:,0]

testSet1 = preprocess(G,y)

predictedLabels1 = classify(trainSet1,trainLabels1,testSet1)

target = open('myResult.csv', 'w')
target.write('PassengerId,Survived')
target.write("\n")
for i in range(len(passId)):
    target.write(passId[i])
    target.write(',')
    if predictedLabels1[i] == 1:
        target.write(str(1))
    else:
        target.write(str(0))
        
    target.write("\n")
    
    
target.close()
#END Kaggle Submit-------------------------------------------------------------



# Initialize cross validation
kf = cross_validation.KFold(data.shape[0], n_folds=10)

totalInstances = 0 # Variable that will store the total intances that will be tested  
totalCorrect = 0 # Variable that will store the correctly predicted intances  

for trainIndex, testIndex in kf:
    trainSet = data[trainIndex]
    testSet = data[testIndex]
    trainLabels = y[trainIndex]
    testLabels = y[testIndex]
	
    predictedLabels = classify(trainSet, trainLabels, testSet)

    correct = 0	
    for i in range(testSet.shape[0]):
        if predictedLabels[i] == testLabels[i]:
            correct += 1
        
    print 'Accuracy: ' + str(float(correct)/(testLabels.size))
    totalCorrect += correct
    totalInstances += testLabels.size
print 'Total Accuracy: ' + str(totalCorrect/float(totalInstances))


