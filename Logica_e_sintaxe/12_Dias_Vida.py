dias = input('Quantos dias você quer converter? ')
try:
    dias = int(dias)
except:
    print('Insira somente os dias em números! ex: 765')
else:
    # Por considerarmos o mês com 30 dias, ocorriam erros na resposta no intervalo de dias de 360 a 364
    # O If evita que mostre por exemplo: 363 dias como 12 meses e 3 dias
    if 360 <= dias <= 364:
        anos = 0
        meses = 11
        dias_final = dias - 335
    else:
        anos = dias // 365  # Divisão por inteiro pois queremos saber somente quantos anos foram completados

        meses = (dias % 365) // 30  # A partir do resto deixado(dias que não chegam a completar um ano)
        #                               divide-se por inteiro para saber quantos meses foram completados

        dias_final = (dias % 365) % 30  # Mesmo raciocínio anterior, porém calcula-se o resto para saber quantos dias
        #                                 ficaram de fora do cálculo de meses

    print(f'{anos} ano(s)')
    print(f'{meses} mes(es)')
    print(f'{dias_final} dia(s)')
