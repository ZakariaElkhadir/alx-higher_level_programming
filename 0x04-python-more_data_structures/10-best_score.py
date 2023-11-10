#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mval = 0
    mkey = None
    for x, s in a_dictionary.items():
        if s > mval:
            mval = s
            mkey = x
    return mkey
