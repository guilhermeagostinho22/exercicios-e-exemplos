def occupation(name):
    value=len(name)+1
    for i in range(1,value):
       count=i*-1
       print(name[count])    
invert=input("Qual nome/palavra voce deseja inverter? - ") 
occupation(invert)