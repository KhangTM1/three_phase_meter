def data_preprocessing(data):
    output_data = {}
    for item in data:
        if 'id' in item and 'value' in item:
            output_data[item['id'].replace('-', '_')] = item['value']
        if 'name' in item and 'email' in item:
            output_data[item['name']] = item['email']
    
    return output_data
