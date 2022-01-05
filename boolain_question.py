from tkinter import *
import welcome_frame as wf
import questions_bank

FOREGROUND_COLOR = "#234e71"
WRONG_ANSWER = "#e06565"
RIGHT_ANSWER = "#b0ef8f"
HOME_BUTTON_C = "#f68946"
FONT_HEADING = ("Arial", 25, 'bold')
FONT_QUESTION = ("Arial", 20, 'bold')
FONT_LABELS = ("Arial", 15, 'bold')


class BooleanQuestion(Frame):
    def __init__(self, root, questions_amount: str, quiz: questions_bank.QuizSetup):
        super().__init__()
        self.root = root
        self.number_of_question = questions_amount
        self.quiz_bank = quiz
        self.config(bg="white")
        # Setup Photos
        self.question_frame_img = PhotoImage(file="img/question_fram.png")
        self.true_image = PhotoImage(file="img/true_button.png")
        self.false_image = PhotoImage(file="img/false_button.png")
        self.happy_image = PhotoImage(file="img/happy_photo.png")
        self.sad_image = PhotoImage(file="img/sad_photo.png")
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
        # set 2 buttons true and false
        self.true_button = Button(
            self,
            image=self.true_image,
            highlightthickness=0,
            bd=0,
            bg="white",
            activebackground="white",
            command=lambda: self.answer_checked("True")
        )
        self.reaction_canvas = Canvas(
            self,
            width=150,
            height=150,
            bg="white",
            highlightthickness=0,
            bd=0
        )
        self.face_image = self.reaction_canvas.create_image(
            75, 75,
            image=self.happy_image,
        )
        self.false_button = Button(
            self,
            image=self.false_image,
            highlightthickness=0,
            bd=0,
            bg="white",
            activebackground="white",
            command=lambda: self.answer_checked("False")
        )
        self.play_again_b = Button(
            self,
            text="Play again",
            bg=FOREGROUND_COLOR,
            fg="white",
            highlightthickness=0,
            activebackground=FOREGROUND_COLOR,
            activeforeground="white",
            font=FONT_LABELS
        )
        self.go_home_b = Button(
            self,
            text="Home",
            bg=HOME_BUTTON_C,
            fg="white",
            highlightthickness=0,
            activebackground=HOME_BUTTON_C,
            activeforeground="white",
            font=FONT_LABELS,
            command=self.go_home
        )
        self.quiz_bank.start_quiz()
        self.start_multiple_quiz()
        # load quiz data
        self.false_button.grid(column=2, row=2, pady=20, padx=15)
        self.reaction_canvas.grid(column=1, row=2, padx=15, pady=20)
        self.true_button.grid(column=0, row=2, pady=20, padx=15)
        self.canvas_frame.grid(column=0, row=1, columnspan=3, padx=15, pady=15)
        self.total_score.grid(column=2, row=0, padx=15, pady=15)
        self.total_question.grid(column=0, row=0, columnspan=2, padx=15, pady=15)
        self.grid(column=0, row=0)

    def go_home(self):
        self.destroy()
        wf.WelcomeFrame(self.root)

    def start_multiple_quiz(self):
        self.canvas_frame.itemconfig(
            self.question_text,
            text=self.quiz_bank.question
        )

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
            text="You reach to the end of the game."
        )
        self.true_button.configure(state="disabled")
        self.false_button.configure(state="disabled")
        self.go_home_b.grid(column=0, row=5, columnspan=2, padx=15, pady=10, sticky=E + W)
        self.play_again_b.grid(column=0, row=4, columnspan=2, padx=15, pady=10, sticky=E + W)

    def play_again_same(self):
        self.quiz_bank.question_index = 0
        self.quiz_bank.question_number = 1
        self.quiz_bank.score = 0
        self.total_score.config(text=f"Score : {self.quiz_bank.score}")
        self.total_question.config(text=f"Q {self.quiz_bank.question_number} from {self.number_of_question}")
        self.true_button.configure(state="active")
        self.false_button.configure(state="active")
        self.start_multiple_quiz()
        self.play_again_b.grid_remove()
        self.go_home_b.grid_remove()
