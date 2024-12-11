import datetime
import os

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        # Tenta carregar os dados ou cria o arquivo vazio se não existir
        self.load()
    
    def load(self):
        # Se o arquivo não existir, cria um novo
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                pass  # Apenas cria um arquivo vazio
            self.users = {}  # Nenhum usuário no início
        else:
            self.file = open(self.filename, 'r')
            self.users = {}
            # Lê cada linha do arquivo e preenche o dicionário
            for line in self.file:
                email, password, name, created = line.strip().split(';')
                self.users[email] = (password, name, created)
            self.file.close()
    
    def get_user(self, email):
        # Retorna os dados do usuário ou None se não encontrado
        return self.users.get(email, None)
    
    def add_user(self, email, password, name):
        # Adiciona um novo usuário se o email não existir
        email = email.strip()
        if email not in self.users:
            self.users[email] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1  # Usuário adicionado com sucesso
        else:
            print('Email já existe')
            return -1  # Usuário já existe
    
    def validate(self, email, password):
        # Valida se o email e a senha correspondem
        user = self.get_user(email)
        if user:
            return user[0] == password
        return False
    
    def save(self):
        # Salva todos os usuários no arquivo
        with open(self.filename, 'w') as f:
            for email, (password, name, created) in self.users.items():
                f.write(f"{email};{password};{name};{created}\n")
    
    @staticmethod
    def get_date():
        # Retorna a data atual no formato yyyy-mm-dd
        return str(datetime.datetime.now()).split(" ")[0]


        