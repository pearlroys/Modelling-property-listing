bucket_size = 20

# Create an array of bucket edges
bucket_edges = np.arange(-100, 101, bucket_size)

# Calculate the average values for each bucket
average_values = [col_y[(col_x >= edge) & (col_x < edge + bucket_size)].mean() for edge in bucket_edges]

# Create the distribution plot
plt.bar(bucket_edges[:-1], average_values, width=bucket_size, align='edge')

# Set labels and title
plt.xlabel('X-axis Buckets')
plt.ylabel('Average Y-values')
plt.title('Distribution of Average Y-values in X-axis Buckets')

# Show the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
col_x = np.random.randint(-100, 100, size=100)
col_y = np.random.randint(-100, 100, size=100)

# Define the bucket size
bucket_size = 20

# Create an array of bucket centers
bucket_centers = np.arange(-100, 101, bucket_size) + bucket_size / 2

# Calculate the average values for each bucket
average_values = [col_y[(col_x >= edge - bucket_size / 2) & (col_x < edge + bucket_size / 2)].mean() for edge in bucket_centers]

# Create a line plot
plt.plot(col_x, average_values, marker='o', linestyle='-', label='Average Values')

# Set labels and title
plt.xlabel('X-values (col_x)')
plt.ylabel('Average Y-values')
plt.title('Line Plot of Average Y-values vs. X-values')

# Show the legend
plt.legend()

# Show the plot
plt.show()
