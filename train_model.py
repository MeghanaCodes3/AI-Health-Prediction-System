import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# diabetes
data=pd.read_csv("dataset.csv")

X=data.iloc[:,:-1]

y=data.iloc[:,-1]

model=RandomForestClassifier()

model.fit(X,y)

pickle.dump(
model,
open("diabetes.pkl","wb")
)

print("Diabetes model ready")

# heart
data=pd.read_csv("heart.csv")

X=data.iloc[:,:-1]

y=data.iloc[:,-1]

model=RandomForestClassifier()

model.fit(X,y)

pickle.dump(
model,
open("heart.pkl","wb")
)

print("Heart model ready")