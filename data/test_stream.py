import os
import logging
import findspark
findspark.init()
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka_2.11:1.6.3,org.apache.spark:spark-sql_2.13:3.5.1 pyspark-shell'
from ast import literal_eval
from pyspark.sql import SparkSession
import sys
from pyspark.sql.types import StructType,StructField,FloatType,IntegerType,StringType
from pyspark.sql.functions import from_json,col

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger = logging.getLogger("spark_structured_streaming")

import warnings
warnings.simplefilter("ignore")

# JDBC URL
jdbc_url = "jdbc:postgresql://postgres:5432/postgres"
# Connection properties
connection_properties = {
    "user": "postgres",
    "password": "root",
    "driver": "org.postgresql.Driver"
}


# spark = SparkSession \
#     .builder \
#     .getOrCreate()
    
try:

    spark = SparkSession \
                .builder \
                .appName("SparkStructuredStreaming") \
                .config("spark.jars.packages","org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0") \
                .config("spark.jars", "/opt/spark-apps/postgresql-42.2.22.jar") \
                .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    logging.info('Spark session created successfully')
except Exception:
    logging.error("Couldn't create the spark session")

# default for startingOffsets is "latest", but "earliest" allows rewind for missed alerts    
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka1:19092") \
  .option("subscribe", "registered_user") \
  .option("startingOffsets", "earliest") \
  .load()


"""
    Modifies the initial dataframe, and creates the final dataframe.
"""


schema = StructType([
            StructField("DateTime",StringType(),False),
            StructField("article",StringType(),False),
            StructField("quantite",StringType(),False),
            StructField("prix unitaire",StringType(),False)
        ])

# df = df.selectExpr("CAST(value AS STRING)").writeStream(from_json(col("value"),schema).alias("data"))
# df.printSchema()

# df = df.selectExpr("CAST(value AS STRING)")
# info_dataframe = df.select(
#         from_json(col("value"), schema).alias("sample")
#     )

# info_df_fin = info_dataframe.select("sample.*")

## good##
# Convert value column to string and then apply schema to parse JSON
parsed_df = df.selectExpr("CAST(value as STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")

# Write the parsed DataFrame to console for debugging
query = parsed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .trigger(processingTime="5 seconds") \
    .foreachBatch(lambda batch_df, batch_id: batch_df.write.jdbc(
        url=jdbc_url,
        table="FLOWTTT",
        mode="append",
        properties=connection_properties
    )) \
    .start()

query.awaitTermination()

# df.select("").writeStream.trigger(processingTime="10 seconds").start()
# df.show(truncate=False)
