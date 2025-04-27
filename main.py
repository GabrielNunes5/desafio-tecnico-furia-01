import telebot
from dotenv import load_dotenv
import os
from api import fetch_matches, format_match

# Carregando as variaveis de ambiente
load_dotenv()

# Inicializando o bot com o token da API
bot = telebot.TeleBot(os.getenv("API_KEY"))


# Comando /start
@bot.message_handler(commands=['start', 'help'])
def start_msg(msg: telebot.types.Message):
    texto = """
    Salve! Eu sou o bot da TEAM FURIA CS!
Escolha uma das opções abaixo para continuarmos:
    /matches para ver as ultimas e próximas partidas do time da FURIA
    /news para ver as ultimas noticias do time da FURIA
    /shop para ver os produtos mais vendidos da loja oficial da FURIA
    /contact para ver os contatos do time da FURIA
    """
    bot.reply_to(msg, texto)


# Comando /matches
@bot.message_handler(commands=['matches'])
def matches(msg: telebot.types.Message):
    # Busca as partidas e formata o texto
    upcoming = fetch_matches(True)
    past = fetch_matches(False)
    texto = ["*Próximas 3 partidas:*"]
    texto += [f"• {format_match(m, True)}" for m in upcoming]
    texto.append("\n*Últimas 3 partidas:*")
    texto += [f"• {format_match(m, False)}" for m in past]
    # Envia tudo num único reply
    bot.send_message(msg.chat.id, "\n".join(texto), parse_mode='Markdown')


def verify(msg):
    return True


@bot.message_handler(func=verify)
def msg_padrao(msg: telebot.types.Message):
    texto = """
    Salve! Eu sou o bot da TEAM FURIA CS!
Escolha uma das opções abaixo para continuarmos:
    /matches para ver as ultimas e próximas partidas do time da FURIA
    /news para ver as ultimas noticias do time da FURIA
    /shop para ver os produtos mais vendidos da loja oficial da FURIA
    /contact para ver os contatos do time da FURIA
    """
    bot.reply_to(msg, texto)


bot.polling(none_stop=True, interval=0)
