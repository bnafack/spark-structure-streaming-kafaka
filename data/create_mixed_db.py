import psycopg2

# Connection parameters
database = "dev"
user = "root"
password = "root"
host = "postgres"
port = "5432"

# connection setting
connection_string = f"dbname='{database}' user='{user}' password='{password}' host='{host}' port='{port}'"

# create a Table
create_table_sql = '''
CREATE TABLE MIXED_DATA_FLOW(
   DATETIME TIMESTAMP WITHOUT TIME ZONE,  
   MACHINE_NUM CHAR(20),
   PARAM1 FLOAT,
   PARAM2 FLOAT,
   PARAM3 FLOAT,
   PARAM4 FLOAT,
   PARAM5 FLOAT,
   PARAM6 FLOAT,
   PARAM7 FLOAT,
   PARAM8 FLOAT,
   PARAM9 FLOAT
)'''

try:
    # Setting up the connection
    with psycopg2.connect(connection_string) as conn:
        with conn.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS MIXED_DATA_FLOW")
            # Create a new table
            cursor.execute(create_table_sql)
            print("Table created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
    