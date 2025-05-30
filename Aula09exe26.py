# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece
# a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece
# a última vez.

frase = str(input('Digite uma frase: ')).strip().lower()
#qtde_a = frase.count('a')
#primeira = frase.find('a') + 1
#segunda = frase.rfind('a') + 1
#print("O 'a' aparece {} na frase ".format(qtde_a))
#print("O 'a' aparece pe primeira vez na posição {} ".format(primeira))
#print("O 'a' aparece pela última vez na posição {} ".format(segunda))

print("O 'a' aparece {} na frase ".format(frase.count('a')))
print("O 'a' aparece pe primeira vez na posição {} ".format(frase.find('a')+1))
print("O 'a' aparece pela última vez na posição {} ".format(frase.rfind('a')+1))
