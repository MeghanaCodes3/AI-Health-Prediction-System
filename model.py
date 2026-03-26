import pickle
import numpy as np

diabetes_model=pickle.load(
open("diabetes.pkl","rb")
)

heart_model=pickle.load(
open("heart.pkl","rb")
)

def predict_diabetes(

pregnancies,
glucose,
bp,
bmi,
age

):

    data=np.array([[

    pregnancies,
    glucose,
    bp,
    bmi,
    age

    ]])

    risk=diabetes_model.predict_proba(data)[0][1]

    return int(risk*100)

def predict_heart(

age,
cholesterol,
bp,
bmi

):

    data=np.array([[

    age,
    cholesterol,
    bp,
    bmi

    ]])

    risk=heart_model.predict_proba(data)[0][1]

    return int(risk*100)