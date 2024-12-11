import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label


# Classe para o banco de dados (DataBase) que cria o arquivo se não existir
class DataBase:
    def __init__(self, filename):
        self.filename = filename
        # Verifica se o arquivo existe, caso contrário cria um arquivo vazio
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write("")  # Cria um arquivo vazio
        self.load()

    def load(self):
        # Carregar dados do arquivo
        self.users = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    self.users.append(line.strip().split(','))
        except FileNotFoundError:
            pass

    def add_user(self, email, password, name):
        # Adiciona um novo usuário no arquivo
        with open(self.filename, 'a') as file:
            file.write(f"{email},{password},{name},2024-12-11\n")

    def validate(self, email, password):
        # Verifica se as credenciais do usuário são válidas
        for user in self.users:
            if user[0] == email and user[1] == password:
                return True
        return False

    def get_user(self, email):
        # Obtém os dados do usuário pelo e-mail
        for user in self.users:
            if user[0] == email:
                return user[1], user[2], user[3]  # Retorna senha, nome e data de criação
        return None, None, None


# Telas de CreateAccount, Login e Main
class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password.text != "":  # Corrigido para verificar a senha
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                sm.current = "login"
            else:
                self.invalidForm()
        else:
            self.invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def invalidForm(self):
        pop = Popup(title='Invalid Form',
                    content=Label(text='Please fill in all inputs with valid information.'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            self.invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

    def invalidLogin(self):
        pop = Popup(title='Invalid Login',
                    content=Label(text='Invalid username or password.'),
                    size_hint=(None, None), size=(400, 400))
        pop.open()


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created


class WindowManager(ScreenManager):
    pass


# Carregando o arquivo .kv
kv = Builder.load_file("my.kv")

# Instanciando o ScreenManager e o banco de dados
sm = WindowManager()
db = DataBase('users.txt')

# Adicionando as telas
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main")]

for screen in screens:
    sm.add_widget(screen)

# Definindo a tela inicial
sm.current = "login"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()

