def par(num):
    result = 1
    while num != 1:
        result *= num  # Inicialmente multiplica-se por 1, e após isso multiplica-se com um número subtraído
        print(num, end=' x ')  # Para printar cada número do fatorial e o sinal de vezes
        num -= 1  # Para subtrair 1 no valor que será usado pra próxima multiplicação
    print('1 =', end=' ')
    return result  # Retornar o valor final do fatorial


def impar(num):
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')


while True:
    num = input('Insira um número inteiro: ')
    try:
        num = int(num)
    except:
        print('Insira somente números inteiros!')
    else:
        if num % 2 == 0:
            print(f'Para número par: Fatorial de {num}')
            result_par = par(num)
            print(result_par)
        else:
            print(f'Para número ímpar: Tabuada do {num}')
            impar(num)
        break
