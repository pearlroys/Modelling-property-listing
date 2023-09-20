# Define a custom aggregation function to select the first non-null value
def first_non_null(series):
    return next((val for val in series if not pd.isna(val)), None)

# Group by 'patient id' and aggregate columns using the custom function
result_df = filtered_df.groupby('patient id').agg({
    'company name': first_non_null,
    'age': first_non_null,
    'alcohol': first_non_null,
    'bmi': first_non_null
}).reset_index()

# Display the resulting DataFrame
print(result_df)