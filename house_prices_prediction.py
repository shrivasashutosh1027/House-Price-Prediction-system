#Import important libraries
import pandas as pd
import numpy as np 
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#import dataset
df=pd.read_csv("house_prices.csv")

#save coloumns
df=df[["LotArea","YearBuilt","FullBath","BedroomAbvGr","GarageCars","SalePrice"]]

#Spliting data
X=df.drop("SalePrice", axis=1)
y=df["SalePrice"]

#Predict the model

#Train the model
X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.2,random_state=42)

#Train the model
model= LinearRegression()
model.fit(X_train,y_train)

#save model
with open("house_price_model.pkl","wb") as f:
    pickle.dump(model, f)

print("Success")