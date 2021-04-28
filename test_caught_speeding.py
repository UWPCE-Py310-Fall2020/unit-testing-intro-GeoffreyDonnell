#!/usr/bin/env python

"""
test code for the walnut party example

Adapted from the "coding bat" site: https://codingbat.com/prob/p137202

When squirrels get together for a party, they like to have walnuts.
A squirrel party is successful when the number of walnuts is between
40 and 60, inclusive. Unless it is the weekend, in which case there
is no upper bound on the number of walnuts.

Return True if the party with the given values is successful,
or False otherwise.
"""


# you can change this import to test different versions
from caught_speeding import caught_speeding
# from walnut_party import walnut_party2 as walnut_party
# from walnut_party import walnut_party3 as walnut_party


def test_1():
    assert caught_speeding(60, False) is 0


def test_2():
    assert caught_speeding(65, False) is 1


def test_3():
    assert caught_speeding(65, True) is 0


def test_4():
    assert caught_speeding(80, False) is 1


def test_5():
    assert caught_speeding(85, False) is 2


def test_6():
    assert caught_speeding(85, True) is 1


def test_7():
    assert caught_speeding(70, False) is 1


def test_8():
    assert caught_speeding(75, False) is 1


def test_9():
    assert caught_speeding(75, True) is 1


def test_10():
    assert caught_speeding(40, False) is 0


def test_11():
    assert caught_speeding(40, True) is 0


def test_12():
    assert caught_speeding(90, False) is 2
