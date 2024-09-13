#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    key = ''
    if a_dictionary is None:
        return None
    else:
        for k, v in a_dictionary.items():
            if v > score:
                score = v
                key = k
    if score == 0:
        return None
    return key
