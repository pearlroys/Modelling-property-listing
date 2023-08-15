# Pivot the DataFrame to have NPS categories as columns
pivot_df = pd.pivot_table(df, index='Days', columns='NPS', aggfunc=len, fill_value=0)

# Calculate cumulative values for each NPS category
cumulative_df = pivot_df.cumsum()

# Create a stacked line plot using Matplotlib
plt.figure(figsize=(12, 6))

# Plot stacked lines
plt.stackplot(cumulative_df.index, cumulative_df["Promoters"], cumulative_df["Detractors"], cumulative_df["Passives"], labels=["Promoters", "Detractors", "Passives"], alpha=0.7)

# Add labels and title
plt.xlabel('Days')
plt.ylabel('Cumulative Count')
plt.title('Stacked Line Plot of Cumulative NPS Categories')

# Add legend
plt.legend(loc='upper left')

# Show the plot
plt.show()
In this code, we pivot the DataFrame to have NPS categories as columns using pd.pivot_table. Then, we calculate the cumulative sum for each NPS category and create a stacked line plot using Matplotlib's stackplot.

Replace the sample data with your actual data before running the code. Adapt the code according to your specific data structure and requirements.





