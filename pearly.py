result_df = pd.DataFrame(columns=df.columns)

# Iterate through unique patient IDs
for patient_id in df['patient id'].unique():
    # Filter rows for the current patient ID
    patient_rows = df[df['patient id'] == patient_id]
    
    # Select the first non-null value for each column
    result_row = patient_rows.apply(lambda x: next((val for val in x if not pd.isna(val)), None))
    
    # Append the result row to the result DataFrame
    result_df = result_df.append(result_row, ignore_index=True)