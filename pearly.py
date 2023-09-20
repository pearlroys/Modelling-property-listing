# Pivot the DataFrame to merge rows based on 'entry'
df_pivoted = df.pivot(index=['age', 'company name'], columns='entry', values='entry_value')

# Reset the index
df_pivoted.reset_index(inplace=True)

# Rename the columns if needed
df_pivoted.columns.name = None