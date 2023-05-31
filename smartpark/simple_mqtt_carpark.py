"""Demonstrates a simple implementation of an 'event' listener that triggers 
a publication via mqtt"""
import paho.mqtt.client as paho
import json

class Carpark:
    def __init__(self, config):
        self.name = config['name']
        self.location = config['location']
        self.topic = config['topic']
        self.broker = config['broker']
        self.port = config['port']
        self.type = config['type']  # SPACES or FULL
        
        # initialise a paho client and bind it to the object Sensor (has-a)
        self.client = paho.Client()
        self.client.connect(self.broker,
                            self.port)

        # subscribe to the topic to listen to it in an instance
        client.subscribe(TOPIC)

    def on_detection(self, message):
        """The method that is triggered when a detection occurs
        - sends a message to MQTT and to all listener/subscriber"""
        message = f'{self.type}, {message}'
        self.client.publish(self.topic, message)

    def start_sensing(self):
        """a blocking event loop that waits for detection events, in this case Enter presses"""
        while True:
            input("Press Enter when 🚗 detected!")
            self.on_detection("Car detection took place")



if __name__ == '__main__':
    config = {'name': 'super sensor',
              'location': 'L306',
              'topic': "Vacancy",
              'broker': 'localhost',
              'port': 1883,
              'type': 'ENTRY'}

    sensor = Sensor(config)
    print("Sensor initialized")
    sensor.start_sensing()
