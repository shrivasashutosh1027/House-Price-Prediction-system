import streamlit as st 
import pickle
import numpy as np

# load Model 
with open ("house_price_model.pkl","rb") as f:
    model=pickle.load(f)
st.title("House Price Prediction System")
st.sidebar.title("Navigation")#Side bar
page = st.sidebar.radio("Go to",["Introduction","Prediction"])

#Introductiom Page
if page=="Introduction":
    st.title("Welcome to the House Price Prediction Model")
    st.write("We make a House Price Prediction model which help you to make decision of purchasing house with best prices")

#Prediction Page
elif page=="Prediction":
    st.write_stream("Prediction")
    #Input fields
    lot_area = st.number_input("Lot Area(sq ft)",min_value=500,max_value=100000, step=100)
    year_built = st.number_input("Year Built",min_value=1800,max_value=2024, step=1)
    full_bath = st.number_input("Full Bathrooms",min_value=0,max_value=5, step=1)
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, step=1)
    garage_cars = st.number_input("Garage Cars", min_value=0, max_value=5, step=1)

    # Predict button
    if st.button("Predict Price"):
        features = np.array([[lot_area, year_built, full_bath, bedrooms, garage_cars]])
        prediction = model.predict(features)
        st.success(f"Estimated House Price: ${prediction[0]:,.2f}")