import re

from Levenshtein import jaro


def parse_iso(date_string):
    if type(date_string) != str:
        raise TypeError(f'date is not string')
    if not re.match(r'\d{4}\W\d{2}\W\d{2}', date_string):
        raise ValueError(f'invalid date format ({date_string})')
    year = date_string[:4]
    month = date_string[5:7]
    day = date_string[8:]
    return year, month, day


def calculate_date_similarity(d1, d2, scorer=jaro):
    d1 = parse_iso(d1)
    d2 = parse_iso(d2)
    year_match = scorer(d1[0], d2[0])
    month_match = scorer(d1[1], d2[1])
    day_match = scorer(d1[2], d2[2])
    return year_match, month_match, day_match


if __name__ == '__main__':
    print(calculate_date_similarity('1989-02-14', '1999-02-14'))
