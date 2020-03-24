# Necessary pandas, py-Trello
# to install run the command `python -m pip install py-Trello` and `python -m pip install pandas`

# This script gets:
# Painting Trello

###############################
#           imports           #
###############################

from trello import TrelloClient
from pandas import DataFrame

###############################
#     Request credential      #
###############################
client = TrelloClient(
    api_key='your api_key',
    api_secret='your api_secret',
    token='your token',
    token_secret='your token_secret'
)

###############################
#      selecting frame        #
###############################

all_boards = client.list_boards()
# lists all frames
print(all_boards)
# selects the project frame
frame = all_boards[1]
print("+====================================+")
print("|       Script to export CSV         |")
print("|====================================|")
print("|Board name:",frame.name,           "|")
print("+====================================+")
print()
#lists the columns in the frame
print(frame.all_lists())

###############################
#   columns id in the frame   #
###############################

columns_id = []
# ID das Listas no Board #
# for each column you want in the table, duplicate and place the column ID
columns_id.append(frame.get_list('column_ID'))

###############################
#             code            #
###############################

card_list = []
for board in columns_id:
    for card in board.list_cards():  
        object = {}
        object["Coluna"] = board 
        object["Nome"] = card.name
        object["Etiquetas"] = card.labels
        object["Data de Criação"] = card.card_created_date
        card_list.append(object)

###############################
#    Script to export CSV     #
###############################

# Exportando arquivos
export = DataFrame.from_dict(card_list)
# print(export)
export.to_excel ("Board_Trello.xlsx")
print("+====================================+")
print("|    Successfully generated file     |")
print("+====================================+")
