import paho.mqtt.client as mqtt
import time

# Configurações do broker MQTT e tópicos
broker = "localhost"  # IP do BROKER
port = 1883
id_robo = "1"  # Identificação do robô
topic_controle = f"robos/futebol/controle/{id_robo}"
topic_status = f"robos/futebol/status/{id_robo}"

# Inicializando variáveis de estado
velocidade = 0
direcao = 0

# Função para processar comandos recebidos
def processar_comando(mensagem):
    global velocidade, direcao
    comando = mensagem.split(",")  # Exemplo: "velocidade,10"
    if comando[0] == "velocidade":
        velocidade = int(comando[1])
    elif comando[0] == "direcao":
        direcao = int(comando[1])

# Callback para conexão
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker MQTT.")
    client.subscribe(topic_controle)

# Callback para mensagens recebidas
def on_message(client, userdata, msg):
    mensagem = msg.payload.decode()
    print(f"Comando recebido: {mensagem}")
    processar_comando(mensagem)

# Criação do cliente e configuração dos callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conecta-se ao broker
client.connect(broker, port)

# Loop principal para enviar status periodicamente
def enviar_status():
    global velocidade, direcao
    status = f"posicao,x:{10},y:{20},velocidade:{velocidade},direcao:{direcao}"
    client.publish(topic_status, status)
    print(f"Status enviado: {status}")

# Loop para manter conexão e enviar status
client.loop_start()
while True:
    enviar_status()
    time.sleep(1)  # Envia status a cada segundo
