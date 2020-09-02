#Sintaxe de uma lista(array) em python
minhaLista = ["Guilherme", "Amanda","Francine", 22]
print(minhaLista)

#Acesso ao item por posição
print("acesso por posição: ",minhaLista[0])

#Acesso indexado negativo por posição (-1 é o ultimo item da lista)
print("acesso indexado negativo: ",minhaLista[-3])

#intervalo de itens
print("intervalo de itens: ",minhaLista[1:3])
print("intervalo de itens sem item de inicio: ",minhaLista[:3])
print("intervalo de itens sem item de final: " ,minhaLista[1:])

#intervalo de itens indexação negativo
print("intervalo de itens indexado negativo: ",minhaLista[-3:-1])
print("intervalo de itens indexado negativo sem item de final: ",minhaLista[:-1])
print("intervalo de itens indexado negativo sem item de inicio: ",minhaLista[-3:])

#alterando valor do item
minhaLista[3] = "Julia"
print("Lista com valor do item alterado: ",minhaLista)

#percorrer lista
for i in minhaLista:
    print("Item da lista: ",i)

#verificar se o item está na lista
if "Amanda" in minhaLista:
    print("Sim, está na lista!")
else:
    print("Não está!")

#Retorna quantidade de itens na lista
print("Quantidade de itens na lista: ", len(minhaLista))

#Adiciona item ao final da lista
minhaLista.append("Henrique")
print("Minha lista com novo item no final: ", minhaLista)

#Adiciona item na posição escolhida
minhaLista.insert(1,"Madu")
print("Minha lista com item adicionado em posição específica: ", minhaLista)

#Remover item especifico da lista
    