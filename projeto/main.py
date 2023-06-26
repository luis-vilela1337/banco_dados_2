from database import Database
from funcionarioModel import FuncionarioModel
from departamentoModel import DepartamentoModel
from cli import EmpresaCLI

funcionarioModel = FuncionarioModel(database= Database(database="S202-L2", collection="funcionarios"))
departamentoModel = DepartamentoModel(database= Database(database="S202-L2", collection="departamento"))


empresaCLI = EmpresaCLI(funcionario_model = funcionarioModel, departamento_model= departamentoModel) 

empresaCLI.run()