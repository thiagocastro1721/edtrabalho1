
'''
def adicionar_alfabeto(deque, alfabeto):
Esta função adiciona ao objeto deque, do tipo Deque,
cada caractere contido no parâmetro alfabeto (tipo string).
'''
def adicionar_alfabeto(deque, alfabeto):
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
    deque.Deque = []
    
    alfabeto = ""
    alfabeto = input()
    print(alfabeto)
    
adicionar_alfabeto(deque, alfabeto)
