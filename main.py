import telebot
from dotenv import load_dotenv
import os
from api import fetch_matches, format_match
from mocks.news import NEWS
from mocks.shop import SHOP

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


# Comando /news
@bot.message_handler(commands=['news'])
def news(msg: telebot.types.Message):
    # Formata o texto com as noticias
    for n in NEWS:
        # Formata o texto da notícia
        texto = (
            f"*{n['nome_noticia']}*\n"
            f"[Leia mais]({n['link_noticia']}) - {n['data_noticia']}\n"
            f"{n['descricao_noticia']}"
        )
        # Envia o texto da notícia
        bot.send_message(msg.chat.id, texto, parse_mode='Markdown')
        # Verifica se 'imagem_noticia' existe e não está vazio
        if 'imagem_noticia' in n and n['imagem_noticia']:
            bot.send_photo(msg.chat.id, n['imagem_noticia'])


# Comando /shop
@bot.message_handler(commands=['shop'])
def shop(msg: telebot.types.Message):
    # Formata o texto com os produtos
    for p in SHOP:
        # Formata o texto do produto
        texto = (
            f"*{p['nome_produto']}*\n"
            f"[Ver produto]({p['link_produto']})\n"
        )
        # Envia o texto do produto
        bot.send_message(msg.chat.id, texto, parse_mode='Markdown')
        # Verifica se 'imagem_produto' existe e não está vazio
        if 'imagem_produto' in p and p['imagem_produto']:
            bot.send_photo(msg.chat.id, p['imagem_produto'])
    # Envia o link para o site oficial da loja
    bot.send_message(
        msg.chat.id,
        "Entre no [site oficial da loja da FURIA](https://www.furia.gg) para conferir todos os produtos da loja.",
        parse_mode='Markdown'
    )


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
