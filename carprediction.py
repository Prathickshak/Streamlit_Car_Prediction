import numpy as np
import pandas as pd
import pickle
import streamlit as st

def load_data():
    with open('car_model_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_data()
model = data['model']

def prediction():
    st.header("Welcome to Car Price Prediction")
    st.info("## Enter Your Car Details")

   # Define columns
    cols = st.columns(2)
    Year, Present_Price = cols[0], cols[1]
    
    cols = st.columns(2)
    Kms_Driven, Fuel_Type = cols[0], cols[1]

    cols = st.columns(2)
    Seller_Type, Transmission = cols[0], cols[1]
    
    Owner = st.columns(1)[0]
    
    # Collect user input
    x1 = Year.text_input("Enter the year of the car:")
    x2 = Present_Price.text_input("Present price of the car (in lakhs):")
    x3 = Kms_Driven.text_input("Kilo Meters Driven:")
    x4 = Fuel_Type.selectbox("Fuel Type:", ['Petrol', 'Diesel', 'CNG'])
    x5 = Seller_Type.selectbox("Seller Type:", ['Dealer', 'Individual'])
    x6 = Transmission.selectbox("Type Of Transmission:", ['Manual', 'Automatic'])
    x7 = Owner.text_input("Previous Owners of the Car:")

    ok = st.button("Predict")

    if ok:
        # Create DataFrame with input data
        car_data = pd.DataFrame([[x1, x2, x3, x4, x5, x6, x7]],
                                columns=['Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner'])

        # Encoding "Fuel_Type" column 
        car_data['Fuel_Type'] = car_data['Fuel_Type'].map({'Petrol': 0, 'Diesel': 1, 'CNG': 2})

        # Encoding "Seller_Type" column 
        car_data['Seller_Type'] = car_data['Seller_Type'].map({'Dealer': 0, 'Individual': 1})

        # Encoding "Transmission" column 
        car_data['Transmission'] = car_data['Transmission'].map({'Manual': 0, 'Automatic': 1})

        # Convert DataFrame to NumPy array
        car_data_array = car_data.values

        # Predict
        prediction = model.predict(car_data_array)

        # Display result
        st.write(f"The predicted price is: Rs. {prediction[0]:,.2f}")

# Call the prediction function
prediction()