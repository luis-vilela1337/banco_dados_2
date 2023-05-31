from neo4j import GraphDatabase
from database import Database
from teacher_crud import TeacherCRUD


database = Database("bolt://54.236.40.105:7687", "neo4j", "wars-properties-drop")

teacher_crud = TeacherCRUD(database)

teacher_crud.create('Chris Lima', 1956, '189.052.396-66')


teacher = teacher_crud.read('Chris Lima')
print(teacher)

teacher_crud.update('Chris Lima', '162.052.777-77')


cli = TeacherCLI(teacher_crud)
cli.run()
database.close()
