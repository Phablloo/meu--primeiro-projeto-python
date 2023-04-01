print('Hello')

print('Digite um numero:')
numero1 = int(input())

print('Digite um operador:')
operador = input()


print('Digite o segundo:')
numero2 = int(input())

if operador == '+':
    resultado = numero1 + numero2
    print('resultado:', resultado)
elif operador == '-':
    resultado = numero1 - numero2
    print('resultado:', resultado)
elif operador == '*':
    resultado = numero1 * numero2
    print('resultado:', resultado)
elif operador == '/':
    resultado = numero1 / numero2
    print('resultado:', resultado)
else:
    print('Operador incorreto')




