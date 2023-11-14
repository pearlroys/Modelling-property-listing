import subprocess

# List of values to iterate over
locations = ['london', 'paris', 'newyork', 'tokyo', 'sydney', ...]  # Add more locations as needed

# Output file
output_file = 'output.txt'

# Loop over the list of locations
for location in locations:
    # Command to run
    command = f'contract-get --env production abc/{location}'

    # Run the command and capture the output
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)

    # Append the result to the output file
    with open(output_file, 'a') as file:
        file.write(f'Result for {location}:\n')
        file.write(result.stdout)
        file.write('\n' + '-' * 50 + '\n')

    # Print the result to the console
    print(f'Result for {location}:\n{result.stdout}\n' + '-' * 50)
