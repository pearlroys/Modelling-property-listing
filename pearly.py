sample_idx = 0  # Choose the index of the observation you want to analyze
sample = X_test.iloc[sample_idx]

# Calculate SHAP values for the chosen observation
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(sample.values.reshape(1, -1))

# Create a DataFrame to display the SHAP values in a tabular format
shap_df = pd.DataFrame(data=shap_values[0], columns=X_test.columns)

# Display the DataFrame containing SHAP values for the chosen observation
print(shap_df)
