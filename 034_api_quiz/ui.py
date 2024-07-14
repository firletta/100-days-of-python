from tkinter import Tk, Label, Button, Canvas, PhotoImage

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="", fill=THEME_COLOR, font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.setup_buttons()

        self.display_next_question()

    def setup_buttons(self):
        button_info = [("images/true.png", self.true_pressed, 0), ("images/false.png", self.false_pressed, 1)]
        self.buttons = []
        for image_file, command, column in button_info:
            image = PhotoImage(file=image_file)
            button = Button(image=image, highlightthickness=0, command=command)
            button.image = image
            button.grid(row=2, column=column)
            self.buttons.append(button)

    def display_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of the quiz.")
            for button in self.buttons:
                button.config(state="disabled")

    def true_pressed(self):
        self.provide_feedback(self.quiz_brain.check_answer("True"))

    def false_pressed(self):
        self.provide_feedback(self.quiz_brain.check_answer("False"))

    def provide_feedback(self, is_correct):
        color = "green" if is_correct else "red"
        self.canvas.config(bg=color)
        self.window.after(1000, self.display_next_question)

    def mainloop(self):
        self.window.mainloop()