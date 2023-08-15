df = pd.DataFrame(data)

# Create a scatter plot using Matplotlib
plt.figure(figsize=(12, 6))
plt.scatter(df["Days"], df["NPS"], alpha=0.5)

# Add labels and title
plt.xlabel('Days')
plt.ylabel('NPS Category')
plt.title('Number of Days vs. NPS Category')

# Show the plot
plt.show()