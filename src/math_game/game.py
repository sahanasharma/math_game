def get_user_info():
    username = "sahana"
    grade = 1
    return {
        "username":"sahana",
        "grade":1

    }

def get_all_questions():
    with open("data/questions.txt", "r") as f:
        questions = f.read()
    questions = questions.split("\n")
    return questions



def main():
    answers = []
    user = get_user_info()
    questions = get_all_questions()
    for question in questions:
        answer = input(f"{question}: ")
        answers.append(answer)
    print(answers)

if __name__ == "__main__":
    main()