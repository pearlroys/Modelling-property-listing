# Create a violin plot using Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.violinplot(x="Advisor Team", y="NPS", data=df, palette="Set3")

# Add labels and title
plt.xlabel('Advisor Team Value')
plt.ylabel('NPS Category')
plt.title('NPS Categories by Advisor Team')

# Show the plot
plt.show()