from database import Database
from motoristaDAO import MotoristaDAO
from cli import MotoristaCLI

motoristaDAO = MotoristaDAO(database= Database(database="S202-L2", collection="Motoristas"))

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()