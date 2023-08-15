# Create a pivot table to count NPS categories for each Advisor Team value
pivot_df = df.pivot_table(index='Advisor Team', columns='NPS', aggfunc='size', fill_value=0)

# Create a bar plot using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
pivot_df.plot(kind='bar', stacked=True, color=sns.color_palette("Set3", n_colors=3))

# Add labels and title
plt.xlabel('Advisor Team Value')
plt.ylabel('Count')
plt.title('NPS Categories by Advisor Team')

# Show the plot
plt.show()