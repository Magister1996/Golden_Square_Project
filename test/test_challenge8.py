from lib.challenge8 import *
from datetime import datetime

def test_add():
    calender = BirthdayCalender()
    subject = Person('Peter','2000/01/01')
    calender.add(subject)
    assert calender.person_list == [subject]

def test_update_name():
    calender = BirthdayCalender()
    subject = Person('Peter','2000/01/01')
    calender.add(subject)
    calender.update_name(subject, 'John')
    assert subject.name == 'John'

def test_update_birthday():
    calender = BirthdayCalender()
    subject = Person('Peter','2000/01/01')
    calender.add(subject)
    calender.update_birthday(subject, '1999/01/01')
    assert subject.birthday == datetime.strptime('1999/01/01', '%Y/%m/%d')

def test_near_birthdays():
    calender = BirthdayCalender()
    subject = Person('Peter', '2000/01/01')
    calender.add(subject)
    subject2 = Person('John', '2000/03/01')
    calender.add(subject2)
    subject3 = Person('Gregg', '2000/04/01')
    calender.add(subject3)
    assert calender.near_birthdays() == ['John', 'Gregg']

def test_appropriate_age():
    calender = BirthdayCalender()
    subject = Person('Peter','1996/10/21')
    calender.add(subject)
    assert calender.appropriate_age(subject) == 28
    subject2= Person('John','1966/09/27')
    calender.add(subject2)
    assert calender.appropriate_age(subject2) == 58
    subject3 = Person('Gregg','1976/11/17')
    calender.add(subject3)
    assert calender.appropriate_age(subject3) == 48

def test_birthday_card_send():
    calender = BirthdayCalender()
    subject = Person('Peter','1996/10/21')
    calender.add(subject)
    calender.birthday_card_send(subject)
    assert subject.card_send == 'Done'