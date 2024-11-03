import paho.mqtt.client as mqtt

# Configurações do broker
broker = "test.mosquitto.org"
port = 1883 # sem tls
topic = "ramo/luzes" # topico - lampadas do ramo

# Criação do cliente
client = mqtt.Client()

# Conexão com o broker
client.connect(broker, port)

# Publica uma mensagem no tópico
message = "ON"  # Exemplo de mensagem "comando" para as lampadas.
client.publish(topic, message)

#print(f"Mensagem '{message}' publicada no tópico '{topic}'.")

# Desconecta do broker
client.disconnect()
