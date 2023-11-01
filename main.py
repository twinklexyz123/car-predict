import pandas as pd
import numpy as np
import datetime
# import xgboost as xgb
import streamlit as st



def main():
    html_temp = """
        <h1>Car Price Prediction</h1>
    """

    model = xgb.XGBRegressor()
    model.load_model("xgb_model.json")

    st.markdown(html_temp, unsafe_allow_html=True)

    st.markdown("This app will help you to predict your car selling price")

    p1 = st.number_input("Please enter ex-showroom price (In Lakhs)", 2.5,25.0,step=1.0)

    p2 = st.number_input("Please enter car driven (In Kilometers)",100,500000,step=100)

    s1 = st.selectbox("Select the fuel_type",("Petrol","Diesel","CNG"))

    if s1=='Petrol':
        p3=0
    elif s1=='Diesel':
        p3=1
    elif s1=='CNG':
        p3=2

    
if __name__ == '__main__':
    main()