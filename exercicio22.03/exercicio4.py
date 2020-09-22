age = 0

tiime = 0

k = 0

kg = (float(input("Qual o seu peso? ")))
timee = (float(input("Quantas horas você dormiu na última noite?")))
i = (int(input("Qual a sua idade? ")))

if i <= 69 and i >= 16:
  
  age += 1

else:
  print(" A idade a qual você nos forneceu não está dentro dos nossos requesitos, confira nossas indicações.")

if timee >= 6:
  
  tiime += 2

else:
  print(" O tempo de sono o qual você nos forneceu não está dentro dos nossos requesitos, confira nossas indicações.")

if kg >= 50:
  
  k += 3

else:
  print("O peso o qual você nos forneceu não está dentro dos nossos requesitos, confira nossas indicações")

if age == 1 and tiime == 2 and k == 3:
  print("Você está dentro das nossas indicações para ser doador(a)")

else: 
  print("Infelizmente você não pode ser doador por estar fora dos requisitos.")