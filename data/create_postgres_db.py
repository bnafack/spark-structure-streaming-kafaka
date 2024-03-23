
import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user="postgres", password="root", host="postgres", port= "5432"
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE FLOWTTT(
   ARTICLE CHAR(20) ,
   QUANTITE CHAR(20),
   "PRIX UNITAIRE" CHAR(20),
   DATETIME CHAR(20)
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#Closing the connection
conn.close()