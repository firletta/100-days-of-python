import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

class FlashCardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Flash Cards")
        self.master.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.words = pd.read_csv("data/french_words.csv").to_dict(orient="records")
        self.current_card = {}
        self.setup_ui()

    def setup_ui(self):
        self.canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.card_front_img = tk.PhotoImage(file="images/card_front.png")
        self.card_back_img = tk.PhotoImage(file="images/card_back.png")
        self.card_image = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
        self.right_image = tk.PhotoImage(file="images/right.png")
        self.wrong_image = tk.PhotoImage(file="images/wrong.png")
        self.right_button = self.create_button(self.right_image, self.handle_right_answer, row=1, col=0)
        self.wrong_button = self.create_button(self.wrong_image, self.handle_wrong_answer, row=1, col=1)
        self.show_card()

    def create_button(self, image, command, row, col):
        button = tk.Button(image=image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, bg=BACKGROUND_COLOR, command=command)
        button.grid(row=row, column=col)
        return button

    def show_card(self):
        if self.words:
            self.current_card = random.choice(self.words)
            self.update_canvas("French", self.current_card["French"], self.card_front_img)
            self.master.after(3000, self.flip_card)
        else:
            self.update_canvas("Well done!", "All words were reviewed.", self.card_front_img)

    def flip_card(self):
        self.update_canvas("English", self.current_card["English"], self.card_back_img)

    def update_canvas(self, title, word, image):
        self.canvas.itemconfig(self.card_image, image=image)
        self.canvas.itemconfig(self.card_title, text=title, fill="black")
        self.canvas.itemconfig(self.card_word, text=word, fill="black")
        self.canvas.tag_raise(self.card_title)
        self.canvas.tag_raise(self.card_word)

    def handle_right_answer(self):
        try:
            self.words.remove(self.current_card)
        except ValueError:
            pass
        self.show_card()

    def handle_wrong_answer(self):
        self.show_card()

def main():
    root = tk.Tk()
    app = FlashCardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
