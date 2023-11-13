 if "contracts" in data and isinstance(data["contracts"], list):
        for dictionary in data["contracts"]:
            if isinstance(dictionary, dict):
                description = dictionary.get('description', '')

                # Check if 'edf' is in the description
                if 'edf' in description.lower():
                    parameters = dictionary.get('parameters', {})
                    keys_with_description = {
                        'description': description,
                        'sochigh': parameters.get('sochigh'),
                        'soclow': parameters.get('soclow')
                    }

                    result.append(keys_with_description)