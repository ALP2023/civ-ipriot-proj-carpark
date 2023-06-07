from datetime import datetime

import mqtt_device
import paho.mqtt.client as paho
from paho.mqtt.client import MQTTMessage
import json
from config_parser import parse_config


class CarPark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        self._temperature = None
        self.client.loop_forever()


    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return max(available, 0)

    @property
    def temperature(self):
        self._temperature
    
    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        
    def _publish_event(self):
        readable_time = datetime.now().strftime('%H:%M')
        print(
            (
                f"TIME: {readable_time}, "
                + f"SPACES: {self.available_spaces}, "
                + "TEMPC: 42"
            )
        )
        message = (
            f"TIME: {readable_time}, "
            + f"SPACES: {self.available_spaces}, "
            + "TEMPC: 42"
        )
        self.client.publish('display', message)

    def on_car_entry(self):
        self.total_cars += 1
        self._publish_event()

    def on_car_exit(self):
        self.total_cars -= 1
        self._publish_event()

    '''def on_message(self, client, userdata, msg):
        # print(f'Received {msg.payload.decode()}')
        topic = msg.topic().strip().split('/')[-1]
        if topic == 'entry:':
            self.on_car_entry()
        else:
            self.on_car_exit()'''

    def on_message(self, client, userdata, msg: MQTTMessage):
        payload = msg.payload.decode()


        # TODO: Extract temperature from payload
        """self.temperature = float(temperature_str) # Extracted value"""

        if 'exit' in payload:
            self.on_car_exit()
        else:
            self.on_car_entry()



if __name__ == '__main__':
    """config = {'name': 'Disaster-park',
              'total_spaces': 100,
              'total_cars': 0,
              'location': 'L306',
              'topic-root': "space",
              'device_name': 'carpark',
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'entry',
              'is_stuff': False
              }"""
    # TODO: Read config from file
    config = parse_config()
    car_park = CarPark(config)
    print("Carpark initialised")


