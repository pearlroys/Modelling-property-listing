if "contracts" in data and isinstance(data["contracts"], list):
        for dictionary in data["contracts"]:
            if isinstance(dictionary, dict):
                keys_with_description = {
                    'description': dictionary.get('description'),
                    'sochigh': dictionary.get('sochigh'),
                    'soclow': dictionary.get('soclow')
                }

                result.append(keys_with_description)

    return result