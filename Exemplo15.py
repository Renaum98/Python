#usando o Kivy

from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        # Criando o rótulo (label)
        label = Label(text='Fala galera!',
                      size_hint=(0.5, 0.5),  # Tamanho relativo
                      pos_hint={'center_x': 0.5, 'center_y': 0.5})  # Posição centralizada
        return label

if __name__ == '__main__':
    app = MainApp()  # Criando uma instância do aplicativo
    app.run()  # Iniciando o aplicativo