from tkinter import messagebox, PhotoImage, Canvas, Label, Button, Tk

PINK = "#e2979c"
RED = "#f1583f"
GREEN = "#66c67f"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.config(padx=100, pady=50, bg=YELLOW)

        self.session_count = 0
        self.focus_time_count = 0
        self.is_timer_running = False
        self.timer_seconds = 0
        self.timer_after_id = None

        self.setup_ui()

    def setup_ui(self):
        self.timer_label = Label(self.root, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 42, "bold"))
        self.timer_label.grid(column=1, row=0)

        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
        self.canvas.grid(column=1, row=1)

        self.start_button = self.create_button("Start", self.start_timer, 0, 2)
        self.reset_button = self.create_button("Reset", self.reset_timer, 2, 2)

        self.checkmarks_label = Label(self.root, text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
        self.checkmarks_label.grid(column=1, row=3)

    def create_button(self, text, command, col, row):
        button = Button(self.root, text=text, highlightthickness=0, highlightbackground=YELLOW, command=command, font=(FONT_NAME, 12, "normal"))
        button.grid(column=col, row=row)
        return button

    def update_timer(self):
        if self.timer_seconds > 0:
            self.timer_seconds -= 1
            mins, secs = divmod(self.timer_seconds, 60)
            self.canvas.itemconfig(self.timer_text, text=f"{mins:02d}:{secs:02d}")
            self.timer_after_id = self.root.after(1000, self.update_timer)
        else:
            self.update_checkmarks()
            self.start_next_session()
            

    def start_timer(self):
        if not self.is_timer_running:
            self.is_timer_running = True
            self.session_count += 1
            self.set_timer_session()
            self.update_timer()

    def reset_timer(self):
        if self.is_timer_running:
            self.is_timer_running = False
            if self.timer_after_id:
                self.root.after_cancel(self.timer_after_id)
            self.canvas.itemconfig(self.timer_text, text="00:00")
            self.timer_label.config(text="Timer", fg=GREEN)
            self.checkmarks_label.config(text="")
            self.session_count = 0

    def set_timer_session(self):
        if self.session_count % 8 == 0:
            self.timer_seconds = LONG_BREAK_MIN * 60
            self.timer_label.config(text="Long Break", fg=RED)
        elif self.session_count % 2 == 0:
            self.timer_seconds = SHORT_BREAK_MIN * 60
            self.timer_label.config(text="Short Break", fg=PINK)
        else:
            self.timer_seconds = WORK_MIN * 60
            self.timer_label.config(text="Work Time", fg=GREEN)
            self.focus_time_count += 1

    def start_next_session(self):
        self.is_timer_running = False
        messagebox.showinfo(title="Session Ended", message="Time for the next pomodoro session!")
        self.start_timer()

    def update_checkmarks(self):
        checkmarks = "✔" * self.focus_time_count
        self.checkmarks_label.config(text=checkmarks)

def main():
    root = Tk()
    PomodoroApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()