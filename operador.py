# arquivo: adicionar:py
def adicionar(estoque, produto):
    # evita duplicidade no estoque
    if produto not in estoque:
        estoque.append(produto)  # insere
    return estoque


# teste rapido do modulo
if __name__ == "__main__":
    print(adicionar(["mouse"], "teclado"))



# arquivo: remove.py
def remover(estoque, produto):
    #soremove se o item existir
    if produto in estoque:
        estoque.remove(produto)
    else:
        print("produto nao enconrado")
    return estoque

if __name__ == "__main__":
    print(remover(["mouse", "hd"], "hd"))



# arquivo: atualizar.py
def atualizar(estoque, antigo, novo):
    #localiza o indice do produto
    if antigo in estoque:
        i = estoque.index(antigo)
        estoque[i] = novo # substitui
    return estoque

if __name__ == "__main__":
    print(atualizar(["mose"], "mose", "mouse"))



# arquivo: iterar.py
def iterar(estoque):
    # enumere da inice e valor
    for I, produto in enumerate (estoque, start=1):
        print(I, "-", produto)
    print("total:", len(estoque))

if __name__ == "__main__":
    iterar(["mouse", "teclado"])



# arquivo: pertencimento.py
def existe(estoque, produto):
    # o operador in devolve True/False
    return produto in estoque

if __name__ == "__main__":
    lista = ["mouse", "teclado"]
    if existe(lista, "mouse"):
        print("ja cadastrado")
    else:
        print("pode comprar")