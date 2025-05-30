pessoas = {'nome': 'Jose', 'sexo': 'M', 'idade': 58}
#print(pessoas['nome'])
#print(pessoas['idade'])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#del pessoas['sexo']
#pessoas['nome'] = 'Ester'
#pessoas['peso'] = 58.5
#for k, v in pessoas.items():
    #print(f'{k} = {v}')

#Colocar dicuinário dentro de uma lista

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'Sao Paulo', 'sigla': 'RJ'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(estado1)
#print(brasil[0]['sigla'])
#print(f'{brasil[0]["sigla"]} é igual a {brasil[0]["uf"]}')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Digite a unidade federativa: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    #for k, v in e.items():
        #print(f'o campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end=" ")
    print()

#print(brasil)

