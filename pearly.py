 Create a pivot table to count NPS categories for each Product
pivot_df = df.pivot_table(index='Product', columns='NPS', aggfunc='size', fill_value=0)

# Normalize the pivot table to get proportions
normalized_pivot_df = pivot_df.div(pivot_df.sum(axis=1), axis=0)

# Create a stacked line plot using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
normalized_pivot_df.plot(kind='line', stacked=True, color=sns.color_palette("Set3", n_colors=3))

# Add labels and title
plt.xlabel('Product')
plt.ylabel('Proportion')
plt.title('Stacked Line Plot of NPS Categories by Product ("prod_book")')

# Show the plot
plt.show()