#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first = None
    if length > 0:
        first = sentence[0]
    tuple_result = (length, first)
    return (tuple_result)
