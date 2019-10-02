import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
myInp = pd.DataFrame()
size= pd.DataFrame()
type_= pd.DataFrame()
small = 0
medium = 1
large = 2
size = np.array([small, small, small, medium, medium, medium, large, large, large])
type_['Height (in Cms)']= [150, 155, 160, 165, 170, 175, 180, 185, 190]
type_['Weight (in Kgs)']= [65, 70, 75, 80, 85, 90, 95, 100, 105]
print("\n",type_,"\n\n")
types= np.array(type_)
classifier = KNeighborsClassifier(5)
classifier = classifier.fit(types, size)
h=float(input("Enter Height (in Cms): "))
w=float(input("Enter Weight (in Kgs): "))
myInp['Height (in Cms)']= [h]
myInp['Weight (in Kgs)']= [w]
myInp = np.array(myInp)
prediction = classifier.predict(myInp)
print("\nPredicted Shirt Size:")
if prediction == 0:
    print('Small!')
elif prediction == 1:
    print('Medium')
elif prediction == 2:
    print('Large')
