import matplotlib.pyplot as plt
import numpy as np

# Assuming you have a DataFrame 'df' with columns 'average_predicted_nps' and 'actual_nps'
average_predicted_nps = df['average_predicted_nps']
actual_nps = df['actual_nps']

# Create an array of indices for each data point
indices = np.arange(len(df))

# Set the width of each bar
bar_width = 0.35

# Create a bar chart for actual NPS values
plt.bar(indices, actual_nps, bar_width, label='Actual NPS', color='green', alpha=0.7)

# Add a horizontal line for the average predicted NPS
plt.axhline(y=average_predicted_nps.iloc[0], color='blue', linestyle='--', label='Average Predicted NPS')

# Add labels, title, and legend
plt.xlabel('Data Point')
plt.ylabel('NPS')
plt.title('Comparison of Average Predicted NPS and Actual NPS')
plt.xticks(indices, indices)
plt.legend()

# Show the chart
plt.tight_layout()
plt.show()
