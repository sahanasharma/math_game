import csv


def get_user_info():
    username = "sahana"
    grade = 1
    return {
        "username":"sahana",
        "grade":1

    }

def get_all_questions():
    with open("data/questions.csv", "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def main():
    grade = input("What is your grade: ")
    answers = []
    user = get_user_info()
    questions = get_all_questions()

    for qg in questions:
        if qg["grade"] != grade:
            continue
        answer = input(f'{qg["question"]}: ')
        answers.append(answer)
    print(answers)

if __name__ == "__main__":
    main()