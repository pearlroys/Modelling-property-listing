# Create a pivot table to count NPS categories for each Gender
pivot_df = df.pivot_table(index='Gender', columns='NPS', aggfunc='size', fill_value=0)

# Create a bar plot using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
pivot_df.plot(kind='bar', stacked=True, color=sns.color_palette("Set3", n_colors=3))

# Add labels and title
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('NPS Categories by Gender')

# Show the plot
plt.show()