from lib.make_and_test_drive_a_function import *

def test_sort_list():
    assert sort_list(['first_task#TODO', 'second_task#TODO', 'third_task#completed', 'fourth_task#completed']) == ['first_task#TODO', 'second_task#TODO']
    assert sort_list(['first_task#completed', 'second_task#completed', 'third_task#completed', 'fourth_task#completed']) == []
    assert sort_list(['first_task#TODO', 'second_task#TODO', 'third_task#TODO', 'fourth_task#TODO']) == ['first_task#TODO', 'second_task#TODO', 'third_task#TODO', 'fourth_task#TODO']