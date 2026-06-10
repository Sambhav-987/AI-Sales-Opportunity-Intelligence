import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("lead_scoring_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("AI Sales Opportunity Intelligence Platform")

st.header("Lead Conversion Predictor")

# Numeric Inputs
total_visits = st.number_input(
    "Total Visits",
    min_value=0.0,
    value=3.0
)

website_time = st.number_input(
    "Total Time Spent on Website",
    min_value=0,
    value=500
)

page_views = st.number_input(
    "Page Views Per Visit",
    min_value=0.0,
    value=2.0
)

# Dropdown Inputs
lead_origin = st.selectbox(
    "Lead Origin",
    [
        "Landing Page Submission",
        "Lead Add Form",
        "Lead Import",
        "Quick Add Form"
    ]
)

last_activity = st.selectbox(
    "Last Activity",
    [
        "Form Submitted on Website",
        "Had a Phone Conversation",
        "Olark Chat Conversation",
        "Page Visited on Website",
        "Resubscribed to emails",
        "SMS Sent",
        "Unreachable",
        "Unsubscribed"
    ]
)
lead_profile = st.selectbox(
    "Lead Profile",
    [
        "Lateral Student",
        "Other Leads",
        "Potential Lead",
        "Select",
        "Student of SomeSchool"
    ]
)

occupation = st.selectbox(
    "Occupation",
    [
        "Housewife",
        "Other",
        "Student",
        "Unemployed",
        "Working Professional"
    ]
)

city = st.selectbox(
    "City",
    [
        "Other Cities",
        "Other Cities of Maharashtra",
        "Other Metro Cities",
        "Select",
        "Thane & Outskirts",
        "Tier II Cities"
    ]
)

if st.button("Predict Conversion Probability"):

    # Empty feature vector
    input_df = pd.DataFrame(
        0,
        index=[0],
        columns=model_columns
    )

    # Numerical features
    input_df["TotalVisits"] = total_visits
    input_df["Total Time Spent on Website"] = website_time
    input_df["Page Views Per Visit"] = page_views

    # Lead Origin Encoding
    lead_origin_col = f"Lead Origin_{lead_origin}"
    if lead_origin_col in input_df.columns:
        input_df[lead_origin_col] = 1

    # Last Activity Encoding
    activity_col = f"Last Activity_{last_activity}"
    if activity_col in input_df.columns:
        input_df[activity_col] = 1

    # Lead Profile Encoding
    lead_profile_col = f"Lead Profile_{lead_profile}"
    if lead_profile_col in input_df.columns:
        input_df[lead_profile_col] = 1

    # Occupation Encoding
    occupation_col = f"What is your current occupation_{occupation}"
    if occupation_col in input_df.columns:
        input_df[occupation_col] = 1

    # City Encoding
    city_col = f"City_{city}"
    if city_col in input_df.columns:
        input_df[city_col] = 1

    # Prediction
    probability = model.predict_proba(input_df)[0][1]

    st.success(
        f"Conversion Probability: {probability:.2%}"
    )

    if probability >= 0.80:
        st.success("🔥 High Priority Lead")

    elif probability >= 0.50:
        st.warning("⚡ Medium Priority Lead")

    else:
        st.error("❄️ Low Priority Lead")
        