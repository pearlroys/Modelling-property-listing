row = 8
shap.waterfall_plot(shap.Explanation(values=shap_values[0][row], 
feature_names=X_test.columns.tolist()))