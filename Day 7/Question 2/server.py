from flask import Flask,request
from executeQuery import executeQuery
from executeSelectQuery import executeSelectQuery
from datetime import datetime

server=Flask(__name__)

@server.get('/')
def homepage():
    return "Welcome.This is home page."

@server.post('/iot')
def create_data():
    id=request.form.get("sensor_id")
    humidity=request.form.get("humidity")

    query=f"insert into  iot_agriculture values({id},{humidity},'{datetime.now()}');"
    executeQuery(query=query)

    return "data is added successfully"

@server.put('/iot')
def update_data():
    id=request.form.get('sensor_id')
    humidity=request.form.get('humidity')
    query=f"update  iot_agriculture SET moisture_lvl={humidity} where id={id};"

    executeQuery(query=query)

    return "temp is updated successfully"

@server.get('/iot')
def get_data():
    query=f"select * from  iot_agriculture; "

    data=executeSelectQuery(query=query)
    
    return str(data)

@server.delete('/iot')
def delete_data():
    id=request.form.get('sensor_id')

    query=f"delete from  iot_agriculture where id={id};"

    executeQuery(query=query)

    return "data deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)

s