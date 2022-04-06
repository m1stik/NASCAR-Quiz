from tkinter import *
from tkinter import messagebox
from game_logic import GameLogic

THEME_COLOR = "#007bbf"
FONT = ("Tahoma", 18, "italic")

class UserInterface:
    
    # Initializing and menu display
    def __init__(self):
        self.window = Tk()
        self.window.title("NASCAR Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.menu_label = Label(text="Choose a game mode", bg=THEME_COLOR, fg="white", font=("Tahoma", 16))
        self.menu_label.grid(column=0, row=0, columnspan=2, pady=10)

        self.number_gamemode = Button(bg="white", highlightthickness=0, text="Guess the number", command=self.gamemode_number)
        self.number_gamemode.grid(column=0, row=1, padx=20)

        self.manufacturer_gamemode = Button(bg="white", highlightthickness=0, text="Guess manufacturer", command=self.gamemode_manufacturer)
        self.manufacturer_gamemode.grid(column=1, row=1)

        self.window.mainloop()

    # Starting the game with the game mode
    def gamemode_number(self):
        self.menu_label.grid_forget()
        self.number_gamemode.grid_forget()
        self.manufacturer_gamemode.grid_forget()

        self.game_logic = GameLogic("number")
        self.display_game()
        self.get_next_question()

    def gamemode_manufacturer(self):
        self.menu_label.grid_forget()
        self.number_gamemode.grid_forget()
        self.manufacturer_gamemode.grid_forget()

        self.game_logic = GameLogic("manufacturer")
        self.display_game()
        
    # Display game interface
    def display_game(self):
        self.score_label = Label(text="Your score: 0", bg=THEME_COLOR, fg="white", font=("Tahoma", 16))
        self.score_label.grid(column=0, row=0, pady=10, columnspan=2)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 125, text="Quiz", font=FONT, width=280, fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.entry = Entry(bg="white", highlightthickness=0)
        self.entry.grid(column=0, row=2)

        self.button_entry = Button(bg="white", highlightthickness=0, text="Answer", command=self.send_answer)
        self.button_entry.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    # Getting the next question from the game logic class
    def get_next_question(self):
        if self.game_logic.question_number > 10:
            answer = messagebox.askyesno("Game over", f"Your score is {self.game_logic.points}/10. Do you want to play again?")
            if answer:
                self.game_logic.points = 0
                self.game_logic.question_number = 0
            else:
                quit()

        self.canvas.config(bg="white")
        self.score_label.config(text=f"Your score: {self.game_logic.points}")
        self.canvas.itemconfig(self.quiz_text, fill=THEME_COLOR)
        question_text = self.game_logic.next_question()
        self.canvas.itemconfig(self.quiz_text, text=question_text)

    # sending user's input to the logic class, getting feedback
    def send_answer(self):
        user_answer = self.entry.get()
        self.is_right = self.game_logic.check_answer(user_answer)
        self.give_feedback(self.is_right)
        self.entry.delete(0, END)
    
    # display results of the answer, start next question
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Your score: {self.game_logic.points}")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.quiz_text, text=self.game_logic.get_correct_answer(), fill="white")
        
        self.window.after(1500, self.get_next_question)