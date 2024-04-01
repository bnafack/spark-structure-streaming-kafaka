import os
import logging
import findspark
findspark.init()
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka_2.11:1.6.3,org.apache.spark:spark-sql_2.13:3.5.1 pyspark-shell'
from ast import literal_eval
from pyspark.sql import SparkSession
import sys
from pyspark.sql.types import StructType,StructField,FloatType,IntegerType,StringType,TimestampType
from pyspark.sql.functions import from_json, col, date_format,to_timestamp
from pyspark.sql.functions import from_json,col
from pyspark.sql.functions import date_format



logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger = logging.getLogger("spark_structured_streaming")

import warnings
warnings.simplefilter("ignore")

# JDBC URL
jdbc_url = "jdbc:postgresql://postgres:5432/dev"#postgres"
# Connection properties
connection_properties = {
    "user": "root",
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
    StructField("DATETIME", StringType(), True),
    StructField("machines_ids", StringType(), True),
    StructField("param1", FloatType(), True),
    StructField("param2", FloatType(), True),
    StructField("param3", FloatType(), True),
    StructField("param4", FloatType(), True),
    StructField("param5", FloatType(), True),
    StructField("param6", FloatType(), True),
    StructField("param7", FloatType(), True),
    StructField("param8", FloatType(), True),
    StructField("param9", FloatType(), True)
])



## good##
# Convert value column to string and then apply schema to parse JSON
parsed_df  = df.selectExpr("CAST(value as STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")\
    .select(
        to_timestamp(col("DATETIME"), "dd/MM/yyyy HH:mm:ss").alias("DATETIME"),
        "machines_ids",
        "param1",
        "param2",
        "param3",
        "param4",
        "param5",
        "param6",
        "param7",
        "param8",
        "param9"
    )




# Write the parsed DataFrame to console for debugging
query = parsed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .trigger(processingTime="1 seconds") \
    .foreachBatch(lambda batch_df, batch_id: batch_df.write.jdbc(
        url=jdbc_url,
        table="DATA_FLOW",
        mode="append",
        properties=connection_properties
    )) \
    .start()

query.awaitTermination()
