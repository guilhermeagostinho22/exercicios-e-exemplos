def check (name,comparename):
    if comparename == name [::-1]:
        return True 
    else:
        return False
nome = input("Informe o nome a ser verificado:") 
comparaNome = input ("Informe o nome invertido a ser comparado:") 
comparacao = check (comparaNome,nome)
print("Conferir - verificação - Verdadeiro = True / Falso = False.")
print ("o nome comparado é:",comparacao)