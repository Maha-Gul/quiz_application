# menu and getting user input

from quiz import display_score, start_quiz


print(f"Welcome to the Quiz Application!")
print(f"Enter S to Start the quiz or Q to Quit the application.")
user_choice = input("Please select an option: ")

while user_choice.lower() not in ["s", "q"]:
    print(f"Invalid option selected. Please try again.")
    user_choice = input("Please select an option: ")
if user_choice.lower() == "s":
    print("Quiz started...")
    # start_quiz()
    start_quiz()
    display_score()

elif user_choice.lower() == "q":
    print("Quiz Closed...")

    # Call the function to quit the application
    # quit_application()
