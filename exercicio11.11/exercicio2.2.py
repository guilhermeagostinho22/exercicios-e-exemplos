def leiaint():
    try:
        c = float(input("Digite um valor real: "))
        d = float(input("Digite um valor real: "))
        t = c/d
        print("O resultado foi: ", t)

    except(ValueError, TypeError):
        print("Infelizmente tivemos um problema com o valor digitado :( ")
    except(ZeroDivisionError):
        print("Infelizmente não é possivel dividir um número por zero :( ")
    except:
        print("Infelizmente tivemos um problema: ( ")
    finally:
        print("Volte sempre, Muito Obrigado!!!")
leiaint()