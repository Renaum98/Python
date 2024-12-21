#Criando uma calculadora



from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ['/','*','+','-']
        self.last_was_operator = None
        self.last_button = None
        
        # TextInput para mostrar a expressão e o resultado
        self.solution = TextInput(
            multiline=False, readonly=True, halign='right', font_size=55
        )
        
        # Layout principal
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.solution)  # Adicionando o TextInput ao layout
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
        ]
        
        # Criando os botões
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={'center_x': 0.5, 'center_y': 0.5}
                )
                button.bind(on_press=self.on_button_press)  # Corrigindo o bind
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        # Botão de "=" para calcular o resultado
        equals_button = Button(
            text='=', pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        equals_button.bind(on_press=self.on_solution)  # Corrigindo a chamada para on_solution
        
        main_layout.add_widget(equals_button)  # Adicionando o botão de "=" ao layout
        
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text  # Texto atual do TextInput
        button_text = instance.text  # Texto do botão pressionado
        
        if button_text == 'C':
            self.solution.text = ""  # Limpar a tela
        else:
            # Verificar se o texto atual e o botão pressionado são válidos
            if current and (self.last_was_operator and button_text in self.operators):
                return  # Não permite inserir dois operadores consecutivos
            elif current == "" and button_text in self.operators:
                return  # Não permite começar com um operador
            else:
                new_text = current + button_text
                self.solution.text = new_text  # Atualizar o texto do TextInput
        
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators  # Atualiza se o último botão pressionado foi um operador

    def on_solution(self, instance):
        text = self.solution.text  # Pega o texto atual do TextInput
        if text:  # Se houver algum texto
            try:
                # Avaliar a expressão matemática e exibir o resultado
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception as e:
                self.solution.text = "Erro"  # Exibir erro caso a expressão não seja válida
        else:
            self.solution.text = ""  # Se não houver texto, limpar o campo
            

if __name__ == '__main__':
    app = MainApp()
    app.run()


