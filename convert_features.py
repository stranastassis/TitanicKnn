import string
import numpy as np 
from math import *
def atof(s):
    s,_,_=s.partition(' ') # eg. this helps by trimming off at the first space
    while s:
        try:
            return float(s)
        except:
            s=s[:-1]
    return 0.0

def convert_fare(data):
    
    for passenger in data:
        fare = atof(passenger[6])
        
        if fare < 10:
            fare = 1
        elif fare >= 10 and fare < 20:
            fare = 2
        elif fare >= 20 and fare < 35:
            fare = 3
        else:
            fare = 4
            
        passenger[6] = fare
        
    return data
    
def convert_cabin(data):
    for passenger in data:
        if passenger[7] != '':
            passenger[7] = str(passenger[7])[0] # Keep the first letter A, B, C,..., T
        else:
            passenger[7] = 'U' # If cabin field is empty cabin = 'U'
   # -----------------------------------------------------
   # cabins = 'A','B','C','D','E','F','G','T','U'
   # num =     1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9
   # Convert caterogical to numerical ( A = 1, B = 2,...,U = 9)         
    num = { 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'T':8, 'U':9}
    for passenger in data:
        passenger[7] = num[passenger[7]]  
    
        
    return data
            
def convert_ageB(data):
    # Fill empty age fields by using the average age of passenger with same title (Mr, Mrs etc.)
    for passenger in data:
        myAge = passenger[3]
        if myAge == '':
            myTitle = passenger[1]    
            age = 0
            count = 0
            for tempPassenger in data:
                if tempPassenger[3] != '' and tempPassenger[1] == myTitle: # if the two passengers have the same title
                    age += float(tempPassenger[3])
                    count += 1
            passenger[3] = round(age / (count + 1))
    
    return data    

def relativies(data):
    # Family = SibSp + Parch
    for passenger in data:
        passenger[4] = int(passenger[4]) + int(passenger[5])

    alternative = True
    
    # if alone 1 else 0
    if alternative:
        for passenger in data:
            if float(passenger[4]) >= 1:
                passenger[5] = 0
            else:
                passenger[5] = 1
        
        
    
    return data
    
  
def convert_name(data):
    for passenger in data:
        passenger[1] = find_title(passenger)
     
    # -----------------------------------------------------
    num = { 'Mr':4, 'Mrs':3, 'Miss':2, 'Master':1, 'Other':4}
    for passenger in data:
        passenger[1] = num[passenger[1]]  
        
    
    return data
    
    # Find and store the important part of the name
def find_title(passenger):
    titles = ['Mrs', 'Mr', 'Master', 'Miss',] # 'Major', 'Ms', 'Mlle', 'Mme','Rev', 'Dr', 'Col', 'Capt', 'Countess', 'Don', 'Jonkheer']
    for title in titles:
        if string.find(passenger[1],title) != -1:
            return title
            
    return 'Other'
                
# Convert embarked ( S=>1, C=>2, Q=>3),
def convert_embarked(data):
    for passenger in data:
        location = passenger[8]
        if location == 'S':
            location = 1
        elif location == 'C':
            location = 2
        else:
            location = 3
        passenger[8] = location
    
    return data

# Another way to compute missing age values    
def convert_ageA(data):
    siblings = data[:,4]

    siblingsSet = np.unique(siblings)

    age_of_siblings = {} 

    num_of_siblings = {} 

    for num in siblingsSet:
        age_of_siblings[num] = 0
        num_of_siblings[num] = 0

    for passenger in data:
        sibSp = passenger[4]
        age = passenger[3] 
        if age != '':
            num_of_siblings[sibSp] += 1
            age_of_siblings[sibSp] += float(age)
    
    for passenger in data:
        sibSp = passenger[4]
        age = passenger[3]
        if  age == '':
            passenger[3] = int(age_of_siblings[sibSp] / (num_of_siblings[sibSp] + 1))
    
    
    return data
# Convert sex , female => 0 , male => 1
def convert_sex(data):
    for passenger in data:
        sex = passenger[2]
        if sex =='female':
            passenger[2] = 0
        elif sex == 'male':
            passenger[2] = 1
    
    return data;