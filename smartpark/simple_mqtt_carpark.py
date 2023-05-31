import paho.mqtt.client as paho
import mqtt_device

class Carpark(mqtt_device.MqttDevice):
    """Creates a carpark object to store the state of cars in the lot"""

    def __init__(self, config):
        super().__init__(config)
        self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.subscribe('+/+/+/+')
        self.client.loop_forever()

    @property
    def available_spaces(self):
        available = self.total_spaces - self.total_cars
        return available if available > 0 else 0
    def on_car_entry(self):
        self.total_cars += 1
        # TODO: Publish to MQTT

    def on_car_exit(self):
        self.total_cars -= 1
        # TODO: Publish to MQTT

    def on_message(self, client, userdata, msg):
        # print(f'Received {msg.payload.decode()}')
        topic = msg.topic().strip().split('/')[-1]
        if topic == 'entry:':
            self.on_car_entry()
        else:
            self.on_car_exit()


if __name__ == '__main__':
    config = {'name': 'Disaster-park',
              'total_spaces': 100,
              'total_cars': 0,
              'location': 'L306',
              'topic-root': "space",
              'device_name': 'carpark',
              'topic-qualifier': 'entry',
              'broker': 'localhost',
              'port': 1883
              }

    carpark = Carpark(config)
    print("Car park initialised")

