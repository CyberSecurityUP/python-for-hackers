# ==	igual
# !=	diferente
# >	maior
# <	menor
# >=	maior ou igual
# <=	menor ou igual
while True:
    print("Bem vindo ao Menu")
    print("1 - Cadastro de nomes\n")
    print("2 - Ver nomes cadastrados\n")
    print("3 - Criador\n")
    menu = str(input("Digite a opção desejada: "))

    if menu == "1":
        print("\nBem vindo ao cadastro de nomes\n")
        nome = str(input("Digite o seu primeiro nome: "))
        print(nome)
        sobrenome = str(input("Digite o seu sobrenome nome: "))
        print(sobrenome)
        idade = int(input("Digite a sua idade: "))
        print(idade)
        peso = float(input("Digite o seu peso: "))
        print(peso)
        print(f"Ola {nome} {sobrenome} sua idade é {idade} e seu peso é {peso}")
        confirmar = input("Confirma? ")
        if confirmar == "Y":
            print("Cadastrado com sucesso")
        else:
            print("Cadastro não efetuado")
    elif menu == "2":
        nome = "Joas"
        sobrenome = "Antonio"
        print(nome, sobrenome)
    elif menu == "3":
        print("Criado por Joas")
    else:
        print("Programa finalizado")
        break