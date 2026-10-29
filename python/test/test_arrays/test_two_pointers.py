import pytest

from ..constants import LONG_STRING

from data_structures_algos.arrays.two_pointers_pattern import valid_palindrome

def test_valid_palindrome_01():
    assert valid_palindrome(s="This is a sentence, that has: punctuation!") == False

def test_valid_palindrome_02():
    assert valid_palindrome(s="A man, a plan, a canal: Panama") == True

def test_valid_palindrome_03():
    assert valid_palindrome(s="pp") == True

def test_valid_palindrome_04():
    assert valid_palindrome(s="mp") == False

def test_valid_palindrome_05():
    assert valid_palindrome(s="s") == True

def test_valid_palindrome_06():
    assert valid_palindrome(s="") == False

def test_valid_palindrome_07():
    assert valid_palindrome("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod") == True
