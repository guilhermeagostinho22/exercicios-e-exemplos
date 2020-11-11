
def leiaint():
    try:
        a = int(input("Digite um valor inteiro real: "))
        b = int(input("Digite um valor inteiro real: "))
        r = a/b
        print("O resultado foi: ", r)

    except(ValueError, TypeError):
        print("Infelizmente tivemos um problema com o valor digitado :( ")
    except(ZeroDivisionError):
        print("Infelizmente não é possivel dividir um número por zero :( ")
    except:
        print("Infelizmente tivemos um problema: ( ")
    finally:
        print("Volte sempre, Muito Obrigado!!!")
leiaint()
