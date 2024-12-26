quiz=[
    {
        "question": "How is your mood today?",
        "options": ["1. Happy","2. Normal","3. Sad"]
    },
    {
        "question": "What kind of movie you like",
        "options": ["1. Comedy","2. Action","3. Comedy Romance"]
    },
    {
        "question": "Do you have any year preference",
        "options": ["1. No i Don't","2. Late 90s","3. Latest"]
    },
]
def display_question(question_data):

    print("\n" + question_data["question"])
    for option in question_data["options"]:
        print(option)

        while True:
            try:
                choice = int(input("Please Tell: "))
                if 1 <= choice <= len(question_data["options"]):
                    return choice
                else:
                    print("Please choose a valid option.")
            except ValueError:
                print("Invalid input! Please enter a number.")

def quiz1():
    print("Welcome to the Quiz!")
    user_answers = []
    for question_data in quiz:
        user_choice = display_question(question_data)
        user_answers.append(user_choice)
        print("\n here is movie for you bitch")


if __name__ == "__main__":
    quiz1()