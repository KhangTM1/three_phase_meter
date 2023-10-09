import paho.mqtt.client as mqtt
from component.active import run_once
from component.pubData import pub_data

def connect(ID, pagrams, vendor):
    client = mqtt.Client(client_id=ID)
    certPath = f'./search/{ID}.cert'
    keyPath = f'./search/{ID}.key'

    
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print(f"Connection failed with code {rc}")   
            
    def on_message(client, userdata, message):
        data = message.payload.decode()
        with open("./data/dataSub.txt", "w") as file:
            file.write(data + "\n")

        
        pub_data(client, f'{ID}/report', pagrams)
        run_once(client, ID, vendor)
        
    client.tls_set(ca_certs='./search/ca.cert', 
                   certfile=certPath, 
                   keyfile=keyPath)
    client.will_set(topic=f'{ID}/heartbeat', payload="Offline", qos=1, retain=True)
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect("mqtt.filiot.com", 8884, 60)
    return client
