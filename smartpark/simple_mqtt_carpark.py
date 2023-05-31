"""Demonstrates a simple implementation of an 'event' listener that triggers 
a publication via mqtt"""
import paho.mqtt.client as paho
import mqtt_device
class Carpark(mqtt_device.MqttDevice):
    """Carpark object that is both a subscriber and publisher"""
    def __init__(self, config):
        super().__init__(config)
        self.total_spaces = config['total_spaces']
        self.total_cars = config['total_cars']
        self.client.on_message = self.on_message
        self.client.subscribe(self.topic)
        self.client.loop_forever()

    def available_spaces
    def on_car_entry(self):
        self.total_cars = 1
    def on_car_exit(self):
        self.total_cars -= 1

    def on_message(self, client, userdata, msg):
        print(f'Received {msg.payload.decode()}')




if __name__ == '__main__':
    config = {'name': 'Disaster-park',
              'total_spaces': 100,
              'total_cars': 0,
              'location': 'L306',
              'topic-root': "Space",
              'broker': 'localhost',
              'port': 1883,
              'topic-qualifier': 'ENTRY'}

    sensor = Carpark(config)
    print("Car park initialized")
    sensor.start_sensing()

