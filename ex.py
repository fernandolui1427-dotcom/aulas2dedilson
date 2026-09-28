lista = [10, 20, 30]
# adiciona um numero
lista.append(40)

print(lista)


lista = [10, 20, 30]
# insere um numero obs:no primeiro numero do parenteses vem a posição e dps o numero
lista.insert(1, 15)

print(lista)


lista = [10, 20, 30]
# remove determinado numero
lista.remove(20)

print(lista)


lista = [10, 20, 30]
# retorna um elementode u indice, o primeiro por padrão
lista.pop()

print(lista.pop())


lista = [10, 20, 30]
# conta quantas vezes o valor aparece  
x = lista.count(10)

print(x)


lista = [10, 20, 30]
# retorna o indice da primeira ocorrencia
lista.index(30)

print(lista.index(20))


lista = [10, 20, 40, 30]
#ordena a lista na ordem crescente
lista.sort()

print   (lista)



lista = [10, 20, 30]
# ordena a lista na ordem decrescente
lista.reverse()

# print(lista)



#lista de entregas com nomes repetidos
entregas = ["Ana", "joão", "Ana", "Pedro"]
# set() elimina a duplicatas
conjunto = set(entregas)
#imprime apenas os alunos unicos
print(conjunto)

