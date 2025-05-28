import pytest

from data_structures_algos.arrays.binary_search import binary_search, r_binary_search

def test_01_binary_search():
    arr01 = [-10, -5, -4, -1, 0, 2, 6, 8, 12, 22, 30]
    target = 6
    assert binary_search(arr=arr01, num=target) == 6
    assert r_binary_search(arr=arr01, num=target) == 6
    
def test_02_binary_search():
    arr02 = [-30, -25, -24, -21, -15, -11, -6, -2, 0, 2, 6, 8, 12, 22, 30, 31, 32, 33, 38, 42]
    target = 6
    assert binary_search(arr=arr02, num=target) == 10
    assert r_binary_search(arr=arr02, num=target) == 10
    
def test_03_binary_search():
    arr03 = [-1,0,3,5,9,12]
    target = 9
    assert binary_search(arr=arr03, num=target) == 4
    assert r_binary_search(arr=arr03, num=target) == 4
    
def test_04_binary_search():
    arr04 = [5]
    target = 5
    assert binary_search(arr=arr04, num=target) == 0
    assert r_binary_search(arr=arr04, num=target) == 0
    
def test_05_binary_search():
    arr04 = [5]
    target = -5
    assert binary_search(arr=arr04, num=target) == -1
    assert r_binary_search(arr=arr04, num=target) == -1
    
def test_06_binary_search():
    arr04 = [-1, 0, 5]
    target = 5
    assert binary_search(arr=arr04, num=target) == 2
    assert r_binary_search(arr=arr04, num=target) == 2