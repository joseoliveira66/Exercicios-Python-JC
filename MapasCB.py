def encontrar_posicao_final(mapa):
    """
    Encontra a posição final ('H') em um mapa 2D, começando de um ponto inicial ('o').

    Args:
        mapa: Uma lista de listas representando o mapa. '.' representa caminho vazio,
              'H' representa a posição de Hermione e 'o' representa o ponto inicial.

    Returns:
        Uma tupla (linha, coluna) representando a posição final de Hermione,
        ou None se não houver um ponto inicial ou se a posição final não for encontrada.
    """
    if not mapa:
        return None  # Mapa vazio

    linhas, colunas = len(mapa), len(mapa[0])
    inicio = None

    # Encontrar o ponto inicial ('o')
    for i in range(linhas):
        for j in range(colunas):
            if mapa[i][j] == 'o':
                inicio = (i, j)
                break
        if inicio:
            break

    if inicio is None:
        return None  # Retorna None se não houver ponto inicial

    # Explorar o mapa usando DFS (Depth-First Search - Busca em Profundidade)
    pilha = [inicio]  # Inicializa a pilha com o ponto inicial
    visitados = set([inicio])  # Conjunto para armazenar as posições já visitadas
    while pilha:
        i, j = pilha.pop()  # Remove o último elemento da pilha (LIFO)

        # Define os possíveis vizinhos (cima, baixo, esquerda, direita)
        vizinhos = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

        # Filtra os vizinhos válidos:
        # 1. Dentro dos limites do mapa
        # 2. Que sejam a posição de Hermione ('H')
        # 3. Que ainda não tenham sido visitados
        vizinhos_validos = [(x, y) for x, y in vizinhos if
                            0 <= x < linhas and 0 <= y < colunas and mapa[x][y] == 'H' and (x, y) not in visitados]

        # Se houver exatamente um vizinho válido, significa que encontramos a posição final
        if len(vizinhos_validos) == 1:
            return vizinhos_validos[0]

        # Adiciona os vizinhos válidos ao conjunto de visitados e à pilha para continuar a busca
        # Isso garante que não revisitemos o mesmo nó e evita loops infinitos.
        for vizinho in vizinhos_validos:
            visitados.add(vizinho)
            pilha.append(vizinho)

    return None  # Posição final não encontrada


# Exemplo de uso
mapa = [
    ['.', '.', '.', 'H', 'H', 'H', '.'],
    ['H', 'H', 'H', '.', '.', '.', 'H'],
    ['.', '.', '.', 'H', 'H', 'H', '.'],
    ['H', 'H', 'H', 'H', 'o', '.', 'H']
]

resultado = encontrar_posicao_final(mapa)
if resultado:
    print("Posição final de Hermione:", resultado)
else:
    print("Não foi possível encontrar a posição final.")