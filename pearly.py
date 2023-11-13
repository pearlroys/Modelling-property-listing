with open(output_file, 'w', newline='') as csv_file:
        fieldnames = ['description', 'sochigh', 'soclow']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data
        writer.writerows(result)

output_file = 'output.csv'
extract_keys_with_description_to_csv(data, output_file)