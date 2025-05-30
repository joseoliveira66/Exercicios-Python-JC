# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço
# militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

from datetime import date

nasc = int(input('Em que ano você nasceu? '))
genero = int(input('''Digite o genero:
 [1] para masculino
 [2] para feminino
 :  '''))

idade_alistar = 18
ano_atual = date.today().year


# Depois colocar os anos corretos para alistamento, que faltam e que passaram.
# Usar elif pode ficar melhor compreensivo o código

if genero == 1:
    if (ano_atual - nasc) < idade_alistar:
        print('Você tem {} anos e Faltan {} anos para o seu alistamento!!.'.format((ano_atual - nasc), (idade_alistar - (ano_atual - nasc))))
    elif (ano_atual - nasc) == idade_alistar:
        print('Você tem {} anos e Chegou a hora do seu alistamento'.format(ano_atual - nasc))
    elif (ano_atual - nasc) > idade_alistar:
        print('Você passou {} anos do prazo para alistamento.'.format((ano_atual - nasc) - idade_alistar))
else:
    print('Você não tem obrigação de se alistar.')
