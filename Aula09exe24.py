# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

#cidade = str(input('Digite um nome de uma cidade: ')).strip()
#cidade = cidade.upper()

#if cidade [ :5] == 'SANTO':
    #print("A cidade contém o nome 'SANTO' ")
#else:
    #print("A cidade não contém o nome 'SANTO'")

cid = str(input('Em que cidade você nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')