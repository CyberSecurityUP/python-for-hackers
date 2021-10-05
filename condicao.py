#simples = É uma condição aonde temos apenas uma ação, aonde só temos o IF
#composta = Uma estrutura de condição que tem mais de uma condição para uma ação, então temos o IF e o ELSE
idade = int(input("Digite uma idade: "))
if idade < 12:
    print("criança")
elif idade < 18:
    print("adolescente")
elif idade < 60:
    print("adulto")
else:
    print("idoso")