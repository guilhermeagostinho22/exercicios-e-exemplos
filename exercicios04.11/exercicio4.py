n1 = int(input("digite um número: "))
n2 = int(input("digite mais um número: "))
n3 = int(input("digite mais um número: "))
n4 = int(input("digite mais um número: "))
n5 = int(input("digite mais um número: "))
n6 = int(input("digite mais um número: "))
n7 = int(input("digite mais um número: "))
n8 = int(input("digite mais um número: "))
n9 = int(input("digite mais um número: "))
n10 = int(input("digite mais um número: "))
lista = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]

numero=filter(lambda x: '%2==0' in x, print("é par: ",[lista]))  
numero2=filter(lambda x: '%!=0' in x, print("é ímpar: ",[lista]))