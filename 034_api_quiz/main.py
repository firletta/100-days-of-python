from data import question_bank
from quiz_brain import QuizBrain
from ui import QuizInterface

def main():
    quiz_brain = QuizBrain(question_bank)
    quiz = QuizInterface(quiz_brain)
    quiz.mainloop()

if __name__ == "__main__":
    main()