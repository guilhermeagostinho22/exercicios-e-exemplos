escolha = int(input("1-cadastrar ou 2-Não cadastrar: "))
cadastro = 0

if cadastro <= 4:
    if escolha == 1:
        cadastro = cadastro + 1
        nomeCompleto = SyntaxWarning(input("Digite seu Nome completo: ")) 
        cpf = int(input("Digite seu CPF: "))
        senha = int(input("Digite sua senha: "))
        info = int(input("1-apto ou 2-Não está apto: "))
        print("Nome completo: ",nomeCompleto)
        print("CPF: ",cpf)
        if info == 1:
            print("Apto: Está apto") 
        else: 
            print("Apto: Não está apto")            
    else:
        print("Obrigado!!!")   
else:
    print("Obrigado!!!")          
    
   
