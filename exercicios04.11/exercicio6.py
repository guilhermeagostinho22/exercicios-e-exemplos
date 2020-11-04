vf = int(input("digite um número: "))
funcoes = [
    lambda x: x**2,
    lambda x: x**3,
]
for f in funcoes:
    print(f(vf))