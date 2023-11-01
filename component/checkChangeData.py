import json
import time
from component.readData import read_data


last_data_1 = None
last_data_2 = None

def check_for_changes(current_data):

    if last_data_1 is not None and last_data_2 is not None:
        if isinstance(current_data, dict) or current_data != {}:
            for key in current_data:
                current_values_list = list(current_data[key].values())
                last_values_1_list = list(last_data_1[key].values())
                last_values_2_list = list(last_data_2[key].values())

                for i in range(len(current_values_list)):
                    if (
                        isinstance(current_values_list[i], (int, float)) and
                        isinstance(last_values_1_list[i], (int, float)) and
                        isinstance(last_values_2_list[i], (int, float))
                    ):
                        if (
                            abs(current_values_list[i] - last_values_1_list[i]) >= 1 or
                            abs(current_values_list[i] - last_values_2_list[i]) >= 1
                        ):
                            print("Data has changed")
                            return True
                        else:
                            print("Data doesn't change")
                            return False
                    else:
                        print("Wrong data !!!")
                        return False
        else:
            return False
    else:
        return True


def start_checking_for_changes(client, topic_pub, params, current_dir):
    with open(f'{current_dir}/data/dataSub.txt', 'r') as file:
        data_sub = json.load(file)

    while True:
        current_data = read_data(params, client)

        if check_for_changes(current_data):
            data_sub['data']['action'] = "report_state"
            data_sub['data']['state'] = current_data
            message = json.dumps(data_sub)
            client.publish(topic_pub, message)

        global last_data_2, last_data_1
        last_data_2 = last_data_1
        last_data_1 = current_data

        time.sleep(5)