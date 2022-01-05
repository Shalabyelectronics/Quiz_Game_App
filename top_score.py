from tkinter import *
import welcome_frame as wf
from tkinter import ttk

GO_HOME_C = "#ec77a5"
FONT_LABELS = ("Arial", 15, 'bold')

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
            forground="white",
            rowheight=50,
            font=('Arial', 10, "bold"),
            fieldbackground="blue"
        )
        self.style.configure(
            'Treeview.Heading',
            background="white",
            forground='white',
            rowheight=15,
            font=('Arial', 15, "bold"),
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

        # set widgets and frame
        self.header_canvas.grid(column=0, row=0, padx=15, pady=15)
        self.top_players_table.grid(column=0, row=2, padx=15, pady=15)
        self.footer_canvas.grid(column=0, row=3, padx=15, pady=15)
        self.go_home_b.grid(column=0, row=4, padx=15, pady=15, sticky=W + E)
        self.grid(column=0, row=0)

    def go_home(self):
        self.destroy()
        wf.WelcomeFrame(self.root)
