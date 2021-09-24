from kafka import KafkaConsumer
from processamento.Natural_Language import NLP

TOPIC_NAME = 'phrase'
KAFKA_SERVER = 'localhost:9091'

consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=KAFKA_SERVER)
for message in consumer:
    m: str = message.value
    m = m.decode()
    print(m)
    print(NLP(m).process['Mensagem'])