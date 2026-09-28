# #lista original de valores
# lista = [10, 5, 20, 3, 42, 7]
# #filtragem com list comprehension
# maiores = [x for x in lista if x > 70]
# print(maiores)
# #mesta filtragem com filter()
# pares = list(filter (lambda x: x % 2 == 0, lista))
# print(pares) # [10, 20, 42]


# # lista fora de ordem 
# lista = [10, 3, 6, 60]
# # sort( ordena a propria lista)
# lista.sort()
# print(lista)    # [3, ,6 10, 60]
# # ordem decrscente
# lista.sort(reverse=True)
# print(lista)    # [60, 10, 6, 3]

# # sorted()  devolve uma nova lista
# nova = sorted(lista)



# # dois conjuntos de valores 
# A = {1, 2 ,3}
# B = {3, 4, 5}
# # união: tudo de A e de B
# print(A | B)  # {1, 2, 3, 4, 5}
# # intersecção: o que ha nos dois
# print(A & B)  # {3}
# # diferença: so o que e de A
# print(A - B)   # {1, 2} 



# # arquivo: adicionar:py
# def adicionar(estoque, produto):
#     # evita duplicidade no estoque
#     if produto not in estoque:
#         estoque.append(produto)  # insere
#     return estoque


# # teste rapido do modulo
# if __name__ == "__main__":
#     print(adicionar(["mouse"], "teclado"))



# # arquivo: remove.py
# def remover(estoque, produto):
#     #soremove se o item existir
#     if produto in estoque:
#         estoque.remove(produto)
#     else:
#         print("produto nao enconrado")
#     return estoque

# if __name__ == "__main__":
#     print(remover(["mouse", "hd"], "hd"))



# # arquivo: atualizar.py
# def atualizar(estoque, antigo, novo):
#     #localiza o indice do produto
#     if antigo in estoque:
#         i = estoque.index(antigo)
#         estoque[i] = novo # substitui
#     return estoque

# if __name__ == "__main__":
#     print(atualizar(["mose"], "mose", "mouse"))



# # arquivo: iterar.py
# def iterar(estoque):
#     # enumere da inice e valor
#     for I, produto in enumerate (estoque, start=1):
#         print(I, "-", produto)
#     print("total:", len(estoque))

# if __name__ == "__main__":
#     iterar(["mouse", "teclado"])



# # arquivo: pertencimento.py
# def existe(estoque, produto):
#     # o operador in devolve True/False
#     return produto in estoque

# if __name__ == "__main__":
#     lista = ["mouse", "teclado"]
#     if existe(lista, "mouse"):
#         print("ja cadastrado")
#     else:
#         print("pode comprar")



# arquivo: principal.py
from operador import adicionar
from operador import remover
from operador import atualizar
from operador import iterar
from operador import existe
estoque = ["mouse", "mose", "hd"]
adicionar (estoque, "teclado")
atualizar(estoque, "mose", "mouse2")
remover(estoque, "hd")
if existe (estoque, "teclado"):
    iterar(estoque)    #relatorio
