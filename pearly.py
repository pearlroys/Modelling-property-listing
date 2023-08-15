# Create a pivot table to count NPS categories for each Product
pivot_df = df.pivot_table(index='Product', columns='NPS', aggfunc='size', fill_value=0)

# Transpose the pivot table for stacked line plot
stacked_df = pivot_df.transpose()

# Create a stacked line plot using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
stacked_df.plot(kind='line', stacked=True, color=sns.color_palette("Set3", n_colors=3))

# Add labels and title
plt.xlabel('NPS Category')
plt.ylabel('Count')
plt.title('Stacked Line Plot of NPS Categories for Product ("prod_book")')

# Show the plot
plt.show()