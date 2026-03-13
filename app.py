import streamlit as st
import pandas as pd
import joblib

st.title("⚡ EV Remaining Range Prediction")

# Load Model Files
model = joblib.load("linear_ev_model.pkl")
encoder = joblib.load("gear_encoder.pkl")
cols = joblib.load("model_columns.pkl")

# User Inputs
gear = st.selectbox("Gear Type", ["CY", "TorkZ"])
speed = st.slider("Speed (km/h)", 1, 40, 20)
distance = st.slider("Distance Covered (km)", 0, 170, 50)
current = st.slider("Current (Amp)", 5, 60, 20)
load = st.slider("Vehicle Load (kg)", 500, 1000, 800)
ambient = st.slider("Ambient Temperature (°C)", 15, 45, 30)

# Fixed constants (from research dataset)
voltage = 51.1
motor_temp = 28
controller_temp = 40
diff_temp = 31

# Feature Engineering
power = voltage * current / 1000
energy_km = power / speed
efficiency = speed / current
payload_ratio = (load - 450) / 450
tsi = (motor_temp + controller_temp + diff_temp) / (3 * ambient)
speed_drop = (35 - speed) / (distance + 1)
acc = 21 if gear == "CY" else 16

# Encode gear
gear_enc = encoder.transform([gear])[0]

# Create DataFrame
input_df = pd.DataFrame([[gear_enc, speed, distance, current, voltage,
                          load, payload_ratio, power, energy_km, efficiency,
                          motor_temp, controller_temp, diff_temp,
                          tsi, speed_drop, acc, ambient]],
                        columns=cols)

# Prediction
if st.button("Predict Remaining Range"):
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Remaining Range: {round(prediction,2)} km")