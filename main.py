from welcome_frame import *

root = Tk()
root.title("Quiz Game App V1.0")
root.iconbitmap("img/my.ico")
root.geometry("+600+100")
root.resizable(False, False)
root.minsize(width=500, height=600)
WelcomeFrame(root)
root.mainloop()
