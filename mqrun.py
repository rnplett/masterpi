from time import sleep
import paho.mqtt.subscribe as subscribe

def on_message_print(client, userdata, message):
    print("{} {}".format(message.topic, message.payload))

if __name__ == '__main__':
    subscribe.callback(on_message_print, "garage/brightness", hostname="masterpi.local")