
def check_answer(question, selected_answer, difficulty):
    points_by_difficulty = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }

    if difficulty not in points_by_difficulty:
        raise ValueError("Invalid difficulty level")

    if selected_answer not in question["options"]:
        raise ValueError("Invalid answer")

    is_correct = selected_answer == question["correct_answer"]
    max_points = points_by_difficulty[difficulty]
    points = max_points if is_correct else 0

    return {
        "correct_country": question["correct_country"],
        "selected_country": question["option_countries"][selected_answer],
        "correct_answer": question["correct_answer"],
        "selected_answer": selected_answer,
        "difficulty": difficulty,
        "is_correct": is_correct,
        "points": points,
        "max_points": max_points
    }


def calculate_results(results):
   
    if not results:
        raise ValueError("No answers to calculate")

    total_questions = len(results)
    correct_answers = sum(result["is_correct"] for result in results)
    total_points = sum(result["points"] for result in results)
    max_points = sum(result["max_points"] for result in results)

    accuracy = correct_answers / total_questions * 100

    return {
        "total_questions": total_questions,
        "correct_answers": correct_answers,
        "total_points": total_points,
        "max_points": max_points,
        "accuracy": round(accuracy, 1)
    }
