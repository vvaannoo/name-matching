import operator
from time import time

from Levenshtein import jaro_winkler

from src.normalizer import normalize_and_tokenize


def calculate_tokens_similarity(tokens_1, tokens_2, scorer):
    x = [(scorer(a, b), a, b) for a in tokens_1 for b in tokens_2]
    x.sort(key=operator.itemgetter(0), reverse=True)
    set_1, set_2 = set(), set()
    # print(x)
    matches = []
    for score, token_1, token_2 in x:
        if token_1 not in set_1 and token_2 not in set_2:
            matches.append((score, token_1, token_2))
            set_1.add(token_1)
            set_2.add(token_2)
    avg_score = sum([score for score, _, _ in matches]) / ((len(tokens_1) + len(tokens_2)) / 2)
    print(f'score: {avg_score:.4f}, matches: {matches}')
    return avg_score


def concat_random(tokens):
    sets = []
    for token_1 in tokens:
        for token_2 in tokens:
            if token_1 != token_2:
                st = tokens.copy()
                st.remove(token_1)
                st.remove(token_2)
                st.add(token_1 + token_2)
                sets.append(st)
    return sets


def calculate_name_similarity(s1, s2, scorer=jaro_winkler):
    s1 = normalize_and_tokenize(s1)
    s2 = normalize_and_tokenize(s2)

    tokens_list_1 = [s1] #+ concat_random(s1)
    tokens_list_2 = [s2] #+ concat_random(s2)

    max_score = 0
    for tokens_1 in tokens_list_1:
        for tokens_2 in tokens_list_2:
            score = calculate_tokens_similarity(tokens_1, tokens_2, scorer)
            if score > max_score:
                max_score = score
            if max_score == 1:
                break
        if max_score == 1:
            break
    return max_score


if __name__ == '__main__':
    start_time = time()
    score = calculate_name_similarity('FUCHS OR', 'PINTO OR')
    print(f'max score: {score}')
    end_time = time()
    print(f'time: {end_time - start_time}')