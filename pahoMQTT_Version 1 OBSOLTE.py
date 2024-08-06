import paho.mqtt.client as mqtt # type: ignore #import the client1
import time

############

#Creamos la función para ver el mensaje recibido en el subscriber
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

########################################

#Coloca IP del broker
broker_address="192.168.1.50"
#broker_address="iot.eclipse.org"

#Creamos la instancia del cliente
print("creating new instance")
client = mqtt.Client("P1") #create new instance - P1 es el nombre del cliente creado
client.on_message=on_message #attach function to callback - Esto es para ejecutar la función on_message creada al inicio

#Nos conectamos al broker
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop

#Nos suscribimos a un tópico
print("Subscribing to topic","house/bulbs/bulb1")
#client.subscribe("house/bulbs/bulb1")
client.subscribe("temperatura")

#Publicamos un mensaje
print("Publishing message to topic","house/bulbs/bulb1")
#client.publish("house/bulbs/bulb1","OFF")
client.publish("temperatura","150 C")

#Detenemos el proceso
time.sleep(4) # wait
client.loop_stop() #stop the loop
