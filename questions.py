
import random
from atw.difficulty import choose_wrong_countries


def generate_capital_question(countries, correct_country=None, difficulty="Easy"):
    if len(countries) < 10:
        raise ValueError("At least ten countries are required")

    if correct_country is None:
        correct_country = random.choice(countries)

    wrong_answers = choose_wrong_countries(
        countries, correct_country, difficulty
    )

    answers = [correct_country] + wrong_answers
    random.shuffle(answers)

    return {
        "question": f"What is the capital of {correct_country['country']}?",
        "options": [country["capital"] for country in answers],
        "correct_answer": correct_country["capital"],
        "correct_country": correct_country["country"],
        "option_countries": {
            country["capital"]: country["country"]
            for country in answers
        },
        "difficulty": difficulty
    }


def generate_quiz(countries, number_of_questions=10, difficulty="Easy", mode="Capitals"):
    if mode not in ["Capitals", "Flags"]:
        raise ValueError("Invalid quiz mode")

    if number_of_questions < 1:
        raise ValueError("Number of questions must be positive")

    if len(countries) < max(10, number_of_questions):
        raise ValueError("Not enough countries")

    selected_countries = random.sample(
        countries, number_of_questions
    )

    questions = []

    for country in selected_countries:
        if mode == "Capitals":
            question = generate_capital_question(
                countries, country, difficulty
            )
        else:
            question = generate_flag_question(
                countries, country, difficulty
            )

        questions.append(question)

    return questions

def generate_flag_question(countries, correct_country=None, difficulty="Easy"):
    if len(countries) < 10:
        raise ValueError("At least ten countries are required")

    if correct_country is None:
        correct_country = random.choice(countries)

    wrong_answers = choose_wrong_countries(
        countries, correct_country, difficulty
    )

    answers = [correct_country] + wrong_answers
    random.shuffle(answers)

    return {
        "question": "Which country does this flag belong to?",
        "flag": correct_country["flag"],
        "options": [country["country"] for country in answers],
        "correct_answer": correct_country["country"],
        "correct_country": correct_country["country"],
        "option_countries": {
            country["country"]: country["country"]
            for country in answers
        },
        "difficulty": difficulty,
        "type": "Flags"
    }
