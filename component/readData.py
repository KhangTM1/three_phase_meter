import json
from component.callApi import call_api
from component.dataPreprocessing import data_preprocessing

def read_data(params, client):
    data = {}
    for key, api_url in params.items():
        data_current = json.dumps(call_api(api_url, client))
        if data_current is not None:
            preprocessed_data = {}
            if 'items' in json.loads(data_current):
                preprocessed_data = data_preprocessing(json.loads(data_current)['items'])
            else:
                preprocessed_data = data_preprocessing(json.loads(data_current))
            data[key] = preprocessed_data
        else:
            data[key] = ""
    return data
