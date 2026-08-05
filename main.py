# menu and getting user input

from data import load_questions


print(f"Welcome to the Quiz Application!")
print(f"Enter S to Start the quiz or Q to Quit the application.")
user_choice = input("Please select an option: ")

while user_choice.lower() not in ["s", "q"]:
    print(f"Invalid option selected. Please try again.")
    user_choice = input("Please select an option: ")
if user_choice.lower() == "s":
    print("Quiz started...")
    # start_quiz()

    title, questions = load_questions("questions.json")
    print(f"Quiz Title: {title}")
    n = 9
    for question in questions:
        print(f"Question {len(questions)-n}: {question['question']}")
        print(f"Options: {question['options']}")
        print(f"Answer: {question['correct_answer']}")
        print(f"Explanation: {question['explanation']}")
        n -= 1
elif user_choice.lower() == "q":
    print("Quiz Closed...")

    # Call the function to quit the application
    # quit_application()
