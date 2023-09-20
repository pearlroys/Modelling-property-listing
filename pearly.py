# Create separate columns for 'alcohol' and 'bmi' and fill them based on 'entry_value'
df['alcohol'] = df.apply(lambda row: row['entry_value'] if row['entry'] == 'alcohol' else None, axis=1)
df['bmi'] = df.apply(lambda row: row['entry_value'] if row['entry'] == 'bmi' else None, axis=1)

# Drop the 'entry' and 'entry_value' columns
df.drop(columns=['entry', 'entry_value'], inplace=True)