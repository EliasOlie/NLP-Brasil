# -*- coding: utf-8 -*-

from kafka import KafkaProducer
import json

# message = json.dumps({"Mensagem":"Não gostei do pão"})

TOPIC_NAME = 'phrase'
KAFKA_SERVER = 'localhost:9091'

message = 'não gostei do pão'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER, value_serializer=lambda m: m.encode('utf-8'))
producer.send(TOPIC_NAME, message)

producer.flush()