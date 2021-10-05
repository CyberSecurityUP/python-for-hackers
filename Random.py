import random

j1 = input("(1 Jogador digite o seu nome)" "Digite o seu Nome: ")
j2 = input("(1 Jogador digite o seu nome)" "Digite o seu Nome: ")
j3 = input("(1 Jogador digite o seu nome)" "Digite o seu Nome: ")

sort = random.randint(1,10)

if sort == 1:
    print('Parabéns',j1,'Você Ganhou!!')
    print(sort)
elif sort == 3:
    print('Parabéns',j2,'Você Ganhou!!')
    print(sort)
elif sort == 5:
    print('Parabéns',j3,'Você Ganhou!!')
    print(sort)
else:
    print("Ninguém ganhou")