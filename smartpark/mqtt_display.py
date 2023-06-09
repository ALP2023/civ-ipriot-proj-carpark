import mqtt_device
import time
from config_parser import parse_config
class Display(mqtt_device.MqttDevice):
    """Displays the number of cars and the temperature"""
    def __init__(self, config):
        super().__init__(config)
        self.client.on_message = self.on_message
        self.client.subscribe('display')
        self.client.loop_forever()

    def display(self, *args):
        print('*' * 20)
        for val in args:
            print(val)
            time.sleep(1)

        print('*' * 20)
    def on_message(self, client, userdata, msg):
       data = msg.payload.decode()
       self.display(*data.split(','))

       # TODO: Parse the message and extract free spaces,\
       #  temperature, time

if __name__ == '__main__':
    """config = {'name': 'display',
     'location': 'L306',
     'topic-root': "lot",
     'broker': 'localhost',
     'port': 1883,
     'topic-qualifier': 'na'
     }"""

    # The above is a dictionary
    # TODO: Read previous config from file instead of embedding if time
    config2 = parse_config()
    display = Display(config2)

