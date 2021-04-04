class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque
    
    def indice(self, indice):
        return self.__items[indice]
    
deque = Deque()
alfabeto = ""
texto_cifrado = ""
texto_decifrado = ""
lista_decifrada = []

'''
def adicionar_alfabeto(deque, alfabeto):
Esta função adiciona ao objeto deque, do tipo Deque,
cada caractere contido no parâmetro alfabeto (tipo string).
'''
def adicionar_alfabeto(deque, alfabeto):
    #for para preencher a deque com a string alfabeto
    for i in range(len(alfabeto)):
        deque.add_front(alfabeto[i])
    #depois que esta funcao eh executada a string alfabeto fica vazia
    
    #print(alfabeto)
    #print(deque)
    #print(deque[0]) não deu certo

def decifrar(deque, texto_cifrado, chave):
    for i in range(len(texto_cifrado)):
        for j in range(deque.size()):
            if texto_cifrado[i] == deque.indice(j):
                indice_novo = j - chave
                #print("indice i = %d" % (i))
                #print("letra do texto cifrado no incice i %d = %s" % (i, texto_cifrado[i]))
                #print("indice j = %d" % (j))
                #print("elemento da deque no indice %d = %s" % (j, deque.indice(j)))
                #print("novo_indice = %d" % (indice_novo))
                #print(lista_decifrada)
                lista_decifrada.append(deque.indice(indice_novo))
                #texto_decifrado.replace(texto_decifrado[], deque.indice(indice_novo))
    texto_cifrado = ''.join(map(str, lista_decifrada))#unir elementos de uma lista e transforma-la em uma string
    lista_decifrada.clear()#limpado a lista
    return texto_cifrado
    
    
    
    #embaralhar de acordo com a chave
    #for i in range(chave):#nao eh possivel fazer pois alfabeto esta vazio
    #    deque.remove_rear()
    #    deque.add_front(deque.indice(i))
#alfabeto = deque
#p#int(deque)
def selecionar_subconjunto_missoes():#todo o resto da implimentação deve estar dentro desta funcao
    lista_de_strings = []
    horas_disponiveis = int(input())
    apresentar_missoes_s = int(input())#1 para sim e 0 para não
    indice_da_coluna = int(input())
    alfabeto = input()
    chave = int(input())
    missoes_cifradas = int(input())
    
    adicionar_alfabeto(deque, alfabeto)
    #Capturar N strings
    for i in range(missoes_cifradas):
        string_aux = ""
        string_colchetes = "[]"
        string_aux = input()
            
        #for para remover os colchetes na primeira e ultima posição
        for i in range(0,len(string_colchetes)):
            string_aux = string_aux.replace(string_colchetes[i],"")
            #print("String_aux = %s" % (string_aux))
        lista_de_strings.append(string_aux)
    
    #decifrar N strings
    for i in range(missoes_cifradas - 1, -1, -1):
        #print("Numero de for's = %d" % (i))
        texto_cifrado = lista_de_strings[i]
        #print("Texto cifrado = %s" % (texto_cifrado))
        print(decifrar(deque, texto_cifrado, chave))
    #print(lista_de_strings)

def mochila(n, v, w, W):
    usa = 0
    nao_usa = 0
    n = n + 1
    W = W + 1
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
    print(matriz)
    return matriz[n -1][W - 1]
         