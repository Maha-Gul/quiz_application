from data import load_questions

score = 0


def start_quiz():
    title, questions = load_questions("questions.json")
    print(f"Quiz Title: {title}")
    n = 9
    option_map = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
    }
    for question in questions:
        print(f"Question {len(questions)-n}: {question['question']}")
        print(f"Option A: {question['options'][0]}")
        print(f"Option B: {question['options'][1]}")
        print(f"Option C: {question['options'][2]}")
        print(f"Option D: {question['options'][3]}")
        user_answer = input("Please select an option (A, B, C, D): ")
        while not validate_answer(user_answer):
            user_answer = input("Please select an option (A, B, C, D): ")
        if user_answer.lower() in option_map:
            user_answer = question['options'][option_map[user_answer.lower()]]
        check_answer(user_answer, question['correct_answer'])
        n -= 1


def validate_answer(user_answer):
    valid_options = ["A", "B", "C", "D"]
    if user_answer.upper() in valid_options:
        return True
    else:
        print("Invalid option selected. Please try again.")
        return False


def check_answer(user_answer, correct_answer):
    global score
    if user_answer.lower() == correct_answer.lower():
        score += 1
        print("Excellent! Correct answer!")

    else:
        print(f"Incorrect answer. The correct answer is: {correct_answer}")


def display_score():
    global score
    print(f"Your final score is: {score}")
