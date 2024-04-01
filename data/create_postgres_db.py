
import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="dev", user="root", password="root", host="postgres", port= "5432"
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping measurement table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE FLOWTTT_DATA(
   DATETIME CHAR(20),
   ARTICLE CHAR(20) ,
   QUANTITE INT,
   PRIX_UNITAIRE FLOAT
)'''

cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#Closing the connection
conn.close()