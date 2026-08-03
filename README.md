# Quiz Application MVP

This project is a beginner-friendly Python command-line quiz application. The goal of the MVP is to let users choose a quiz category, answer multiple-choice questions loaded from a JSON file, and see their final score at the end.

## Project Goal

Build a simple quiz app that demonstrates:
- basic Python program structure
- reusable functions
- user input handling
- JSON file loading
- score calculation and display

## Implementation Steps

1. Set up the project structure
   - Create a Python file such as `main.py` for the application logic.
   - Create a folder for data files, such as `data/`.
   - Add a JSON file to store quiz questions and answers.

2. Design the quiz data format
   - Define a simple structure for each question in the JSON file.
   - Include fields such as:
     - category
     - question
     - options
     - correct_answer
   - Make sure the JSON file contains multiple questions for at least one category.

3. Create the quiz categories
   - Decide which categories will be available in the app.
   - Load the quiz questions from the JSON file based on the selected category.

4. Build the main program flow
   - Display a welcome message to the user.
   - Ask the user to choose a quiz category.
   - Load the relevant questions from the JSON file.
   - Start the quiz loop.

5. Implement question handling
   - Show one question at a time.
   - Display the multiple-choice options clearly.
   - Accept the user’s answer.
   - Compare the answer with the correct answer.
   - Update the score if the answer is correct.

6. Add score tracking
   - Keep track of the number of correct answers.
   - Keep track of the total number of questions.
   - Calculate the final score after the quiz ends.

7. Display results
   - Show the user’s final score.
   - Display a message such as "Quiz completed" or a performance summary.

8. Improve the user experience
   - Add input validation so invalid choices are handled gracefully.
   - Add a simple menu for selecting categories.
   - Add clear prompts and friendly messages.

9. Test the application
   - Run the app and try different categories.
   - Check that questions load correctly from the JSON file.
   - Verify that scoring works as expected.
   - Confirm that the program handles incorrect or invalid input properly.

## Suggested Project Files

- `main.py` - main application logic
- `data/questions.json` - quiz questions and answers
- `README.md` - project instructions and overview

## Next Steps

Once the basic MVP works, you can extend it with features such as:
- timed questions
- difficulty levels
- a leaderboard
- persistent score history
- a graphical user interface
