# Script_Trello
Script para extração em .CSV do Trello

# Instalar
```
pip instalar py-trello
```
# Uso
- importando a lib
```
from trello import TrelloClient
```
- utilizando o TrelloClient
```
client = TrelloClient (
     api_key = ' sua-chave ' ,
     api_secret = ' seu-segredo ' ,
     token = ' sua-oauth-chave-de-token ' ,
     token_secret = ' seu-oauth-token-secreto ' 
)
```

O ``` token ``` e ``` token_secret ``` vêm do processo OAuth, ``` api_key ``` e ```api_secret``` são as credenciais da API do Trello. Para conseguir as credenciais <a href="https://trello.com/app-key">( clique aqui ).</a>
