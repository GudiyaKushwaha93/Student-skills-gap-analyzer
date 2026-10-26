import matplotlib.pyplot as plt

print("=" * 45)
print("     STUDENT SKILL GAP ANALYZER")
print("=" * 45)

student_name = input("Enter your name: ")
target_job = input("Enter your target job (e.g. Data Analyst): ")
quiz = {
    "Excel": [
        ("Which function adds numbers?",
         ["A. COUNT", "B. SUM", "C. MAX", "D. TEXT"], "B"),
        ("Which symbol starts an Excel formula?",
         ["A. #", "B. @", "C. =", "D. &"], "C"),
        ("Which function finds the average?",
         ["A. AVERAGE", "B. TOTAL", "C. ADD", "D. MEANING"], "A"),
        ("What is a PivotTable used for?",
         ["A. Drawing pictures", "B. Summarizing data",
          "C. Playing videos", "D. Writing code"], "B")
    ],

    "Python": [
        ("Which function displays output?",
         ["A. input()", "B. print()", "C. type()", "D. range()"], "B"),
        ("Which data type stores True or False?",
         ["A. str", "B. int", "C. bool", "D. list"], "C"),
        ("Which brackets create a Python list?",
         ["A. [ ]", "B. { }", "C. ( )", "D. < >"], "A"),
        ("Which keyword is used for a condition?",
         ["A. repeat", "B. check", "C. if", "D. print"], "C")
    ],

    "SQL": [
        ("Which command retrieves data?",
         ["A. SELECT", "B. DELETE", "C. DROP", "D. UPDATE"], "A"),
        ("Which clause filters rows?",
         ["A. ORDER BY", "B. WHERE", "C. GROUP BY", "D. FROM"], "B"),
        ("Which command adds a new row?",
         ["A. INSERT INTO", "B. SELECT", "C. REMOVE", "D. FETCH"], "A"),
        ("Which function counts rows?",
         ["A. SUM()", "B. AVG()", "C. COUNT()", "D. ROUND()"], "C")
    ],

    "Power BI": [
        ("What is Power BI mainly used for?",
         ["A. Video editing", "B. Data visualization",
          "C. Gaming", "D. Typing documents"], "B"),
        ("What is a dashboard used for?",
         ["A. Displaying key information",
          "B. Installing Python", "C. Writing emails",
          "D. Creating folders"], "A"),
        ("Which view is used to create relationships between tables?",
         ["A. Report view", "B. Model view",
          "C. Reading view", "D. Print view"], "B"),
        ("Which language is used for measures in Power BI?",
         ["A. HTML", "B. CSS", "C. DAX", "D. Java"], "C")
    ]
}

scores = {}
total_questions = 0
total_correct = 0

# Ask questions and calculate scores
for skill, questions in quiz.items():
    print("\n" + "=" * 35)
    print("SKILL TEST:", skill)
    print("=" * 35)

    correct = 0

    for number, question_data in enumerate(questions, start=1):
        question, options, answer = question_data

        print(f"\nQ{number}. {question}")
        for option in options:
            print(option)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        while user_answer not in ["A", "B", "C", "D"]:
            print("Please enter only A, B, C or D.")
            user_answer = input("Your answer: ").strip().upper()
            
        if user_answer == answer:
            print("Correct answer!")
            correct += 1
        else:
            print("Wrong answer. Correct option:", answer)

        explanations = {
            "Which function adds numbers?":
                "SUM() is used to add numbers.",
            "Which symbol starts an Excel formula?":
                "The equals sign (=) starts an Excel formula.",
            "Which function finds the average?":
                "AVERAGE() calculates the average of numbers.",
            "What is a PivotTable used for?":
                "A PivotTable summarizes and analyzes data.",
            "Which function displays output?":
                "print() displays output on the screen.",
            "Which data type stores True or False?":
                "The bool data type stores True or False values.",
            "Which brackets create a Python list?":
                "Square brackets [ ] are used to create a Python list.",
            "Which keyword is used for a condition?":
                "The if keyword is used to check a condition.",
            "Which command retrieves data?":
                "SELECT retrieves data from a database.",
            "Which clause filters rows?":
                "WHERE filters rows based on a condition.",
            "Which command adds a new row?":
                "INSERT INTO adds a new row to a database table.",
            "Which function counts rows?":
                "COUNT() counts rows or values.",
            "What is Power BI mainly used for?":
                "Power BI is used for data visualization and reporting.",
            "What is a dashboard used for?":
                "A dashboard displays important information in one place.",
            "Which view is used to create relationships between tables?":
                "Model view is used to manage relationships between tables.",
            "Which language is used for measures in Power BI?":
                "DAX is used to create calculations and measures in Power BI."
        }

        print("Explanation:", explanations[question])
    scores[skill] = correct
    total_correct += correct
    total_questions += len(questions)

# Calculate percentage
overall_percentage = (total_correct / total_questions) * 100
print("\n===== SKILL GAP ANALYSIS =====")

weakest_skill = min(
    quiz,
    key=lambda skill: scores[skill] / len(quiz[skill])
)

weakest_score = scores[weakest_skill]
weakest_total = len(quiz[weakest_skill])
weakest_percentage = (weakest_score / weakest_total) * 100

print("Your weakest skill is:", weakest_skill)
print(f"Your score: {weakest_score}/{weakest_total}")
print(f"Your percentage: {weakest_percentage:.1f}%")

print("\n===== RECOMMENDATION =====")
print("Focus on improving", weakest_skill)
print("Practice more questions and complete a small project in this skill.")
print("\n===== SKILL-WISE PERFORMANCE =====")

for skill in quiz:
    total_questions_skill = len(quiz[skill])
    percentage = (scores[skill] / total_questions_skill) * 100

    if percentage < 40:
        level = "Beginner"
    elif percentage < 70:
        level = "Intermediate"
    else:
        level = "Good"

    print(f"\n{skill}")
    print(f"Score: {scores[skill]}/{total_questions_skill}")
    print(f"Percentage: {percentage:.1f}%")
    print(f"Performance Level: {level}")

print("\n" + "=" * 45)
print("          FINAL SKILL REPORT")
print("=" * 45)
print("Student:", student_name)
print("Target Job:", target_job)

print("\nSKILL-WISE RESULTS")

for skill, score in scores.items():
    percentage = (score / len(quiz[skill])) * 100
    print(f"{skill}: {score}/{len(quiz[skill])} ({percentage:.0f}%)")

print(f"\nTotal Score: {total_correct}/{total_questions}")
print(f"Overall Accuracy: {overall_percentage:.1f}%")

if overall_percentage >= 80:
      print("Overall Performance: Excellent")
elif overall_percentage >= 60:
    print("Overall Performance: Good")
elif overall_percentage >= 40:
    print("Overall Performance: Average")
else:
    print("Overall Performance: Needs Improvement")

print("\nPERSONALIZED LEARNING PLAN")

learning_plan = {
    "Excel": [
        "Practise SUM, AVERAGE and COUNT functions.",
        "Learn sorting, filtering and PivotTables."
    ],
    "Python": [
        "Practise variables, data types and if-else.",
        "Learn loops, lists and functions."
    ],
    "SQL": [
        "Practise SELECT, WHERE and ORDER BY.",
        "Learn GROUP BY, aggregate functions and JOIN."
    ],
    "Power BI": [
        "Practise creating charts and dashboards.",
        "Learn data relationships and DAX measures."
    ]
}

for skill, score in scores.items():
    percentage = (score / len(quiz[skill])) * 100

    print(f"\n{skill}: {percentage:.0f}%")

    if percentage < 60:
        print("Status: Needs improvement")
        print("Recommended topics:")

        for topic in learning_plan[skill]:
            print("-", topic)

    elif percentage < 80:
        print("Status: Good - practise advanced topics.")

    else:
        print("Status: Strong - keep practising!")

# Create bar graph
skills = list(scores.keys())
ratings = [
    (scores[skill] / len(quiz[skill])) * 100
    for skill in skills
]

plt.figure(figsize=(8, 5))
bars = plt.bar(skills, ratings)

plt.title("Student Skill Gap Analysis")
plt.xlabel("Skills")
plt.ylabel("Quiz Score (%)")
plt.ylim(0, 110)
plt.xticks(rotation=15)

for bar, rating in zip(bars, ratings):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        rating + 2,
        f"{rating:.0f}%",
        ha="center"
    )

plt.tight_layout()
plt.show()
import csv
import os

file_name = "student_skill_results.csv"
file_exists = os.path.isfile(file_name)

with open(file_name, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Student Name",
            "Target Job",
            "Excel Score",
            "Python Score",
            "SQL Score",
            "Power BI Score",
            "Overall Percentage"
        ])

    writer.writerow([
        student_name,
        target_job,
        f"{scores['Excel']}/{len(quiz['Excel'])}",
        f"{scores['Python']}/{len(quiz['Python'])}",
        f"{scores['SQL']}/{len(quiz['SQL'])}",
        f"{scores['Power BI']}/{len(quiz['Power BI'])}",
        f"{overall_percentage:.1f}%"
    ])

print("\nYour result has been saved to", file_name)

