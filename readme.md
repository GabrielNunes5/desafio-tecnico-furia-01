## 📌 Visão Geral

**Este arquivo define a lógica principal de um bot do Telegram para o time de CS da FURIA, utilizando a biblioteca telebot (pyTelegramBotAPI). O bot oferece comandos para visualizar partidas, notícias, produtos da loja oficial e informações de contato**

## 📁 Estrutura do Projeto

project/
├── main.py 
├── api.py
├── mocks/
│   ├── news.py
│   └── shop.py
├── .env
└── requirements.txt

## 🧩 Dependências

**telebot:** Biblioteca para interação com a API do Telegram.
**dotenv:** Carrega variáveis de ambiente do arquivo .env.
**requests:** Realiza requisições HTTP para APIs externas.

## ⚙️ Detalhes Técnicos

### api.py

Este módulo contém funções para integração com a API PandaScore:
    - fetch_matches(future: bool, limit: int = 3): Busca partidas futuras ou passadas.
    - format_match(match: dict, future: bool): Formata os dados de uma partida para exibição.

### main.py

Este é o arquivo principal que inicializa o bot e define os comandos:

/start ou /help: Mensagem inicial com as opções do bot.
/matches: Integra-se com api.py para buscar e exibir partidas.
/news: Usa o mock NEWS para exibir notícias.
/shop: Usa o mock SHOP para exibir produtos.
/contact: Exibe os contatos oficiais da FURIA.

## Mocks
Os mocks estão localizados na pasta mocks/:
    - news.py: Contém uma lista de notícias recentes do time de CS da FURIA. Aqui, poderia ser substituido por uma automação para sempre que sair uma nova noticia do time, o bot ja captura e envia. 
    - shop.py: Contém uma lista de alguns produtos da loja oficial da FURIA. Poderia ser substituido por uma API contendo todos os itens da loja, que estão sendo mais comprados, que estão com descontos especiais assim o bot poderia enviar produtos selecionados

## 🔧 Instalação

**1. Clone o repositório:**
```bash
    git clone https://github.com/GabrielNunes5/desafio-tecnico-furia-01.git
    cd desafio-tecnico-furia-01
```

**2. Crie um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

**3. Instale as dependências:**
    ```bash
pip install -r requirements.txt
    ```

**4. Configure as variáveis de ambiente no arquivo .env:**
API_KEY = "7674698181:AAHI4T3y_rpgW_Y0Op4NySOhPLeTjH6Akdk"
PANDASCORE_TOKEN = "Z3ZfbKwYCCvDcuBHUv9cSdhom84rRh09nlNBcq7KHWUsX6xvBl4"

## ​📨  Uso do Bot

**1. Execute o bot:**
```bash
python main.py
```

**2. Acesse o link do bot no navegador:**
https://t.me/team_furia_bot

**3. No Telegram, inicie uma conversa com o bot e use os comandos disponíveis:**
- /start ou /help
- /matches
- /news
- /shop
- /contact

## 📞 Contato
Para dúvidas ou sugestões, entre em contato comigo:
[Linkedin](https://www.linkedin.com/in/gabriel-nunes-085gn/)

## ✈️ Considerações finais
Esse codigo foi desenvolvido como parte de um desafio tecnico para um processo seletivo de Assistente de Engenharia de Software na FURIA
