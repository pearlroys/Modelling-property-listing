# Create bins for months
bins = [0, 25, 50, 75, 100]  # You can adjust the bin ranges as needed

# Assign bins to months
df['Month Bins'] = pd.cut(df['Months'], bins=bins)

# Create a pivot table to count NPS categories for each bin
pivot_df = df.pivot_table(index='Month Bins', columns='NPS', aggfunc='size', fill_value=0)

# Create a bar plot using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
pivot_df.plot(kind='bar', stacked=True, color=sns.color_palette("Set3", n_colors=3))

# Add labels and title
plt.xlabel('Months')
plt.ylabel('Count')
plt.title('NPS Categories by Months')

# Show the plot
plt.show()