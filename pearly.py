# Initialize lists to store x and average values
x_values = []
average_values = []

# Calculate the average values for each bucket and store corresponding x-values
for edge in bucket_centers:
    x_in_bucket = col_x[(col_x >= edge - bucket_size / 2) & (col_x < edge + bucket_size / 2)]
    if len(x_in_bucket) > 0:
        average_y = col_y[(col_x >= edge - bucket_size / 2) & (col_x < edge + bucket_size / 2)].mean()
        x_values.append(np.mean(x_in_bucket))
        average_values.append(average_y)
