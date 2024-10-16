from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)

@app.route("/")
def start():
    return (f'<h1>Guess a number between 0 and 9</h1>'
            f'<p>Random number for this session: {random_number}</p>'
            '<img style="max-width:400px;" src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjE5emN0Z3hkaG1sdjJmZGRqbmNxZjM4Z2dweTQ0dHphcXZ3bmJyNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l378khQxt68syiWJy/giphy.gif">')

@app.route("/<int:number>")
def guess(number):
    if number == random_number:
        return ('<h1 style="color:green;">You found me!</h1>'
                '<img style="max-width:400px;" src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjQ4Ym1pNW43NmFmMTU4ZTEzc2RwNGZtdzN2N25leW5scWo5cjdyNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oGRFp0AqM0BY4axjO/giphy.gif">')
    elif number < random_number:
        return ('<h1 style="color:red;">Too low, try again!</h1>'
                '<img style="max-width:400px;" src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWwzZW0zZ2pxbTB2aW5kaXlkaTU4Y3h5c2thYWNyYWZpdndwNXkyMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PR3585ZZSvcHO9pa76/giphy.gif">')
    else:
        return ('<h1 style="color:red;">Too high, try again!</h1>'
                '<img style="max-width:400px;" src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnRodjIwNTRwdm95bW1ndmltbmtpZmR5eXVwZ2tuMXFodXdkeDZqcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g8tLOZ6RWlDvRf5Kfp/giphy.gif">')

if __name__ == "__main__":
    app.run(debug=True)