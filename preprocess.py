from numpy import *
from convert_features import convert_ageB
from convert_features import convert_sex
from convert_features import convert_embarked
from convert_features import convert_name
from convert_features import relativies
from convert_features import convert_cabin
from convert_features import convert_fare
from infogain import infogain
from chiSQ import chiSQ
import operator
# Pclass Name Sex Age Relativies Fare | Cabin Embarked
def preprocess(data,Y,gain=False):
    # data = our dataset
    # Y = the labels of our dataset
    # gain , True if we want to compute information gain and metric x^2

    # Start of Preprocess------------------------------------------------------
    data = delete(data,0,1)         # Remove PassengerID column from matrix X 
    data = delete(data,6,1)         # Remove Ticket column from matrix X                            
    data = convert_name(data)       # Keep only the title (Mrs, Miss, Ms, Master, Other)
    data = convert_ageB(data)       # Fill empty age fields 
    data = convert_sex(data)        # male = 0 , female = 1
    data = convert_embarked(data)   # convert non-numerical to numerical (S => 1, C => 2, Q => 3)
    data = relativies(data)         # add sibSp and Parch

    data = convert_cabin(data)      # Keep only the first letter A21 => A etc.
    data = convert_fare(data)       # Sort fares in 4 clusters ( <10, >=10 and <20,>=20 and <35, >=35)
    
    # Compute imprortance of each attribute using InfoGain and X^2 methods---------------------------
    if gain:
        categories = ['Pclass', 'Name', 'Sex', 'Age', 'Family', 'Alone', 'Fare', 'Cabin','Embarked']
        gainIG = infogain(data,Y)
        gainSQ = chiSQ(data,Y)
    
        att_gainIG = {}
        att_gainSQ = {}
    
        counter = 0
        for cat in categories:
           att_gainIG[cat] = gainIG[counter]
           att_gainSQ[cat] = gainSQ[counter]
           counter += 1
       
        sorted_IG = sorted(att_gainIG.items(), key=operator.itemgetter(1), reverse=True)
        sorted_SQ = sorted(att_gainSQ.items(), key=operator.itemgetter(1), reverse=True)
        
        print "sorted_IG"
        for i in range(len(sorted_IG)):
            print str(i+1)+") "+str(sorted_IG[i])
        print "sorted_SQ"
        for i in range(len(sorted_SQ)):
            print str(i+1)+") "+str(sorted_SQ[i])  
    #--------------------------------------------------------------------------
   
    
    data = delete(data,-1,1)         # Remove embarked
    data = delete(data,-1,1)         # Remove cabin
    data = delete(data,3,1)         # Remove age
    #--------------------------------------------------------------------------
    return data
    
