from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    question_bank = [
        Question(question["question"], question["correct_answer"])
        for question in question_data
    ]

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()

    print(f"You've completed the quiz.\nYour final score was: "
          f"{quiz.score}/{quiz.question_number}")


if __name__ == "__main__":
    main()
