class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Digite um comando: ")
            if command == "quit":
                print("Até logo!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_model):
        super().__init__()
        self.teacher_model = teacher_model
        self.add_command("criar", self.create_teacher)
        self.add_command("ler", self.read_teacher)
        self.add_command("atualizar", self.update_teacher)
        self.add_command("excluir", self.delete_teacher)

    def create_teacher(self):
        name = input("Digite o nome: ")
        year_of_birth = int(input("Digite o ano de nascimento: "))
        cpf = input("Digite o CPF: ")
        self.teacher_model.create(name, year_of_birth, cpf)

    def read_teacher(self):
        name = input("Digite o nome: ")
        teacher = self.teacher_model.read(name)
        if teacher:
            print_teacher_details(teacher[0])

    def update_teacher(self):
        name = input("Digite o nome: ")
        new_cpf = input("Digite o novo CPF: ")
        self.teacher_model.update(name, new_cpf)

    def delete_teacher(self):
        name = input("Digite o nome: ")
        self.teacher_model.delete(name)

    def run(self):
        print("Bem-vindo à CLI de professores!")
        print("Comandos disponíveis: criar, ler, atualizar, excluir, quit")
        super().run()

def print_teacher_details(teacher):
    properties = teacher._properties
    year_of_birth = properties.get('year_of_birth')
    cpf = properties.get('cpf')
    name = properties.get('name')
    if year_of_birth:
        print(f"Ano de Nascimento: {year_of_birth}")
    if cpf:
        print(f"CPF: {cpf}")
    if name:
        print(f"Nome: {name}")
