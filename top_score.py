from tkinter import *
import welcome_frame as wf
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import os


GO_HOME_C = "#ec77a5"
FONT_LABELS = ("Arial", 15, 'bold')
# FONT_ROWS = ("Arial", )


class TopPlayers(Frame):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.config(bg="white")
        # setup photos
        self.header_image = PhotoImage(
            file="img/top_player.png"
        )
        self.footer_image = PhotoImage(
            file="img/top_player_footer.png"
        )
        # Create canvas frame object
        # header
        self.header_canvas = Canvas(
            self,
            width=500,
            height=84,
            bg="white"
        )
        self.header_canvas_image = self.header_canvas.create_image(
            250, 42,
            image=self.header_image
        )
        # footer
        self.footer_canvas = Canvas(
            self,
            width=500,
            height=84,
            bg="white"
        )
        self.footer_canvas_image = self.footer_canvas.create_image(
            250, 42,
            image=self.footer_image
        )
        # Treeview
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure(
            'Treeview',
            background="white",
            forground="blue",
            rowheight=50,
            font=('Arial', 15, "bold"),
            fieldbackground="white"
        )
        self.style.configure(
            'Treeview.Heading',
            background="white",
            forground='blue',
            rowheight=15,
            font=('Arial', 18, "bold"),
            fieldbackground='white'
        )
        self.style.map(
            'Treeview',
            background=[('selected', 'orange')]
        )
        self.style.map(
            'Treeview.Heading',
            background=[('selected', "blue")]
        )
        self.top_players_table = ttk.Treeview(
            self,
            columns=("player", "score"),
            selectmode="browse",
            show="headings",
            height=6,
            padding=15
        )
        self.top_players_table.column(
            'player',
            anchor=CENTER,
            width=235
        )
        self.top_players_table.column(
            'score',
            anchor=CENTER,
            width=235
        )
        self.top_players_table.heading(
            'player',
            text='PLAYERS NAMES',
            anchor=CENTER
        )
        self.top_players_table.heading(
            'score',
            text='SCORES',
            anchor=CENTER
        )
        self.go_home_b = Button(
            self,
            text="Home",
            bg=GO_HOME_C,
            fg="white",
            highlightthickness=0,
            activebackground=GO_HOME_C,
            activeforeground="white",
            font=FONT_LABELS,
            command=self.go_home
        )
        self.load_player_data()
        # set widgets and frame
        self.header_canvas.grid(column=0, row=0, padx=15, pady=15)
        self.top_players_table.grid(column=0, row=2, padx=15, pady=15)
        self.footer_canvas.grid(column=0, row=3, padx=15, pady=15)
        self.go_home_b.grid(column=0, row=4, padx=15, pady=15, sticky=W + E)
        self.grid(column=0, row=0)

    def go_home(self):
        self.destroy()
        wf.WelcomeFrame(self.root)

    def load_player_data(self):
        if os.path.isfile("data/top_player.csv"):
            player_data = pd.read_csv("data/top_player.csv")
            player_data.sort_values(
                ['player score'],
                axis=0,
                ascending=[False],
                inplace=True
            )
            player_data.to_csv('data/top_player.csv', index=False)
            top_players = pd.read_csv("data/top_player.csv")
            players_name = top_players['player name'].tolist()
            players_score = top_players['player score'].tolist()
            for i in range(len(players_score)):
                self.top_players_table.insert(
                    parent='',
                    index='end',
                    iid=i,
                    values=(players_name[i], players_score[i])
                )
        else:
            messagebox.showinfo(
                title="Attention",
                message="There is no data saved yet!!"
            )



