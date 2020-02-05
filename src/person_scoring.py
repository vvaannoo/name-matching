from time import time

from Levenshtein import jaro

from src.date_scoring import calculate_date_similarity
from src.name_scoring import calculate_name_similarity


def calculate_person_similarity(person_1, person_2):
    name_score = calculate_name_similarity(person_1[0], person_2[0])
    date_scores = calculate_date_similarity(person_1[1], person_2[1])
    bd_score = (date_scores[0] + date_scores[1] + date_scores[2]) / 3
    return (name_score + bd_score) / 2, name_score, date_scores


if __name__ == '__main__':
    start_time = time()
    person_1 = ('vano atabegashvilo', '1989-02-14')
    person_2 = ('ათაბეგაშვილი jemal', '1989-12-14')
    print(calculate_person_similarity(person_1, person_2))
    end_time = time()
    print(f'time: {end_time - start_time}')
