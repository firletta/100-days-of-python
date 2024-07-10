from tkinter import Tk, Canvas, PhotoImage, Button
import requests

class KanyeRestApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Kanye Says...")
        self.window.config(padx=50, pady=50)

        self.canvas = Canvas(width=300, height=414)
        self.background_img = PhotoImage(file="background.png")
        self.canvas.create_image(150, 207, image=self.background_img)
        self.quote_text = self.canvas.create_text(150, 207, text=self.get_quote(), width=250, font=("Arial", 24, "bold"), fill="white")
        self.canvas.grid(row=0, column=0)

        self.kanye_img = PhotoImage(file="kanye.png")
        self.kanye_button = Button(image=self.kanye_img, highlightthickness=0, command=self.update_quote)
        self.kanye_button.grid(row=1, column=0)

    def get_quote(self):
        try:
            response = requests.get("https://api.kanye.rest")
            response.raise_for_status()
            quote = response.json().get("quote", "No quote found.")
        except requests.RequestException:
            quote = "Failed to retrieve quote."
        return quote

    def update_quote(self):
        self.canvas.itemconfig(self.quote_text, text=self.get_quote())

    def run(self):
        self.window.mainloop()

def main():
    app = KanyeRestApp()
    app.run()

if __name__ == "__main__":
    main()