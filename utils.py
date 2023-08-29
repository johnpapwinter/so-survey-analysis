import pandas as pd
from collections import Counter


def calculate_percentages(answers_list: dict, total_respondents: int) -> dict:
    for key in answers_list:
        percentage = answers_list[key] * (100 / total_respondents)
        answers_list[key] = round(percentage, 2)

    return answers_list


def generate_answer_counter(dataframe, column_counting: str, total_respondents: int) -> dict:
    all_answers = ";".join(dataframe[column_counting].astype(str))
    all_answers = all_answers.split(";")
    all_counts = Counter(all_answers)

    return calculate_percentages(dict(all_counts), total_respondents)

