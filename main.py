import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.tree import DecisionTreeRegressor

# Uncomment these imports when your team installs tabpfn and wandb.
# from tabpfn import TabPFNRegressor
# import wandb

st.set_page_config(page_title="Data Science Final", layout="wide")
st.sidebar.title("Data Science Final")
page = st.sidebar.selectbox("Page", [
    "Business Case and Data",
    "Data Visualization",
    "Model Predictions",
    "Feature Importance",
    "Hyperparameter Tuning",
    "Conclusion",
])

# Load the team's dataset here once so every page can use the same DataFrame.

if page == "Business Case and Data":
    st.title("Business Case and Data")
    # Explain who will use the prediction and what decision it helps them make.
    # Give the data source, explain what one row represents, and preview the target and inputs.

elif page == "Data Visualization":
    st.title("Data Visualization")
    # Plot the target's distribution and its relationship with relevant inputs.
    # Under each chart, explain one pattern that matters for the business question.

elif page == "Model Predictions":
    st.title("Model Predictions")
    # Predict the same numeric target with at least five models. Suggested lineup:
    # linear regression, decision tree, random forest, a deep neural network
    # (MLPRegressor with multiple hidden layers), and a tabular foundation model (TabPFN).
    # Let users enter input values, choose a model, and see its prediction in the target's units.

elif page == "Feature Importance":
    st.title("Feature Importance")
    # Rank the inputs that drive the chosen model's predictions, e.g. with permutation importance.
    # Explain what the top features mean for the decision introduced on the first page.

elif page == "Hyperparameter Tuning":
    st.title("Hyperparameter Tuning")
    # Track each model's settings and validation scores in Weights & Biases (wandb).
    # Compare runs on the same validation data and explain why the best settings won.
    # Report the selected model's final error on the held-out test set.

elif page == "Conclusion":
    st.title("Conclusion")
    # Answer the original business question and recommend an action based on the results.
    # Explain one limitation that affects when someone should rely on the prediction.
