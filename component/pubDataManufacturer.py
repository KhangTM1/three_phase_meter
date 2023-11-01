import json
from component.readData import read_data

json_data = {
        "uid": "",
        "version": "1.0",
        "created_at": 1694164550,
        "header": {
            "source": {
                "service_name": "device",
                "id": ""
            },
            "destination": "broker",
            "requested_by": {
                "service_name": "device",
                "id": ""
            }
        },
        "data": {
            "action":"report_info",
            "version":{
                "firmware":"",
                "hardware":""
            },
            "model":{
                "manufacturer":"",
                "vendor":"",
                "model_name":"",
                "model_id":"",
                "model_code":"",
                "product_date":"",
                "first_use":"",
                "home_kit_code":"123-45-678",
                "bluetooth_code":123456,
                "region":""
            }
        }
    }

def pub_data_manufacturer(client, ID, vendor, current_time):
    topic_pub=f'{ID}/info'
    json_data['header']['source']['id'] = ID
    json_data['header']['requested_by']['id'] = ID
    current_data = read_data({'information':'http://192.168.30.9/api/v1/information'}, client)
    json_data['data']['version']['firmware'] = current_data['information']['fw']
    json_data['data']['version']['hardware'] = current_data['information']['hw']
    json_data['data']['model']['manufacturer'] = vendor
    json_data['data']['model']['vendor'] = vendor
    json_data['data']['model']['model_name'] = current_data['information']['metering_point']
    json_data['data']['model']['model_id'] = current_data['information']['uuid']
    json_data['data']['model']['model_code'] = current_data['information']['name']
    json_data['data']['model']['product_date'] = current_data['information']['production_date']
    json_data['data']['model']['first_use'] = current_time
    message = json.dumps(json_data)
    client.publish(topic_pub, message, qos=1, retain=True)
    print("Information")