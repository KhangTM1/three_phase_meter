from component.checkChangeData import start_checking_for_changes
import component.mqtt_connection as mqtt_connection
import threading
from component.readData import read_data

def main():
    ID = 'ndc0odgzmza4_00205005000_18a96fdea37'
    pagrams = {
        'meters': 'http://192.168.30.9/api/v1/meters',
        'measurements': 'http://192.168.30.9/api/v1/measurements'
    }
    client = mqtt_connection.connect(ID, pagrams, vendor='Viettel')
    client.publish(f'{ID}/heartbeat', 'Online', qos=1, retain=True)
    client.subscribe(f'{ID}/command')
    change_thread = threading.Thread(target=start_checking_for_changes, args=(client, f'{ID}/report', pagrams))
    change_thread.start()
    client.loop_forever()

if __name__ == "__main__":
    main()
