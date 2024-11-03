import paho.mqtt.client as mqtt

# Configurações do broker
broker = "test.mosquito.org"
port = 1883
topic = "ramo/luzes"

# Callback para quando o cliente receber uma mensagem
def on_message(client, userdata, message):
    print(f"Recebida a mensagem '{message.payload.decode()}' no topico '{message.topic}'")

# Criação do cliente e definição do callback
client = mqtt.Client()
client.on_message = on_message

# Conexão com o broker e inscrição no tópico
client.connect(broker, port)
client.subscribe(topic)

# Inicia o loop para processar mensagens
client.loop_forever()
