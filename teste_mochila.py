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
    
    # Definindo a Matriz com n linhas e W colunas
    # Preenchendo com zeros
    # Para acessar o elemento matriz[2][3] devemos subtrair 1
    # da linha e da coluna, Assim matriz[1][2].
    # pois o indice comeca com zero
    
    # Necessario add 1 a linha e a coluna para os zeros
    n = n + 1
    W = W + 1
    
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

    for j in range(1, n):
        for x in range(W):
            if w[j - 1] > x:
                matriz[j][x] = matriz[j - 1][x]
            else:
                usa = v[j - 1] + matriz[j - 1][x - w[j - 1]]
                nao_usa = matriz[j - 1][x]
                if usa > nao_usa:
                    matriz[j][x] = usa
                else:
                    matriz[j][x] = nao_usa
                    
    def quais_itens():
        s = []
        j = n - 1 #linha
        x = W - 1 #coluna
        #print("j = %d" % (j))
        #print("x = %d" % (x)) 
        while j >= 1:
            if matriz[j][x] == (matriz[j - 1][x - w[j - 1]] + v[j - 1]):
                s.append(j - 1)
                x = x - w[j - 1]
            j = j - 1
        return s
    print("Itens:")
    print(quais_itens())
    #print(matriz)
    print("Valor Maximo:")
    return matriz[n -1][W - 1]
         