'''
?amount=10&category=17&difficulty=easy&type=multiple
This is the API End point https://opentdb.com/api.php
and there are it is parameters [amount=10, category= 9 to 27, difficulty=easy or medium or hard, type=multiple or boolean, encode=url3986 or base64 or ]
category name and number
General knowledge 9
Entertainment : Books 10
Entertainment : Board Games 16
Science and Nature 17
Science Computers 18
Science Mathematics 19
Sports 21
Geography 22
History 23
Politics 24
Art 25
Celebrities 26
Animals 27
'''

# lets import requests to check the Trivia API
# import json
# import html
# import requests
#
# trivia_parameters = {
#     'amount': 10,
#     'difficulty': 'easy',
#     'type': 'boolean',
#
# }
# trivia_request = requests.get("https://opentdb.com/api.php", params=trivia_parameters)
# trivia_request.raise_for_status()
# with open("data/question_temp.json", 'w') as q_data_file:
#     json.dump(trivia_request.json(), q_data_file, indent=4)
#
# with open("data/question_temp.json", 'r') as q_data_file:
#     data = json.load(q_data_file)
#     question_list = data['results']
#     # for q in range(len(question_list)):
#     #     question_list[q]['question'].replace(question_list[q]['question'], html.unescape(question_list[q]['question']))
#     #     question_list[q]['correct_answer'].replace(question_list[q]['correct_answer'], html.unescape(question_list[q]['correct_answer']))
#     #     for i in range(len(question_list[q]['incorrect_answers'])):
#     #         question_list[q]['incorrect_answers'][i].replace(question_list[q]['incorrect_answers'][i], html.unescape(question_list[q]['incorrect_answers'][i]))
#     # test = question_list[3]['question'].replace(
#     #     question_list[3]['question'],
#     #     html.unescape(question_list[3]['question'])
#     # )
#     # print(len(question_list))
#     # data.update(data)
#
# with open("data/question_temp.json", "w") as question_data:
#     json.dump(data, question_data, indent=4)
#
# # to go over strange html sympol and it's called html character entities by using html.unescape(text) from html module.
#
# from tkinter import *
#
# root = Tk()
#
#
# def change_color():
#     canvas.configure(background="red")
#     root.after(1000, return_defualt)
#
#
# def return_defualt():
#     canvas.configure(background="green")
#
#
# canvas = Canvas(root, width=100, height=100, background="green")
# button = Button(root, text="change color after one second", command=change_color)
#
# button.pack()
# canvas.pack()
# root.mainloop()
import pandas as pd

# now I want to loop inside two list player name and score
'''
top_players = pd.read_csv("data/top_player.csv")
players_name = top_players['player name'].tolist()
players_score = top_players['player score'].tolist()
for i in range(len(players_score)):
    print(f"Player {players_name[i]} has {players_score[i]} score.")
'''
# arranging row from the best score to the lower one
'''
top_player_data = pd.read_csv('top_player.csv')
from_best = top_player_data.sort_values(
    ['player score'],
    axis=0,
    ascending=[False],
    inplace=True
)
top_player_data.to_csv('top_player.csv', index=False)

'''

# create a csv file from dataframe
'''
player_score = {
    'player name': ['Shalaby', 'ali'],
    'player score': ['100', '50']
}

top_player = pd.DataFrame(player_score)
top_player.to_csv("top_player.csv", index=False)
'''

top_player_data = pd.read_csv('data/top_player.csv')
add_data = top_player_data.to_dict()
player_name = input("Please inter your name : ").lower()
player_score = input("Please inter your score : ")
index_key = 0
if player_name not in add_data['player name'].values():
    check_last = add_data['player name'].keys()
    for i in check_last:
        index_key = i + 1
    add_data['player name'][index_key] = player_name
    add_data['player score'][index_key] = player_score
    # update csv
    update_date = pd.DataFrame(add_data)
    update_date.to_csv("data/top_player.csv", index=False)
else:
    player_key = list(add_data['player name'].keys())[list(add_data['player name'].values()).index(player_name)]
    add_data['player score'][player_key] = player_score
    update_date = pd.DataFrame(add_data)
    update_date.to_csv("data/top_player.csv", index=False)
