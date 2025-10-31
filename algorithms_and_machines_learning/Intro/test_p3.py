# Check if Symmetric

import pytest
from p3 import check_if_symmetric, convert_to_numbers, convert_to_letters, get_intersection, get_union, count_characters, is_prime

def test_palindromes():
    assert check_if_symmetric("radar") is True
    assert check_if_symmetric("noon") is True
    assert check_if_symmetric('!ab123 4 321ba!') is True

def test_non_palindromes():
    assert check_if_symmetric("hello") is False

def test_lton():
    assert convert_to_numbers("a cat") == [1,0,3,1,20]

def test_ntol():
    assert convert_to_letters([1,0,3,1,20]) == "a cat"

def test_intersect():
    assert get_intersection([1,1,1,2,3,5], [1,1,2,4,6]) == [1,2]

def test_union():
    assert get_union([1,1,1,2,3,4],[1,1,2,5,6]) == [1,2,3,4,5,6]

def test_countc():
    assert count_characters('A cat!!') == {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 2}

def test_prime():
    assert is_prime(79) == True
    assert is_prime(2) == True
