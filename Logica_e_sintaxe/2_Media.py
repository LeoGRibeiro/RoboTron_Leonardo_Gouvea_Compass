nota1 = float(input('Insira a primeira nota para calcularmos a média: '))
nota2 = float(input('Insira a segunda nota para calcularmos a média: '))

media = (nota1 + nota2) / 2

print(f'Sua nota média entre {nota1} e {nota2} foi: {media:.1f}')  # ":.1f" para mostrar apenas uma casa decimal
