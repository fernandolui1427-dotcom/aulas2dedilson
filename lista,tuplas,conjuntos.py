#declaração de lista
lista = [10, 20, 30]
#acesso pelo indice (inicia em 0)
print(lista[0]) #imprime 10



#lista com os precos dos produtos
precos = [10.5, 5.0, 3.2,]
#soma todos os itens da lista
total = sum(precos)
#exibe o valor total da compra
print(f'total:{total}')



#declaração de tupla (parenteses)
ponto = (10, 20, 30)
#acesso pelo indice (inicia em 0)
print(ponto[0])
#imprime a tupla inteira
print(ponto)
#percorre  a tupla 
for valor in ponto:
    print(valor)

# tuplas com latitude e longitude (imutavel)
local = (12.45, -32.12)
#aceso pelos indices 0 e 1
print(f'latitude: {local[0]}, longiude: {local[1]}')

#declaração do conjunto (chaves)
frutas = {'maca', 'uva', 'maca'}
#duplicatas são eliminadas
print(frutas)   #('maca', 'uva')
#teste de pertinencia (acesso)
print("uva" in frutas)  #true
#percorrendo o conjunto 
for f in frutas:
    print(f)