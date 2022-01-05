from tkinter import *

import questions_bank
import welcome_frame as wf

THEMES_COLOR = "#25bede"
FOREGROUND_COLOR = "#234e71"
RIGHT_COLOR = "#b0ef8f"
WRONG_COLOR = "#f63946"
Button_ONE_C = "#fcd109"
Button_TWO_C = "#ec77a5"
Button_THREE_C = "#f68946"
Button_FOUR_C = "#25bede"
FONT_HEADING = ("Arial", 25, 'bold')
FONT_QUESTION = ("Arial", 20, 'bold')
FONT_LABELS = ("Arial", 15, 'bold')


class MultipleQuestions(Frame):
    def __init__(self, root, questions_amount: str,player_name: str, quiz: questions_bank.QuizSetup):
        super().__init__()
        self.buttons_var = None
        self.root = root
        self.number_of_question = questions_amount
        self.quiz_bank = quiz
        self.config(bg="white")
        # Setup Photos
        self.question_frame_img = PhotoImage(file="img/question_fram.png")
        # set title of the frane as 2 part total questions and score each one on different cell
        self.total_question = Label(
            self,
            text=f"Q 1 from {self.number_of_question}",
            font=FONT_HEADING,
            fg=FOREGROUND_COLOR,
            bg="white"
        )
        self.total_score = Label(
            self,
            text=f"Score : {self.quiz_bank.score}",
            font=FONT_HEADING,
            fg=FOREGROUND_COLOR,
            bg="white"
        )

        # Create canvas frame object
        self.canvas_frame = Canvas(self, width=500, height=358, bg="white")
        self.canvas_frame_image = self.canvas_frame.create_image(250, 179, image=self.question_frame_img)
        # self.canvas_rectangle = self.canvas_frame.create_rectangle()
        self.question_text = self.canvas_frame.create_text(
            250, 179,
            text="Here is a question Here is a question Here is a question",
            font=FONT_QUESTION,
            width=490,
            fill=FOREGROUND_COLOR
        )
        # Set 4 buttons
        self.answer_one_b_var = StringVar()
        self.answer_one_b = Button(
            self,
            textvariable=self.answer_one_b_var,
            bg=Button_ONE_C,
            fg=FOREGROUND_COLOR,
            highlightthickness=0,
            activebackground=Button_ONE_C,
            activeforeground=FOREGROUND_COLOR,
            font=FONT_LABELS,
            command=lambda: self.answer_checked(self.answer_one_b_var.get())
        )
        self.answer_two_b_var = StringVar()
        self.answer_two_b = Button(
            self,
            textvariable=self.answer_two_b_var,
            bg=Button_TWO_C,
            fg=FOREGROUND_COLOR,
            highlightthickness=0,
            activebackground=Button_TWO_C,
            activeforeground=FOREGROUND_COLOR,
            font=FONT_LABELS,
            command=lambda: self.answer_checked(self.answer_two_b_var.get())
        )
        self.answer_three_b_var = StringVar()
        self.answer_three_b = Button(
            self,
            textvariable=self.answer_three_b_var,
            bg=Button_THREE_C,
            fg=FOREGROUND_COLOR,
            highlightthickness=0,
            activebackground=Button_THREE_C,
            activeforeground=FOREGROUND_COLOR,
            font=FONT_LABELS,
            command=lambda: self.answer_checked(self.answer_three_b_var.get())
        )
        self.answer_four_b_var = StringVar()
        self.answer_four_b = Button(
            self,
            textvariable=self.answer_four_b_var,
            bg=Button_FOUR_C,
            fg=FOREGROUND_COLOR,
            highlightthickness=0,
            activebackground=Button_FOUR_C,
            activeforeground=FOREGROUND_COLOR,
            font=FONT_LABELS,
            command=lambda: self.answer_checked(self.answer_four_b_var.get())
        )
        self.play_again_b = Button(
            self,
            text="Play again",
            bg=FOREGROUND_COLOR,
            fg="white",
            highlightthickness=0,
            activebackground=FOREGROUND_COLOR,
            activeforeground="white",
            font=FONT_LABELS,
            command=self.play_again_same
        )
        self.go_home_b = Button(
            self,
            text="Home",
            bg=Button_THREE_C,
            fg="white",
            highlightthickness=0,
            activebackground=Button_THREE_C,
            activeforeground="white",
            font=FONT_LABELS,
            command=self.go_home
        )
        self.quiz_bank.start_quiz()
        self.start_multiple_quiz()
        # Set grid
        self.answer_four_b.grid(column=1, row=3, pady=15, padx=15, sticky=E + W)
        self.answer_three_b.grid(column=0, row=3, pady=15, padx=15, sticky=E + W)
        self.answer_two_b.grid(column=1, row=2, pady=15, padx=15, sticky=E + W)
        self.answer_one_b.grid(column=0, row=2, pady=15, padx=15, sticky=E + W)
        self.canvas_frame.grid(column=0, row=1, columnspan=2, padx=15, pady=15)
        self.total_score.grid(column=1, row=0, padx=15, pady=15)
        self.total_question.grid(column=0, row=0, padx=15, pady=15)
        self.grid(column=0, row=0)

    def go_home(self):
        self.destroy()
        wf.WelcomeFrame(self.root)

    def start_multiple_quiz(self):
        self.canvas_frame.itemconfig(
            self.question_text,
            text=self.quiz_bank.question
        )
        answers_list = self.quiz_bank.all_answers
        self.buttons_var = [
            self.answer_one_b_var,
            self.answer_two_b_var,
            self.answer_three_b_var,
            self.answer_four_b_var
        ]
        for answer in range(4):
            self.buttons_var[answer].set(answers_list[answer])

    def answer_checked(self, answer):
        if self.quiz_bank.check_answers(answer):
            self.canvas_frame.configure(bg="green")
            self.quiz_bank.score += 1
            self.total_score.config(text=f"Score : {self.quiz_bank.score}")
            if self.quiz_bank.is_finish():
                self.after(1000, self.next_question)
            else:
                self.after(1000, self.end_of_game)
        else:
            self.canvas_frame.configure(bg="red")
            if self.quiz_bank.is_finish():
                self.after(1000, self.next_question)
            else:
                self.after(1000, self.end_of_game)

    def next_question(self):
        self.canvas_frame.configure(background="white")
        self.quiz_bank.next_question()
        self.total_question.config(text=f"Q {self.quiz_bank.question_number} from {self.number_of_question}")
        self.quiz_bank.multiple_quiz()
        self.start_multiple_quiz()

    def end_of_game(self):
        self.canvas_frame.configure(background="white")
        self.canvas_frame.itemconfig(
            self.question_text,
            text=f"{self.player_name.title()} you reached to the end of the game."
        )
        disable_buttons = [self.answer_one_b, self.answer_two_b, self.answer_three_b, self.answer_four_b]
        for button in range(len(disable_buttons)):
            self.buttons_var[button].set("See you!!")
            disable_buttons[button].configure(state="disabled")

        self.go_home_b.grid(column=0, row=5, columnspan=2, padx=15, pady=10, sticky=E + W)
        self.play_again_b.grid(column=0, row=4, columnspan=2, padx=15, pady=10, sticky=E + W)

    def play_again_same(self):
        self.quiz_bank.question_index = 0
        self.quiz_bank.question_number = 1
        self.quiz_bank.score = 0
        self.total_score.config(text=f"Score : {self.quiz_bank.score}")
        self.total_question.config(text=f"Q {self.quiz_bank.question_number} from {self.number_of_question}")
        disable_buttons = [self.answer_one_b, self.answer_two_b, self.answer_three_b, self.answer_four_b]
        for button in range(len(disable_buttons)):
            disable_buttons[button].configure(state="active")
        self.start_multiple_quiz()
        self.play_again_b.grid_remove()
        self.go_home_b.grid_remove()
