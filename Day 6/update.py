# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_agriculture",
    use_pure = True
)

# form a query to be executed
id = int(input("Enter sensor id whose moisture_lvl to be updated : "))
moisture_lvl = int(input("Enter new moisture_lvl : "))

query = f"update iot_agriculture SET moisture_lvl = {moisture_lvl} where id = {id};"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()

