import requests
import datetime
import json

def call_api(api_url, client):
    has_error = False
    json_data = {
        "uid": "",
        "version": "1.0",
        "created_at": 1694164550,
        "header": {
            "source": {
                "service_name": "device",
                "id": "ndc0odgzmza4_00205005000_18a96fdea37"
            },
            "destination": "broker",
            "requested_by": {
                "service_name": "app",
                "id": "ee5a5ce0-6335-4b5f-9653-d02485f0dfa0"
            }
        },
        "data": {}
    }
    try:
        response = requests.get(api_url, timeout=30)
        error_state = has_error
        if has_error:
            has_error = False
            
            if has_error != error_state:
                json_data["data"] = {
                    "action": "report_event",
                    "event": {
                        "code": "ndc0odgzmza4_CONNECTED",
                        "values": [datetime.datetime.now().isoformat()]
                    }
                }
                
                message = json.dumps(json_data)
                client.publish('ndc0odgzmza4_00205005000_18a96fdea37/event', message)
        
        return response.json()
    except requests.exceptions.RequestException as e:
        if not has_error:
            has_error = True
            
            json_data["data"] = {
                "action": "report_event",
                "event": {
                    "code": "ndc0odgzmza4_ERROR",
                    "values": [datetime.datetime.now().isoformat()]
                }
            }
            
            message = json.dumps(json_data)
            client.publish('ndc0odgzmza4_00205005000_18a96fdea37/event', message)
