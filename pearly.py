# Define the bucket size
bucket_size = 20

# Sort col_x in ascending order
sorted_indices = np.argsort(col_x)
sorted_x = col_x[sorted_indices]
sorted_y = col_y[sorted_indices]

# Initialize lists to store x-values and average values
x_values = []
average_values = []

# Calculate the average values for each bucket
for start in range(-100, 100, bucket_size):
    end = start + bucket_size
    mask = (sorted_x >= start) & (sorted_x < end)
    x_values.extend(sorted_x[mask])
    if np.any(mask):
        average_y = sorted_y[mask].mean()
        average_values.extend([average_y] * mask.sum())

# Create a scatter plot
plt.scatter(x_values, average_values, label='Average Values')
