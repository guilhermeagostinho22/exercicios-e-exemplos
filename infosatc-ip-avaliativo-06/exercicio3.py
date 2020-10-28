entrada = int(input("Digite um número: "))
lista = [1,2,3,4]

if entrada < 0: 
    lista[3] = lista[2]
    lista[2] = lista[1]
    lista[1] = lista[0]
    del lista[0]
    lista.insert(0,"4")
    print(lista) 
elif entrada > 0: 
    lista[0] = lista[1]
    lista[1] = lista[2]
    lista[2] = lista[3]
    del lista[3]
    lista.insert(3,"1")
    print(lista) 
else: 
    print(lista)   
     