Predictive Modeling for Disease Outbreaks in Nigeria (Lassa Fever Risk Assessor)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost-green)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Completed-orange)

## Project Overview
This project is an end-to-end epidemiological machine learning pipeline designed to predict **Lassa Fever outbreaks** across all 36 states of Nigeria and the Federal Capital Territory (FCT). 

By integrating historical health records, live environmental satellite data, and socio-economic vulnerability metrics, this tool shifts public health strategy from *reactive* to *proactive*, enabling targeted resource allocation ahead of peak disease seasons.


**[Live Web Application - Click Here to View](())**

## Objectives
1.  **Analyze Drivers:** Determine the primary environmental and social factors that trigger Lassa Fever outbreaks.
2.  **Predict Risk:** Build a robust classification model to forecast outbreak probabilities regionally.
3.  **Explain the AI:** Use SHAP (SHapley Additive exPlanations) to provide transparent reasoning behind predictions.
4.  **Operationalize:** Deploy an interactive, user-friendly web application for public health stakeholders to simulate risk scenarios.

## Data Architecture
This project relies on a multi-source data engineering approach:
*   **Target Data (Historical Cases):** NCDC Situation Reports (via Kaggle).
*   **Environmental Data (Live Climate):** Temperature and Precipitation pulled via the **Open-Meteo ERA5 Satellite API**.
*   **Socio-Economic Data (Vulnerability):** Population density and the 2022 Multidimensional Poverty Index (MPI) sourced from the * * **National Bureau of Statistics (NBS)** and the Humanitarian Data Exchange (HDX).

## Tools & Technologies
*   **Language:** Python
*   **Data Engineering:** Pandas, NumPy, Requests (API Integration)
*   **Machine Learning:** Scikit-Learn, XGBoost
*   **Explainable AI (XAI):** SHAP
*   **Geospatial & Visualization:** Matplotlib, Folium
*   **Deployment:** Streamlit Community Cloud

## Methodology

### 1. Data Engineering & Preprocessing
*   Standardized geographic identifiers (State levels) across three disparate data sources.
*   Engineered critical epidemiological features, including **Incidence Rates** (Cases per 100k) and **Historical Endemicity** (past outbreak counts).
*   Handled missing data and converted temporal features (Daily to Epi-Weeks).

### 2. Model Training & Evaluation
We trained an **XGBoost Classifier** to predict the binary risk of an outbreak (1 = Outbreak, 0 = Safe).
*   **Accuracy:** 81%
*   **Recall (Outbreak Detection):** 83%
*   *The model successfully learned to balance "safe" weeks against highly infectious periods, minimizing false negatives which are critical in epidemiology.*

### 3. Explainable AI (SHAP Analysis)
SHAP summary plots revealed the underlying rules the model learned:
*   **Endemic History** is the strongest predictor of future risk.
*   **Environmental Triggers:** High temperatures and low rainfall (the dry season/Harmattan) push the *Mastomys* rat indoors, significantly increasing transmission risk.
*   **Social Vulnerability:** High poverty rates amplify the risk due to poor housing and sanitation, while raw population size showed minimal impact.

## Contributing
Contributions, issues, and feature requests are welcome. If you are a public health researcher or data scientist interested in expanding this to include Cholera or Meningitis, please reach out!

---
*Created by[Taiye Janet Fagbolade] | 3MTT Fellow*
