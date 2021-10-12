from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('SkyNet')
bot = ChatBot(
    'Skynet',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

conversa = ListTrainer(bot)
conversa.train([
    'Oi?',
    'Eae',
    'Qual o seu nome?',
    'Joas',
    'Prazer em te conhecer',
    'Igualmente meu patrão',
])
while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.5:
            print("Skinet: ", resposta)
        else:
            print("Eu não entendi :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break