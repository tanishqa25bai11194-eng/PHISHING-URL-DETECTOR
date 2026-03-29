import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
'length':[20,120,35,140,22,150,40,130],
'https':[1,0,1,0,1,0,1,0],
'at':[0,1,0,1,0,1,0,1],
'dash':[0,1,0,1,0,1,0,1],
'digits':[0,5,0,6,0,7,1,8],
'suspicious':[0,1,0,1,0,1,0,1],
'ip':[0,1,0,1,0,1,0,1],
'label':[0,1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

X = df.drop("label",axis=1)
y = df["label"]

model = RandomForestClassifier()
model.fit(X,y)

pickle.dump(model,open("phishing_model.pkl","wb"))

print("Model trained successfully")