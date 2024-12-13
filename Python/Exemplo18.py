#Adicionando Eventos com o Kivy

# Importação das classes necessárias do Kivy para criar o aplicativo
from kivy.app import App  # Classe base para criar o aplicativo no Kivy
from kivy.uix.button import Button  # Classe para criar um botão na interface

# Definição da classe do aplicativo, que herda de 'App' do Kivy
class MainApp(App):
    
    # Método que cria e retorna a interface gráfica do aplicativo
    def build(self):
        # Criando o botão com texto 'Fala Galera'
        button = Button(text='Fala Galera', 
                        # Definindo o tamanho do botão como 50% da largura e altura da tela
                        size_hint=(.5, .5),  
                        # Definindo a posição do botão, centralizado na tela
                        pos_hint={'center_x': .5, 'center_y': .5})
        
        # Vinculando o evento 'on_press' do botão a uma função (método) que será chamada quando o botão for pressionado
        button.bind(on_press=self.on_press_button)
        
        # Retornando o botão para ser exibido no aplicativo
        return button

    # Definindo o método que será chamado quando o botão for pressionado
    def on_press_button(self, instance):
        # Quando o botão é pressionado, essa função imprime uma mensagem no console
        print('Voce apertou o Botão!')

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Cria uma instância do aplicativo MainApp
    app = MainApp()
    
    # Executa o aplicativo
    app.run()

