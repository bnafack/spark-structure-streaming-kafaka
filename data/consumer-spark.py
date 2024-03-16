
import findspark
findspark.init() 
from kafka import KafkaConsumer
import json
import os
#from database import PopulateDataBase
from pyspark.sql import SparkSession
# Create SparkSession 
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate() 



if __name__ == "__main__":
    consumer = KafkaConsumer(
        "registered_user",
        bootstrap_servers=['kafka1:19092'],
        auto_offset_reset='earliest',
        group_id="consumer-group-a",
        value_deserializer=json.loads)
    print("starting the consumer")
    compt = 0
    data = []
    for msg in consumer:
      print("Registered User = {}".format(msg.value))
      data += [(msg.value['DateTime'],msg.value['article'], msg.value['quantite'],msg.value['prix unitaire'])]
      compt += 1

      if compt == 10 : 
        compt = 0
        # PopulateDataBase(msg.value, name_database='vente')
        columns = ["Datetime","article","quantite","prix unitaire"]

        df = spark.createDataFrame(data=data, schema = columns)
        df.show()
        # df.printSchema()
        data = []
      









