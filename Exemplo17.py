#Criando botoes e layout deiferentes com Kivy

# Importação da biblioteca 'random' para gerar escolhas aleatórias
import random

# Importação do Kivy, biblioteca de interface gráfica para Python
from kivy.app import App  # Para criar o aplicativo Kivy
from kivy.uix.button import Button  # Para criar botões
from kivy.uix.boxlayout import BoxLayout  # Para criar o layout onde os botões serão colocados

# Definindo as cores utilizando listas de valores RGBA (vermelho, verde, azul e alfa/transparência)
red = [1, 0, 0, 1]      # Cor vermelha
green = [0, 1, 0, 1]    # Cor verde
blue = [0, 0, 1, 1]     # Cor azul
purple = [1, 0, 1, 1]   # Cor roxa

# Definindo a classe do aplicativo, que herda de 'App' do Kivy
class HBoxLayoutExample(App):
    
    # Método que constrói e retorna a interface gráfica
    def build(self):
        # Criando o layout com BoxLayout e definindo o padding (espaçamento interno)
        layout = BoxLayout(padding=10, spacing=10)
        
        # Criando uma lista com as cores predefinidas
        colors = [red, green, blue, purple]
        
        # Loop que cria 5 botões e os adiciona ao layout
        for i in range(5):
            # Criando um botão com um texto que indica seu número
            btn = Button(text=f'Este é o Botão #{i+1}',
                         # A cor de fundo do botão é escolhida aleatoriamente da lista de cores
                         background_color=random.choice(colors)
            )
            
            # Adicionando o botão ao layout
            layout.add_widget(btn)
        
        # Retornando o layout com todos os botões
        return layout
    
# Verifica se o arquivo está sendo executado diretamente
if __name__ == '__main__':
    # Cria uma instância da classe HBoxLayoutExample
    app = HBoxLayoutExample()
    
    # Executa o aplicativo
    app.run()

