import paho.mqtt.client as mqtt
from component.pubData import pub_data
import threading


def send_message(client, ID, pagrams, current_dir):
    pub_data(client, f'{ID}/report', pagrams, current_dir)


def connect(ID, pagrams, vendor, current_dir):
    client = mqtt.Client(client_id=ID)
    certPath = f'{current_dir}/search/{ID}.cert'
    keyPath = f'{current_dir}/search/{ID}.key'
    certsPath = f'{current_dir}/search/ca.cert'
    
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print(f"Connection failed with code {rc}")   
            
    def on_message(client, userdata, message):
        has_run = False
        data = message.payload.decode()
        with open(f"{current_dir}/data/dataSub.txt", "w") as file:
            file.write(data + "\n")
        if not has_run:
            send_thread = threading.Thread(target=send_message, args=(client, ID, pagrams,current_dir))
            send_thread.start()
            has_run = True
        
    client.tls_set(ca_certs= certsPath, 
                   certfile=certPath, 
                   keyfile=keyPath)
    client.will_set(topic=f'{ID}/heartbeat', payload="Offline", qos=1, retain=True)
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect("mqtt.filiot.com", 8884, 60)
    return client
