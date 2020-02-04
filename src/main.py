from time import time

from Levenshtein import jaro

from src.date_scoring import calculate_date_similarity
from src.name_scoring import calculate_name_similarity


def calculate_person_similarity(person_1, person_2):
    name_score = calculate_name_similarity(person_1[0], person_2[0])
    date_score = calculate_date_similarity(person_1[1], person_2[1])
    return name_score, date_score


if __name__ == '__main__':
    start_time = time()
    person_1 = ('vano atabegashvilo', '1989-02-14')
    person_2 = ('ათაბეგაშვილი jemal', '1989-12-14')
    print(calculate_person_similarity(person_1, person_2))
    end_time = time()
    print(f'time: {end_time - start_time}')
