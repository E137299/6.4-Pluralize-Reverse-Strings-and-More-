from main import *

def test_pluralize():
    assert pluralize(["apple", "berry", "melon"]) == ["apples", "berries", "melons"]
    assert pluralize(["sky","rainbow","fairy"]) == ["skies","rainbows","fairies"]

def test_reverse_strings():
    assert reverse_strings(["apple", "berry", "melon"]) == ["elppa", "yrreb", "nolem"]
    assert reverse_strings(["tacocat", "madam", "rotator"]) == ["tacocat", "madam", "rotator"]

def test_remove_duplicates():
    assert remove_duplicates(["apple", "berry","apple", "melon", "melon", "apple"]) == ["apple", "berry", "melon"]
    assert remove_duplicates([2,4,5,2,6,7,5]) == [2,4,5,6,7]

def test_shared_items():
    assert shared_items([9,3,6,3,6,8,7,2],[0,2,7,2]) == False
    assert shared_items([9,3,6,3,6,8,7,2],[3,2,7,2]) == True
    