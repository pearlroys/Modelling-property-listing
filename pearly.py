for dictionary in data:
        keys_with_description = {
            'description': dictionary.get('description'),
            'sochigh': dictionary.get('sochigh'),
            'soclow': dictionary.get('soclow')
        }

        result.append(keys_with_description)

    return result