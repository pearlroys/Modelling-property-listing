def extract_info(data):
    results = []

    if isinstance(data, dict):
        # Check if the dictionary contains the required keys
        description = data.get('description', None)
        soc_threshold_low = data.get('socthreshold low', None)
        soc_threshold_high = data.get('socthreshold high', None)

        if description is not None and soc_threshold_low is not None and soc_threshold_high is not None:
            results.append({
                'description': description,
                'socthreshold low': soc_threshold_low,
                'socthreshold high': soc_threshold_high
            })

        # Recursively call the function for nested dictionaries
        for value in data.values():
            results.extend(extract_info(value))

    return results


import json

with open('your_file.json', 'r') as file:
    json_data = json.load(file)

result = extract_info(json_data)
print(result)