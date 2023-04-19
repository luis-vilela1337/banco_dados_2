import threading
import time
import random
from pymongo import MongoClient
from bson.objectid import ObjectId

def gerar_temperatura():
    return random.uniform(30, 40)

# função para verificar se um sensor está alarmado
def verificar_alarme(nome_sensor, valor_sensor, db):
    if valor_sensor > 38:
        db.sensores.update_one({"nomeSensor": nome_sensor}, {"$set": {"sensorAlarmado": True}})
        print(f"Atenção! Temperatura muito alta! Verificar Sensor {nome_sensor}!")
        return True
    else:
      db.sensores.update_one({"nomeSensor": nome_sensor}, {"$set": {"sensorAlarmado": False}})

    return False

# função para cada thread
def sensor(nome_sensor, tempo_atualizacao):
    # conexão com o banco de dados MongoDB
    client = MongoClient('mongodb://localhost:27018/')
    db = client.bancoiot
    # verifica se o documento do sensor já existe
    sensor = db.sensores.find_one({"nomeSensor": nome_sensor})
    if not sensor:
        # cria o documento do sensor no banco de dados
        sensor_id = db.sensores.insert_one({"nomeSensor": nome_sensor, "valorSensor": 0, "unidadeMedida": "C°", "sensorAlarmado": False}).inserted_id
    else:
        sensor_id = sensor['_id']
    while True:
        # gerando temperatura aleatória
        temperatura = gerar_temperatura()
        # atualizando o valor do sensor no banco de dados
        db.sensores.update_one({"_id": ObjectId(sensor_id)}, {"$set": {"valorSensor": temperatura}})
        # verificando se o sensor está alarmado
        if not verificar_alarme(nome_sensor, temperatura, db):
            print(f"Sensor {nome_sensor}: {temperatura} C°")
        time.sleep(tempo_atualizacao)

# criando as threads
t1 = threading.Thread(target=sensor, args=("Temp1", 2))
t2 = threading.Thread(target=sensor, args=("Temp2", 3))
t3 = threading.Thread(target=sensor, args=("Temp3", 4))

# iniciando as threads
t1.start()
t2.start()
t3.start()
