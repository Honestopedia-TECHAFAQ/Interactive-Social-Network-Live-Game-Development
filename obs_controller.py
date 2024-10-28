from obswebsocket import obsws, requests

class OBSController:
    def __init__(self, host="localhost", port=4444, password="password"):
        self.ws = obsws(host, port, password)
        self.connected = False

    def connect(self):
        try:
            self.ws.connect()
            self.connected = True
            print("Connected to OBS")
        except Exception as e:
            print(f"Failed to connect to OBS: {e}")

    def disconnect(self):
        if self.connected:
            self.ws.disconnect()
            self.connected = False
            print("Disconnected from OBS")

    def change_scene(self, scene_name):
        if self.connected:
            self.ws.call(requests.SetCurrentScene(scene_name))

    def show_gift_animation(self, user_name):
        if self.connected:
            print(f"Showing gift animation for {user_name}")
