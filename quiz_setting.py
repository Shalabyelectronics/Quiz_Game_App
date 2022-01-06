from tkinter import *
import multiple_questions as mq
import boolain_question as bq
import questions_bank as qb
from tkinter import messagebox

THEMES_COLOR = "#25bede"
FOREGROUND_COLOR = "#234e71"
FONT_HEADING = ("Arial", 25, 'bold')
FONT_LABELS = ("Arial", 15, 'bold')
AMOUNT_OF_QUESTION = ["10", "20", "30", "40", "50"]
CATEGORY_DICTIONARY = {
    "General knowledge": 9,
    "Books": 10,
    "Board Games": 16,
    "Science and Nature": 17,
    "Science Computers": 18,
    "Science Mathematics": 19,
    "Sports": 21,
    "Geography": 22,
    "History": 23,
    "Politics": 24,
    "Art": 25,
    "Celebrities": 26,
    "Animals": 27
}
CATEGORY_LIST = [key for key, value in CATEGORY_DICTIONARY.items()]
DIFFICULTY = ['easy', 'medium', 'hard']
QUESTION_TYPE = ['multiple', 'boolean']


class QuizSetup(Frame):
    def __init__(self, root):
        super().__init__()
        self.player_name = None
        self.root = root
        self.config(bg="white")
        # Setup photos
        self.header_image = PhotoImage(file="img/header_block.png")
        self.ready_image = PhotoImage(file="img/ready_button.png")
        # Set all labels player name , number of questions, difficulty ,type all will be spinbox just player name
        # will be an entry
        self.canvas_header = Canvas(self, width=500, height=156, background="white")
        self.canvas_image_header = self.canvas_header.create_image(250, 78, image=self.header_image)

        self.canvas_footer = Canvas(self, width=500, height=156, background="white")
        self.canvas_image_footer = self.canvas_footer.create_image(250, 78, image=self.header_image)

        self.ready_button = Button(
            self,
            image=self.ready_image,
            bg="white",
            highlightthickness=0,
            bd=0,
            activebackground="white",
            command=self.start_quiz
        )

        self.setup_label = Label(
            self,
            text="Setup your quiz",
            bg="white",
            fg=FOREGROUND_COLOR,
            font=FONT_HEADING
        )
        self.player_name_label = Label(
            self,
            text="Player name",
            bg="white",
            fg=FOREGROUND_COLOR,
            font=FONT_LABELS
        )
        self.player_entry = Entry(
            self,
            width=20,
            font=FONT_LABELS,
            fg=FOREGROUND_COLOR,
            justify=CENTER
        )

        self.question_amount_label = Label(
            self,
            text="Number of questions",
            bg="white",
            fg=FOREGROUND_COLOR,
            font=FONT_LABELS
        )
        self.question_amount_var = StringVar()
        self.question_amount_var.set(AMOUNT_OF_QUESTION[0])
        self.question_amount_option = OptionMenu(
            self,
            self.question_amount_var,
            *AMOUNT_OF_QUESTION
        )
        self.question_amount_option.config(
            font=FONT_LABELS,
            bg='white',
            fg=FOREGROUND_COLOR,
            activebackground=THEMES_COLOR,
            cursor='hand2',
            width=17
        )
        self.question_amount_menu = self.nametowidget(self.question_amount_option.menuname)
        self.question_amount_menu.config(
            font=FONT_LABELS,
            bg='white',
            fg=FOREGROUND_COLOR,
            activebackground=THEMES_COLOR,
            cursor='hand2'
        )
        self.category_label = Label(
            self,
            text="Category",
            bg="white",
            fg=FOREGROUND_COLOR,
            font=FONT_LABELS
        )
        self.category_var = StringVar()
        self.category_var.set(CATEGORY_LIST[0])
        self.category_option = OptionMenu(
            self,
            self.category_var,
            *CATEGORY_LIST
        )
        self.category_option.config(
            font=FONT_LABELS,
            bg='white',
            fg=FOREGROUND_COLOR,
            activebackground=THEMES_COLOR,
            cursor='hand2',
            width=17
        )
        self.category_menu = self.nametowidget(self.category_option.menuname)
        self.category_menu.config(
            font=FONT_LABELS,
            bg='white',
            fg=FOREGROUND_COLOR,
            activebackground=THEMES_COLOR,
            cursor='hand2'
        )
        self.difficulty_label = Label(
            self,
            text="Difficulty",
            bg="white",
            fg=FOREGROUND_COLOR,
            font=FONT_LABELS
        )
        self.difficulty_var = StringVar()
        self.difficulty_var.set(DIFFICULTY[0])
        self.difficulty_option = OptionMenu(
            self,
            self.difficulty_var,
            *DIFFICULTY
        )
        self.difficulty_option.config(
            font=FONT_LABELS,
            bg='white',
            fg=FOREGROUND_COLOR,
            activebackground=THEMES_COLOR,
            cursor='hand2',
            width=17
        )
        self.difficulty_menu = self.nametowidget(self.difficulty_option.menuname)
        self.difficulty_menu.config(
            font=FONT_LABELS,
            bg='white',
            fg=FOREGROUND_COLOR,
            activebackground=THEMES_COLOR,
            cursor='hand2'
        )
        self.question_type_label = Label(
            self,
            text="Question type",
            bg="white",
            fg=FOREGROUND_COLOR,
            font=FONT_LABELS
        )
        self.question_type_var = StringVar()
        self.question_type_var.set(QUESTION_TYPE[0])
        self.question_type_option = OptionMenu(
            self,
            self.question_type_var,
            *QUESTION_TYPE
        )
        self.question_type_option.config(
            font=FONT_LABELS,
            bg='white',
            fg=FOREGROUND_COLOR,
            activebackground=THEMES_COLOR,
            cursor='hand2',
            width=17
        )
        self.question_type_menu = self.nametowidget(self.question_type_option.menuname)
        self.question_type_menu.config(
            font=FONT_LABELS,
            bg='white',
            fg=FOREGROUND_COLOR,
            activebackground=THEMES_COLOR,
            cursor='hand2'
        )

        self.setup_label.grid(column=0, row=0, columnspan=2, pady=5)
        self.canvas_header.grid(column=0, row=1, columnspan=2, pady=5, padx=15)
        self.player_name_label.grid(column=0, row=2, sticky=W, pady=15, padx=15)
        self.player_entry.grid(column=1, row=2, padx=15)
        self.category_label.grid(column=0, row=3, sticky=W, pady=15, padx=15)
        self.category_option.grid(column=1, row=3, padx=15)
        self.question_amount_label.grid(column=0, row=4, sticky=W, pady=15, padx=15)
        self.question_amount_option.grid(column=1, row=4)
        self.difficulty_label.grid(column=0, row=5, sticky=W, pady=15, padx=15)
        self.difficulty_option.grid(column=1, row=5)
        self.question_type_label.grid(column=0, row=6, sticky=W, pady=15, padx=15)
        self.question_type_option.grid(column=1, row=6)
        self.canvas_footer.grid(column=0, row=7, columnspan=2, pady=20, padx=15)
        self.show_ready_button = self.canvas_footer.create_window(250, 78, window=self.ready_button)
        self.grid(column=0, row=0)

    def start_quiz(self):
        if len(self.player_entry.get()) > 0:
            self.player_name = self.player_entry.get()
            if self.question_type_var.get() == "multiple":
                mq.MultipleQuestions(
                    self.root,
                    self.question_amount_var.get(),
                    self.player_name,
                    qb.QuizSetup(
                        self.player_entry.get(),
                        int(self.question_amount_var.get()),
                        self.difficulty_var.get(),
                        self.question_type_var.get(),
                        CATEGORY_DICTIONARY[self.category_var.get()]
                    )
                )
                self.destroy()
            else:
                if self.difficulty_var.get() != 'hard':
                    bq.BooleanQuestion(
                        self.root,
                        self.question_amount_var.get(),
                        self.player_name,
                        qb.QuizSetup(
                            self.player_entry.get(),
                            int(self.question_amount_var.get()),
                            self.difficulty_var.get(),
                            self.question_type_var.get(),
                            CATEGORY_DICTIONARY[self.category_var.get()]
                        )
                    )
                    self.destroy()
                else:
                    messagebox.showinfo(
                        title='Attention',
                        message="Hard difficulty is not available for this type of quiz!!"
                    )
