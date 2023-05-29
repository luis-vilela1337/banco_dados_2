from neo4j import GraphDatabase
from database import Database
from FamiliaDatabase import FamiliaDatabase

db=Database("bolt://54.89.76.27:7687" , "neo4j", "challenges-subtasks-beach")


familia=FamiliaDatabase(db)


engenheiros = familia.get_engenheiros()
print("Engenheiros da família:")
print(engenheiros)


filhasDeSebastiao = familia.get_filhas_de_sebastiao()
print("Filhas de Sebastião:")
print(filhasDeSebastiao)

cachorros = familia.get_cachorros()
print("Cachorros da Familia:")
print(cachorros)

db.close()