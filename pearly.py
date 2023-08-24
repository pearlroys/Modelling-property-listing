# Convert the probabilities array to a DataFrame
y_pred_df = pd.DataFrame(y_pred_probabilities, columns=['Prob_Promoters', 'Prob_Detractors', 'Prob_Passives'])

# Concatenate the original dataset with the predicted probabilities DataFrame
result_df = pd.concat([X_test, y_pred_df], axis=1)

# Display the resulting DataFrame
print(result_df)