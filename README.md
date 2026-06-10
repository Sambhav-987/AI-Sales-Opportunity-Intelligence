# AI Sales Opportunity Intelligence Platform

## About the Project

Sales teams often receive hundreds or even thousands of leads, but not every lead has the same chance of converting into a customer.

In this project, I built a machine learning system that predicts the likelihood of a lead converting and helps prioritize leads based on their conversion potential. The goal was to assist sales teams in focusing their efforts on the most promising opportunities.

## What I Did

* Performed Exploratory Data Analysis (EDA) on lead generation data
* Cleaned and preprocessed the dataset
* Handled missing values and encoded categorical variables
* Built and compared multiple machine learning models:

  * Logistic Regression
  * Random Forest
  * XGBoost
* Selected XGBoost as the final model based on performance
* Used SHAP to understand and explain model predictions
* Developed an interactive Streamlit dashboard for real-time lead scoring

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* SHAP
* Streamlit

## How It Works

1. User enters lead information through the dashboard.
2. The trained XGBoost model evaluates the lead.
3. The system predicts the probability of conversion.
4. The lead is classified as High, Medium, or Low Priority.
5. The dashboard provides a recommendation for sales follow-up.

## Key Learnings

This project helped me understand that successful machine learning projects are not only about model accuracy but also about data quality, feature engineering, explainability, and building solutions that create business value.

I also gained hands-on experience in model deployment and creating user-facing ML applications using Streamlit.

## Future Improvements

* Add Generative AI-based sales recommendations
* Integrate CRM data sources
* Automate lead follow-up suggestions
* Deploy the application on the cloud for real-world usage

## Author

Sambhav Srivastava
