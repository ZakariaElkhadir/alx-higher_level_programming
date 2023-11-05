#!/usr/bin/python3
def multiple_returns(sentens):
    lsentens = len(sentens)
    if lsentens == 0:
        ntuple = (lsentens, None)
    ntuple = (lsentens, sentens[0])
    return ntuple
