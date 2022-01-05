from tkinter import *
import quiz_setting as qs
import top_score as ts
THEMES_COLOR = "#25bede"
FOREGROUND_COLOR = "#234e71"
FONT_HEADING = ("Arial", 25, 'bold')


class WelcomeFrame(Frame):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.config(bg="white")
        # create canvas background , score and start images
        self.welcome_image = PhotoImage(file="img/welcome_bg.png")
        self.score_image = PhotoImage(file="img/scores.png")
        self.start_image = PhotoImage(file="img/start_button.png")
        self.welcome_label = Label(
            self,
            text="Welcome to Quiz Game App",
            bg="white",
            fg=FOREGROUND_COLOR,
            font=FONT_HEADING
        )
        self.canvas = Canvas(self, width=500, height=500, background="white")
        self.canvas_image = self.canvas.create_image(250, 250, image=self.welcome_image)

        self.start_button = Button(
            self,
            image=self.start_image,
            highlightthickness=0,
            bd=0,
            bg="white",
            activebackground='white',
            command=self.setting_frame
        )

        self.score_button = Button(
            self,
            image=self.score_image,
            highlightthickness=0,
            bd=0,
            bg="white",
            activebackground='white',
            command=self.top_players_frame
        )

        self.score_button.grid(column=0, row=2, pady=15)
        self.start_button.grid(column=1, row=2, pady=15)
        self.welcome_label.grid(column=0, row=0, columnspan=2, pady=15)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=15, pady=15)
        self.grid(column=0, row=0)

    def setting_frame(self):
        self.destroy()
        qs.QuizSetup(self.root)

    def top_players_frame(self):
        self.destroy()
        ts.TopPlayers(self.root)



