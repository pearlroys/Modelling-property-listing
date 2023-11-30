#!/bin/bash

# Run the first script and save the output to a file
./script1.sh > names1.txt

# Run the second script and save the output to a file
./script2.sh > names2.txt

# Use comm to find names unique to each list
unique_names_script1=$(comm -23 names1.txt names2.txt)
unique_names_script2=$(comm -13 names1.txt names2.txt)

# Print unique names for each script
echo "Unique Names in Script 1:"
echo "$unique_names_script1"

echo "Unique Names in Script 2:"
echo "$unique_names_script2"