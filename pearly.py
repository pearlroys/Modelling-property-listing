all_x_values = []
average_values = []

# Calculate the average values for each bucket and store all x-values
for edge in bucket_centers:
    x_in_bucket = col_x[(col_x >= edge - bucket_size / 2) & (col_x < edge + bucket_size / 2)]
    if len(x_in_bucket) > 0:
        average_y = col_y[(col_x >= edge - bucket_size / 2) & (col_x < edge + bucket_size / 2)].mean()
        all_x_values.extend(x_in_bucket)
        average_values.extend([average_y] * len(x_in_bucket))

# Create a scatter plot
plt.scatter(all_x_values, average_values, label='Average Values')