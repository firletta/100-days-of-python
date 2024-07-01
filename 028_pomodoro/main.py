from tkinter import Tk, Canvas, Label, Button, PhotoImage

PINK = "#e2979c"
RED = "#f1583f"
GREEN = "#66c67f"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


class Pomodoro:

    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro")
        self.root.config(padx=100, pady=50, bg=YELLOW)

        self.setup_ui()

    def setup_ui(self):
        self.canvas = self.create_canvas()
        self.timer_title = self.create_title_text()
        self.timer_active = False
        self.checkmarks_label = self.checkmarks_label()
        self.start_button = self.create_button("Start", self.start_timer, 0, 2)
        self.reset_button = self.create_button("Reset", self.reset_timer, 2, 2)

    def create_canvas(self):
        self.tomato_img = PhotoImage(file="tomato.png")
        canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
        canvas.grid(column=1, row=1)
        return canvas

    def create_title_text(self):
        timer_title = Label(self.root,
                            text="Timer",
                            fg=GREEN,
                            bg=YELLOW,
                            font=(FONT_NAME, 42, "bold"),
                            pady=10)
        timer_title.grid(column=1, row=0)
        return timer_title

    def create_button(self, text, command, col, row):
        button = Button(self.root,
                        text=text,
                        highlightthickness=0,
                        highlightbackground=YELLOW,
                        command=command,
                        font=(FONT_NAME, 12, "normal"),
                        pady=4,
                        padx=8,)
        button.grid(column=col, row=row)
        return button

    def update_timer(self):
        if not self.timer_active:
            return
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            mins, secs = divmod(self.timer_seconds, 60)
            timer_text = f"{mins:02d}:{secs:02d}"
            self.canvas.itemconfig(self.timer_text, text=timer_text)
            self.root.after(1000, self.update_timer)
        else:
            self.checkmarks += 1
            self.checkmarks_label.config(text="✔" * self.checkmarks)

    def start_timer(self):
        self.timer_active = True
        self.timer_seconds = WORK_MIN * 60
        self.update_timer()

    def reset_timer(self):
        self.timer_active = False
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.checkmarks = 0
        self.checkmarks_label.config(text="")

    def checkmarks_label(self):
        self.checkmarks = 0
        checkmarks_label = Label(self.root,
                            text="✔" * self.checkmarks,
                            fg=GREEN,
                            bg=YELLOW,
                            font=(FONT_NAME, 24, "bold"),
                            pady=10)
        checkmarks_label.grid(column=1, row=4)
        return checkmarks_label

def main():
    window = Tk()
    app = Pomodoro(window)
    window.mainloop()


if __name__ == "__main__":
    main()
