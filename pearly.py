# Create a DataFrame for actual target values
y_actual_df = pd.DataFrame(y_test, columns=['Actual_Target'])

# Reset index of X_test, y_pred_df, and y_actual_df before concatenating
X_test_reset = X_test.reset_index(drop=True)
y_pred_df_reset = y_pred_df.reset_index(drop=True)
y_actual_df_reset = y_actual_df.reset_index(drop=True)

# Concatenate the original dataset, predicted probabilities, and actual target values
result_df = pd.concat([X_test_reset, y_pred_df_reset, y_actual_df_reset], axis=1)

# Display the resulting DataFrame
print(result_df)