#34-Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. 
#Para salarios superiores a R$1.250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%


salario = float(input('Digite seu salario:'))

if salario > 1250:
    print('Seu novo salario sera R${:.2f} com aumento de 10%'.format(salario +( salario * 10 / 100)))
else:
    print('Seu novo salario sera R${:.2f} com aumento de 15%'.format(salario + (salario * 15 / 100)))