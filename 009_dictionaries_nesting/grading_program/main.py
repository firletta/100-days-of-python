def main():
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99, 
        "Draco": 74,
        "Neville": 62,
        }

    student_grades = {}

    for student in student_scores:
        student_grades[student] = student_grade(student_scores[student])
    print(student_grades)

def student_grade(score):
    if score > 90:
        return "Outstanding"
    elif score > 80:
        return "Exceeds Expectations"
    elif score > 70:
        return "Acceptable"
    else:
        return "Fail"

if __name__ == "__main__":
    main()
