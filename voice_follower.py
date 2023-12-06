import websocket
import json
import queue

obs_websocket_address = "ws://192.168.1.12:4455"

def get_microphone_level(data):
    return data["d"]["eventData"]["inputs"][1]["inputLevelsMul"][0][0]

prev = queue.Queue(maxsize=2)
total = 0

def on_message(ws,message):
    global total
    data = json.loads(message)
    if data["op"] == 0:
        ws.send(json.dumps({
            "op": 1,
            "d":{
                "rpcVersion": 1,
                "eventSubscriptions": (1<<16)
            }
        }))
    elif data["op"] == 5 and data["d"]["eventType"] == "InputVolumeMeters":
        microphone_mul = get_microphone_level(data)
        if prev.full():
            total -=prev.get()
        total += microphone_mul
        prev.put(microphone_mul)

        avr = total / prev.qsize()
        if microphone_mul > 0.05:
            avr = 0.05
        else:
            avr=min(0.05,avr)
        ws.send(json.dumps({
            "op":6,
            "d":{
                "requestType":"SetInputVolume",
                "requestId":"1",
                "requestData":{
                    "inputName":"人声",
                    "inputVolumeMul": avr * 20
                }
            }
        }))

ws = websocket.WebSocketApp(f"{obs_websocket_address}", on_message=on_message)

ws.run_forever()