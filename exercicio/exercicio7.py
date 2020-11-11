for i in range(10): 
    n1=int(input("digite a nota 1 (de 0 a 10): "))
    n2=int(input("digite a nota 2 (de 0 a 10): "))
    media=lambda n1,n2: (n1*0.4) + (n2*0.6)
    print(media(n1,n2))

    if media >=0 and media <= 4.9:
        print("conceito D")
    elif media >=5 and media <= 6.9:
        print("conceito C")    
    elif media >=7 and media <= 8.9:
        print("conceito B") 
    else:
        print("conceito A")    

   