from unit_generator import generate_unit, generate_quiz
from tutor_helper import ai_tutor_reply
from quiz import run_quiz

def main():
    topic = input("What topic should this unit cover?\n")
    unit = generate_unit(topic)
    lessons = unit["LESSON1CONTENT"]

    print(lessons)

if __name__ == "__main__":
    main()