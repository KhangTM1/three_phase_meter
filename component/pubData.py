import json
from component.readData import read_data

def pub_data(client, topic_pub, params, current_dir):
    with open(f'{current_dir}/data/dataSub.txt', 'r') as file:
        data_sub = json.load(file)
    current_data = read_data(params, client)
    data_sub['data']['action'] = "report_state"
    data_sub['data']['state'] = current_data
    message = json.dumps(data_sub)
    client.publish(topic_pub, message)
    print("Start new session")