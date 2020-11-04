n1 = int(input("digite um número: "))
n2 = int(input("digite mais um número: "))
n3 = int(input("digite mais um número: "))
n4 = int(input("digite mais um número: "))
n5 = int(input("digite mais um número: "))
lista = [n1,n2,n3,n4,n5]
numero=filter(lambda x: '>10' in x, [lista])
print(list(numero))
