import pytest

from ..constants import LONG_STRING

from data_structures_algos.arrays.sliding_window_pattern import longest_substring_without_repeats

def test_longest_substring_without_repeats_01():
    assert longest_substring_without_repeats(s="abcabcbb") == 3

def test_longest_substring_without_repeats_02():
    assert longest_substring_without_repeats(s="bbbbb") == 1

def test_longest_substring_without_repeats_03():
    assert longest_substring_without_repeats(s="pwwkew") == 3

def test_longest_substring_without_repeats_04():
    assert longest_substring_without_repeats(s="pp") == 1

def test_longest_substring_without_repeats_05():
    assert longest_substring_without_repeats(s="mp") == 2

def test_longest_substring_without_repeats_06():
    assert longest_substring_without_repeats(s="s") == 1

def test_longest_substring_without_repeats_07():
    assert longest_substring_without_repeats(s="") == 0

def test_longest_substring_without_repeats_08():
    assert longest_substring_without_repeats(s=LONG_STRING) == 95