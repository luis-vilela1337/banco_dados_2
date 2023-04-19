from database import Database
from writeAJson import writeAJson
from BookModel import BookModel
from cli import BookCLI

collection = Database(database="bancoiot", collection="sensores")

# Classe SensorThread
class SensorThread(threading.Thread):
    def __init__(self, nomeSensor, tempo, database):
        threading.Thread.__init__(self)
        self.nomeSensor = nomeSensor
        self.tempo = tempo
        self.sensorAlarmado = False
        self.db = database
        self.collection = self.db.collection_name

    def run(self):
        while True:
            # Gera temperatura aleatória
            temperatura = random.uniform(30, 40)

            # Atualiza o documento do sensor no MongoDB
            query = {"nomeSensor": self.nomeSensor}
            update = {"$set": {"valorSensor": temperatura}}
            self.collection.update_one(query, update)

            # Verifica se a temperatura está acima do limite
            if temperatura > 38:
                self.sensorAlarmado = True
                print("Atenção! Temperatura muito alta! Verificar Sensor", self.nomeSensor)

            # Atualiza o campo sensorAlarmado no documento do sensor
            query = {"nomeSensor": self.nomeSensor}
            update = {"$set": {"sensorAlarmado": self.sensorAlarmado}}
            self.collection.update_one(query, update)

            # Aguarda o tempo configurado
            time.sleep(self.tempo)

# Cria os threads dos sensores
tempo = 5 # tempo de espera em segundos
temp1 = SensorThread("Temp1", tempo, collection)
temp2 = SensorThread("Temp2", tempo, collection)
temp3 = SensorThread("Temp3", tempo, collection)

# Inicia os threads
temp1.start()
temp2.start()
temp3.start()
