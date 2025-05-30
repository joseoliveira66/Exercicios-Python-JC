# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# Algumas frases. Apos a sopa, a sacada da casa, o lobo ama o bolo

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # separa a palavra
junto = "".join(palavras) # junta palavras com o caracter digitado entre aspas
'''inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
inverso = junto[:: -1] # macete do fatiamento de strings
print('O inverso de {} é {}. '.format(junto, inverso))
if inverso == junto:
    print('Temos um PALINDROMO!')
else:
    print('Não temos um PALINDROMO!')