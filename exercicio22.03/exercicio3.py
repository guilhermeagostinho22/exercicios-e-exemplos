ageW = 0
numbW = 0
ageM = 0 
numbM =0

for f in range(0,10):

    sex=(input("Qual o seu sexo ? M para homem e W para mulher."))
    if sex == "M":
        numbM = numbM + 1
        ageM = ageM + (int(input("Qual a sua idade ?")))
    elif sex == "W":
      numbW = numbW + 1
      ageW = ageW + (int(input("Qual a sua idade ?")))


mm = (ageM / numbM)

g  =  (ageW + ageM)
g2 =  (numbM + numbW)

g3 =  (g / g2)

mw = (ageW / numbW)



print(" A média da idade dos entrevistados no geral foi de: ",g3)

print(" A média da idade das mulheres foi de:",mw)

print(" A média da idade dos homens foi de: ",mm)