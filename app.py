import streamlit as st
import pandas as pd
import joblib

# 1. Page Configuration
st.set_page_config(page_title="Lassa Fever Risk Assessor", page_icon="🦠", layout="centered")

# 2. Load the trained model safely
@st.cache_resource
def load_model():
    # Make sure 'lassa_model.pkl' is in the same folder as this app.py file
    return joblib.load('lassa_model.pkl')
    
try:
    model = load_model()
except FileNotFoundError:
    st.error("Model file 'lassa_model.pkl' not found. Please ensure it is in the same directory as app.py.")
    st.stop()

# 3. National Database of State Baselines (Live 2026 Weather + NBS Data + Historical Counts)
# This powers the dynamic sliders for all 37 locations!
# Note: Weather values reflect the Jan-Feb 2026 dry season peak we fetched earlier.
# Historical counts (hist) are approximate based on typical Lassa belt data; adjust as needed from your actual notebook output.
state_database = {
    'Abia': {'temp': 27.93, 'rain': 21.20, 'pop': 3.7, 'pov': 29.8, 'hist': 2},
    'Adamawa': {'temp': 29.02, 'rain': 0.00, 'pop': 4.2, 'pov': 75.4, 'hist': 5},
    'Akwa Ibom': {'temp': 27.96, 'rain': 60.10, 'pop': 5.4, 'pov': 48.0, 'hist': 0},
    'Anambra': {'temp': 28.86, 'rain': 14.10, 'pop': 5.5, 'pov': 43.1, 'hist': 1},
    'Bauchi': {'temp': 25.74, 'rain': 0.00, 'pop': 6.5, 'pov': 73.0, 'hist': 20},
    'Bayelsa': {'temp': 27.57, 'rain': 139.10, 'pop': 2.2, 'pov': 88.0, 'hist': 0},
    'Benue': {'temp': 29.65, 'rain': 3.90, 'pop': 5.7, 'pov': 68.3, 'hist': 8},
    'Borno': {'temp': 25.34, 'rain': 0.00, 'pop': 5.8, 'pov': 56.4, 'hist': 3},
    'Cross River': {'temp': 28.06, 'rain': 22.40, 'pop': 3.8, 'pov': 57.0, 'hist': 1},
    'Delta': {'temp': 28.05, 'rain': 65.90, 'pop': 5.6, 'pov': 50.2, 'hist': 6},
    'Ebonyi': {'temp': 29.14, 'rain': 32.20, 'pop': 2.8, 'pov': 79.8, 'hist': 12},
    'Edo': {'temp': 27.98, 'rain': 52.10, 'pop': 4.2, 'pov': 35.4, 'hist': 50},
    'Ekiti': {'temp': 26.69, 'rain': 2.40, 'pop': 3.2, 'pov': 28.0, 'hist': 1},
    'Enugu': {'temp': 28.64, 'rain': 27.50, 'pop': 4.4, 'pov': 58.1, 'hist': 4},
    'FCT': {'temp': 29.11, 'rain': 0.00, 'pop': 3.5, 'pov': 38.6, 'hist': 3},
    'Gombe': {'temp': 27.22, 'rain': 0.10, 'pop': 3.2, 'pov': 62.3, 'hist': 4},
    'Imo': {'temp': 28.62, 'rain': 24.30, 'pop': 5.4, 'pov': 28.9, 'hist': 2},
    'Jigawa': {'temp': 24.95, 'rain': 0.00, 'pop': 5.8, 'pov': 87.0, 'hist': 1},
    'Kaduna': {'temp': 26.88, 'rain': 0.00, 'pop': 8.2, 'pov': 72.3, 'hist': 7},
    'Kano': {'temp': 25.31, 'rain': 0.00, 'pop': 13.0, 'pov': 66.3, 'hist': 5},
    'Katsina': {'temp': 25.55, 'rain': 0.00, 'pop': 7.8, 'pov': 72.7, 'hist': 2},
    'Kebbi': {'temp': 28.65, 'rain': 0.00, 'pop': 4.4, 'pov': 50.2, 'hist': 3},
    'Kogi': {'temp': 29.85, 'rain': 4.50, 'pop': 4.4, 'pov': 61.3, 'hist': 15},
    'Kwara': {'temp': 29.56, 'rain': 1.20, 'pop': 3.1, 'pov': 20.4, 'hist': 2},
    'Lagos': {'temp': 28.15, 'rain': 89.30, 'pop': 12.5, 'pov': 29.4, 'hist': 0},
    'Nasarawa': {'temp': 30.12, 'rain': 1.50, 'pop': 2.5, 'pov': 57.3, 'hist': 9},
    'Niger': {'temp': 30.05, 'rain': 0.00, 'pop': 5.5, 'pov': 66.1, 'hist': 4},
    'Ogun': {'temp': 28.45, 'rain': 35.60, 'pop': 5.2, 'pov': 26.1, 'hist': 1},
    'Ondo': {'temp': 27.16, 'rain': 11.80, 'pop': 4.6, 'pov': 27.9, 'hist': 45},
    'Osun': {'temp': 27.88, 'rain': 10.50, 'pop': 4.7, 'pov': 29.3, 'hist': 3},
    'Oyo': {'temp': 28.43, 'rain': 33.10, 'pop': 7.8, 'pov': 14.8, 'hist': 2},
    'Plateau': {'temp': 23.74, 'rain': 0.00, 'pop': 4.2, 'pov': 74.1, 'hist': 10},
    'Rivers': {'temp': 27.75, 'rain': 98.40, 'pop': 7.3, 'pov': 43.9, 'hist': 0},
    'Sokoto': {'temp': 28.15, 'rain': 0.00, 'pop': 4.9, 'pov': 90.5, 'hist': 2},
    'Taraba': {'temp': 30.31, 'rain': 0.10, 'pop': 3.0, 'pov': 87.9, 'hist': 15},
    'Yobe': {'temp': 24.85, 'rain': 0.00, 'pop': 3.2, 'pov': 83.5, 'hist': 1},
    'Zamfara': {'temp': 26.45, 'rain': 0.00, 'pop': 4.5, 'pov': 78.0, 'hist': 2}
}

# 4. App Header
st.title("🦠 Nigeria Lassa Fever Risk Assessor (2026)")
st.write("""
This epidemiological tool predicts the probability of a Lassa Fever outbreak based on real-time environmental triggers and socio-economic vulnerability. 
**Select a state to load its current baseline data, or adjust the sliders to simulate a future scenario!**
         
         Developed by Taiye Janet  Fagbolade
""")
st.markdown("---")

# 5. Sidebar - State Selection
st.sidebar.header("Input Regional Data")

# When the user picks a state, we grab that state's data from our dictionary
# We sort the keys so the states appear in alphabetical order in the dropdown
selected_state = st.sidebar.selectbox("Select State", sorted(list(state_database.keys())))
defaults = state_database[selected_state]

# 6. Dynamic Sliders (They automatically update based on 'defaults')
st.sidebar.subheader("Environmental Triggers")
#Format: slider("Name", min, max, default_value, step)
temp = st.sidebar.slider("Average Weekly Temp (°C)", 20.0, 45.0, float(defaults['temp']), 0.5)
rain = st.sidebar.slider("Total Weekly Rainfall (mm)", 0.0, 300.0, float(defaults['rain']), 1.0)

st.sidebar.subheader("Socio-Economic Factors")
population = st.sidebar.number_input("Population (Millions)", 1.0, 25.0, float(defaults['pop']), 0.1)
poverty = st.sidebar.slider("Poverty Rate (NBS MPI %)", 10.0, 95.0, float(defaults['pov']), 1.0)
history = st.sidebar.number_input("Historical Outbreaks (Count)", 0, 150, int(defaults['hist']))

# 7. Package the inputs for the Model
# MUST match the exact order of features used during XGBoost training
input_data = pd.DataFrame({
    'precipitation_sum': [rain],
    'temperature_2m_mean': [temp],
    'Population_Millions': [population],
    'Poverty_Rate_%': [poverty],
    'Historical_Outbreaks': [history]
})

# 8. Run Prediction
if st.button("Predict Outbreak Risk", type="primary"):
    with st.spinner('Analyzing spatial and environmental data...'):
        
        try:
            # Predict the probability of Class 1 (Outbreak)
            risk_prob = model.predict_proba(input_data)[0][1] * 100
            
            st.subheader(f"Risk Assessment for {selected_state}")
            
            # Determine the primary driver
            driver = "Endemic History" if history >= 5 else "Environmental Triggers"
            st.write(f"**Primary Risk Driver:** {driver}")
            
            # Visual Alerts
            if risk_prob >= 75:
                st.error(f"🚨 CRITICAL RISK: {risk_prob:.2f}% probability of an outbreak.")
                st.write("**Action:** Immediate deployment of PPE, rodent control, and community sensitization recommended.")
            elif risk_prob >= 40:
                st.warning(f"⚠️ ELEVATED RISK: {risk_prob:.2f}% probability of an outbreak.")
                st.write("**Action:** Heightened surveillance and preparation of local health facilities.")
            else:
                st.success(f"✅ LOW RISK: {risk_prob:.2f}% probability of an outbreak.")
                st.write("**Action:** Routine monitoring. Conditions are currently unfavorable for Lassa transmission.")
                
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
            st.write("Please check that the feature names in the app match exactly what the model was trained on.")
            
    st.markdown("---")
    st.caption("Model: XGBoost Classifier | Data Sources: NCDC, NBS (HDX), Open-Meteo ERA5 API")
