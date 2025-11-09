from unit_generator import generate_unit, generate_quiz
from tutor_helper import ai_tutor_reply
from quiz import run_quiz

def main():
    topic = input("What topic should this unit cover?\n")
    unit = generate_unit(topic, model="gpt-4o")
    lessons = unit["LESSON1CONTENT"]
    # coins = run_quiz(lessons)

    last_question = lessons[-1]["QUESTIONS"][-1]
    user_answer = input("What was your previous answer")
    #TODO: Fix AI tutor reply
    tutor_resp = ai_tutor_reply(
        question=f'{last_question["QUESTION"]} (options: {last_question["OPTIONS"]})',
        context=f'Correct answer is {last_question["CORRECT_ANSWER"]}, user answered {user_answer}',
    )
    print(tutor_resp)


if __name__ == "__main__":
    main()