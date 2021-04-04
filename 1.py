def mochila(n, v, w, W):
    usa = 0
    nao_usa = 0
    # W capacidade da mochila
    # j linhas
    # x colunas
    # n quantidade de itens
    # w lista com os pesos dos itens
    # v lista com os valores dos itens
    # M matriz
    
    # Definiindo a Matriz com n linhas e W colunas
    # Preenchendo com zeros
    # Para acessar o elemento matriz[2][3] devemos subtrair 1
    # da linha e da coluna, Assim matriz[1][2].
    # pois o indice comeca com zero
    matriz = []
    for i in range(n):
        matriz.append([0]*W)
    #print(matriz)
   
    # Sequencia de 2 for's para zerar a primeira linha
    # e a primeira coluna
    for x in range(W):
        matriz[0][x] = 0
    for j in range(n):
        matriz[j][0] = 0
    #print(matriz)
        

    for j in range(1, n + 1):
        for x in range(W):
            if w[j - 1] > x:
                matriz[j - 1][x - 1] = matriz[j - 2][x - 1]
            else:
                usa = v[j - 1] + matriz[j - 2][x - w[j - 1]]
                nao_usa = matriz[j - 2][x - 1]
                if usa > nao_usa:
                    matriz[j - 1][x -1] = usa
                else:
                    matriz[j - 1][x - 1] = nao_usa
    print(matriz)
    return matriz[n -1][W - 1]