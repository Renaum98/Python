# fazendo Inserts nas Variaveis
import datetime  # Importa o módulo datetime

nome = input('Digite seu Nome:')  # O input serve para que o usuário insira o dado 
idade = int(input('Digite o ano em que você nasceu:'))  # Ano de nascimento
sexo = input('Digite seu Sexo:')  # Recebe o sexo do usuário

# Obtém o ano atual com 4 dígitos
data_atual = datetime.datetime.today()
ano_atual = data_atual.year  # Extrai o ano atual com 4 dígitos

# Calcula a idade subtraindo o ano de nascimento do ano atual
resultado = ano_atual - idade

print('Seja Bem Vindo', nome,'sua idade é', resultado, 'e você é do sexo', sexo)

