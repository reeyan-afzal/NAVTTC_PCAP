"""
Evaluates Grades based on Scores.
"""


def input_validator():
    while True:
        score_input = input("Enter the score (0-100): ")

        if not score_input.strip():
            print("Input cannot be empty. Please enter a valid score.")
            continue

        try:
            _score = float(score_input)
            if _score < 0 or _score > 100:
                print("Invalid score. Please enter a score between 0 and 100.")
                continue
            return _score
        except ValueError:
            print("Invalid input. Please enter a numeric score.")


def evaluate_grade(_score):
    if _score < 0 or _score > 100:
        return "Invalid score. Please enter a score between 0 and 100."

    if _score >= 90:
        return "A"
    elif _score >= 80:
        return "B"
    elif _score >= 70:
        return "C"
    elif _score >= 60:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    score = input_validator()
    grade = evaluate_grade(score)
    print("The grade is:", grade)
