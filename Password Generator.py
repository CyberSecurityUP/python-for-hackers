import random
import string

print("Bem vindo ao gerador de senhas!!")

tamanho = int(input("Digite o tamanho da senha: "))

minuscula = string.ascii_lowercase
maiuscula = string.ascii_uppercase
numeros = string.digits
simbolos = string.punctuation

all = minuscula + maiuscula + numeros + simbolos

randomizacao = random.sample(all,tamanho)

senha = "".join(randomizacao)

print(senha)