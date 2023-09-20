filtered_df = df[['Column1', 'Column2', 'Column3']][(df['ColumnA'] == 'value1') & (df['ColumnB'] == 'value2')]

# Display the filtered DataFrame
print(filtered_df)