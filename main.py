# menu and getting user input
print(f"Welcome to the Quiz Application!")
print(f"Enter S to Start the quiz or Q to Quit the application.")
user_choice = input("Please select an option: ")

while user_choice.lower() not in ["s", "q"]:
    print(f"Invalid option selected. Please try again.")
    user_choice = input("Please select an option: ")
if user_choice.lower() == "s":
    print(f"Quiz started...")
    # Call the function to start the quiz
    # start_quiz()
elif user_choice.lower() == "q":
    print(f"Quiz Closed...")

    # Call the function to quit the application
    # quit_application()
