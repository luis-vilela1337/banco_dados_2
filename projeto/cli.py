class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            print("Bem-vindo à CLI da Empresa!")
            print("Comandos disponíveis: criar_funcionario, ler_funcionario, atualizar_funcionario, excluir_funcionario, criar_departamento, ler_departamento, atualizar_departamento, excluir_departamento, quit")
            command = input("Digite um comando: ")
            if command == "quit":
                print("Até logo!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")

class EmpresaCLI(SimpleCLI):
    def __init__(self, funcionario_model, departamento_model):
        super().__init__()
        self.funcionario_model = funcionario_model
        self.departamento_model = departamento_model
        self.add_command("criar_funcionario", self.criar_funcionario)
        self.add_command("ler_funcionario", self.ler_funcionario)
        self.add_command("atualizar_funcionario", self.atualizar_funcionario)
        self.add_command("excluir_funcionario", self.excluir_funcionario)
        self.add_command("criar_departamento", self.criar_departamento)
        self.add_command("ler_departamento", self.ler_departamento)
        self.add_command("atualizar_departamento", self.atualizar_departamento)
        self.add_command("excluir_departamento", self.excluir_departamento)

    def criar_funcionario(self):
        nome = input("Digite o nome: ")
        cargo = input("Digite o cargo: ")
        salario = float(input("Digite o salário: "))
        self.funcionario_model.create_funcionario(nome, cargo, salario)

    def ler_funcionario(self):
        id = input("Digite o ID: ")
        funcionario = self.funcionario_model.read_funcionario_by_id(id)
        if funcionario:
            print(f"Nome: {funcionario['nome']}")
            print(f"Cargo: {funcionario['cargo']}")
            print(f"Salário: {funcionario['salario']}")

    def atualizar_funcionario(self):
        id = input("Digite o ID: ")
        nome = input("Digite o nome (deixe em branco para pular): ")
        cargo = input("Digite o cargo (deixe em branco para pular): ")
        salario = input("Digite o salário (deixe em branco para pular): ")
        self.funcionario_model.update_funcionario(id, nome, cargo, salario)

    def excluir_funcionario(self):
        id = input("Digite o ID: ")
        self.funcionario_model.delete_funcionario(id)

    def criar_departamento(self):
        nome = input("Digite o nome: ")
        localizacao = input("Digite a localização: ")
        a=str(input("Numero de funcionarios:-"))
        funcionario_ids=list(map(str, input("Funcionarios:-").strip().split()))
        self.departamento_model.create_departamento(nome, localizacao, funcionario_ids)

    def ler_departamento(self):
        id = input("Digite o ID: ")
        departamento = self.departamento_model.read_departamento_by_id(id)
        if departamento:
            print(f"Nome: {departamento['nome']}")
            print(f"Localização: {departamento['localizacao']}")
            print(f"Funcionários: {departamento['funcionarios']}")

    def atualizar_departamento(self):
        id = input("Digite o ID: ")
        nome = input("Digite o nome (deixe em branco para pular): ")
        localizacao = input("Digite a localização (deixe em branco para pular): ")
        a=str(input("Numero de funcionarios:-"))
        funcionario_ids=list(map(str, input("Funcionarios:-").strip().split()))
        self.departamento_model.update_departamento(id, nome, localizacao,funcionario_ids)

    def excluir_departamento(self):
        id = input("Digite o ID: ")
        self.departamento_model.delete_departamento(id)