from lib.high_value import *

def test_get_highest_first():
    subject = HighValue(8, 7)
    assert subject.get_highest() == 'First value is higher'
def test_get_highest_second():
    subject = HighValue(7, 8)
    assert subject.get_highest() == 'Second value is higher'
def test_get_highest_equal():
    subject = HighValue(8, 8)
    assert subject.get_highest() == 'Values are equal'
def test_add():
    subject = HighValue(4, 6)
    assert subject.get_highest() == 'Second value is higher'
    subject.add(10, 'first')
    assert subject.value_first == 14
    subject.add(5, 'second')
    assert subject.value_second == 11
    assert subject.get_highest() == 'First value is higher'
