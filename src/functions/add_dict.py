
# merge_dictionaries_1_2 function

def merge_dict(dict1, dict2):
    merged_dictionary_1_2 = {}

    for key in dict1:
        if key in dict2:
            new_value = dict1[key] + dict2[key]
        else:
            new_value = dict1[key]

        merged_dictionary_1_2[key] = new_value

    for key in dict2:
        if key not in merged_dictionary_1_2:
            merged_dictionary_1_2[key] = dict2[key]

    return merged_dictionary_1_2


# Testing the function

dict1 = {'key1': 1, 'key2': 2, 'key3': 3}
dict2 = {'key1': 10, 'key2': 20, 'key3': 30}

merge_dict(dict1, dict2)
