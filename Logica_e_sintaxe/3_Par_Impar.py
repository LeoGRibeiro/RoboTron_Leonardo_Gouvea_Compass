num1 = int(input('Insira o primeiro valor: '))
num2 = int(input('Insira o segundo valor: '))

result = num1 + num2

if result % 2 == 0:  # Caso o resto da divisão seja 0, o número é par
    print(f'A soma de {num1} + {num2} é igual a {result}, que é um numero Par!')
else:
    print(f'A soma de {num1} + {num2} é igual a {result}, que é um numero Ímpar!')
