import os
import sys
from component.active import run_once
from component.checkChangeData import start_checking_for_changes
import component.mqtt_connection as mqtt_connection
import threading

def main():
    args = sys.argv
    ID = 'ndc0odgzmza4_00205005000_18b27463ee6'
    vendor = 'Viettel'

    for i in range(1, len(args), 2):
        if args[i] == "--uID":
            ID = args[i+1]
        elif args[i] == "--vendor":
            vendor = args[i+1]
    pagrams = {
        'meters': 'http://192.168.30.9/api/v1/meters',
        'measurements': 'http://192.168.30.9/api/v1/measurements'
    }
    current_dir = os.path.dirname(os.path.abspath(__file__))
    client = mqtt_connection.connect(ID, pagrams, vendor, current_dir)
    run_once(client, ID, vendor, current_dir)
    client.publish(f'{ID}/heartbeat', 'Online', qos=1, retain=True)
    client.subscribe(f'{ID}/command')
    change_thread = threading.Thread(target=start_checking_for_changes, args=(client, f'{ID}/report', pagrams, current_dir))
    change_thread.start()
    client.loop_forever()

if __name__ == "__main__":
    main()


# python3 main.py --uID ndc0odgzmza4_00205005000_18b27463ee6 --vendor khangtm