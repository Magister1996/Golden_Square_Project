from lib.most_often import *

def test_add_new():
    subject = MostOften([1,1,1,2,3,3,4])
    subject.add_new(5) 
    assert subject.starting_list == [1,1,1,2,3,3,4,5]

def test_most_often_clear_winner():
    subject = MostOften([1,1,1,2,3,3,4])
    assert subject.get_most_often() == 1

def test_most_often_no_clear_winner():
    subject = MostOften([1,1,1,2,3,3,3,4])
    assert subject.get_most_often() == 'no clear winner'



