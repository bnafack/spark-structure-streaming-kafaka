from kafka import KafkaProducer
import json
from data import GetSellArticle
from daten import GetSensorDataSnapshot
from mixed_data import getSensorData
import time

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        registered_user = GetSensorDataSnapshot() # from API 
        print(registered_user)
        producer.send("registered_user", registered_user)
        time.sleep(1)
        producer.flush()
