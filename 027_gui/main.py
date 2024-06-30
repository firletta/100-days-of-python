from tkinter import Tk, Entry, Label, Button, END

CONVERSION_FACTOR = 1.60934
FONT = ("Arial", 24)

class MilesToKilometersConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Miles to Kilometers Converter")
        self.root.config(padx=20, pady=20)

        self.setup_ui()

    def setup_ui(self):
        self.input_miles = self.create_entry(1, 0, "0")
        self.create_label(2, 0, "miles")
        self.create_label(0, 1, "=")
        self.kilometers_result_label = self.create_label(1, 1, "0", width=10)
        self.create_label(2, 1, "km")
        self.create_button(1, 2, "Calculate", self.update_kilometers_result)

    def create_entry(self, col, row, initial_value):
        entry = Entry(self.root, font=FONT, justify="center", width=10)
        entry.insert(END, initial_value)
        entry.grid(column=col, row=row, padx=4, pady=4)
        return entry

    def create_label(self, col, row, text, width=None):
        label = Label(self.root, text=text, font=FONT, width=width)
        label.grid(column=col, row=row, padx=4, pady=4)
        return label

    def create_button(self, col, row, text, command):
        Button(self.root, text=text, font=FONT, command=command).grid(column=col, row=row)

    def convert_miles_to_kilometers(self, miles):
        try:
            return float(miles) * CONVERSION_FACTOR
        except ValueError:
            return 0

    def update_kilometers_result(self):
        miles = self.input_miles.get()
        kilometers = self.convert_miles_to_kilometers(miles)
        self.kilometers_result_label.config(text=f"{kilometers:.2f}")

def main():
    window = Tk()
    app = MilesToKilometersConverter(window)
    window.mainloop()

if __name__ == "__main__":
    main()