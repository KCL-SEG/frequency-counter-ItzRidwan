"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
"""['a', 'a', 'b', 'b', 'b', 'c']"""
from sre_compile import isstring


def frequencies(items):
    frequencies = {}
    for item in items:
        if type(item) != str:
            item = str(item)

        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies

frequencies([100, 'Hello', '100', '100', 100])