# ler dois número reais e exibir: soma, adiçãom subtração e multiplicação

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

def calcular (n1, n2, operação):
    resultado = 0
    if (operação == '+'):
        resultado = n1 + n2
        print(f'A soma é: {resultado:.2f}')
    elif(operação == '-'):
        resultado = n1 - n2
        print(f'A subtração é: {resultado:.2f}')
    elif(operação == '*'):
        resultado = n1 * n2
        print(f'A multipicação é: {resultado:.2f}')
    elif(operação == '/'):
        resultado = n1 / n2
        print(f'O divisão é: {resultado:.2f}')

operadores = ['+', '-', '*', '/']

for i in range(len(operadores)):
    calcular(n1, n2, operadores[i])
