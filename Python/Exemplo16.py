# Usando o Kivy com imagens

# Importando o módulo App da biblioteca Kivy, que é utilizado para criar o aplicativo.
from kivy.app import App

# Importando as classes Image e AsyncImage, que são usadas para exibir imagens na interface gráfica.
from kivy.uix.image import Image, AsyncImage

# Definindo a classe principal do aplicativo, que herda de App (classe base da Kivy para criação de apps).
class MainApp(App):
    # O método build é chamado automaticamente quando o aplicativo é iniciado.
    def build(self):
        # Criando um widget AsyncImage, que carrega imagens de forma assíncrona (não bloqueia a interface).
        img = AsyncImage(
            # Definindo a URL da imagem que será carregada.
            source='https://supermariorun.com/assets/img/stage/mario03.png',
            # A propriedade size_hint define a relação de tamanho do widget, aqui a altura será metade da altura da tela.
            size_hint=(1, .5),
            # A propriedade pos_hint define a posição do widget na tela. Aqui, ele será centralizado.
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        
        # O método build deve retornar o widget que será exibido na interface. Aqui estamos retornando a imagem.
        return img

# Verificando se o script está sendo executado diretamente (não importado como módulo).
if __name__ == '__main__':
    # Criando uma instância do aplicativo MainApp.
    app = MainApp()
    # Rodando o aplicativo.
    app.run()
