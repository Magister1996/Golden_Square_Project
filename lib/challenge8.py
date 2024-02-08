from datetime import datetime, date, timedelta


class BirthdayCalender():
    def __init__(self):
        self.person_list = []
        
    def add(self, person):
        self.person_list.append(person)
    
    def update_name(self,person,name):
        person.name = name

    def update_birthday(self,person,date):
        person.birthday = datetime.strptime(date, '%Y/%m/%d')
        person.card_send = 'Not done'

    def near_birthdays(self):
        current_time = datetime.now()
        answer = [person.name for person in self.person_list if current_time.month <= person.birthday.month <= current_time.month + 6]
        return answer

    def appropriate_age(self, person):
        number = date.today() - person.birthday.date()
        return (round(number.days/ 365)+ 1)
    
    def birthday_card_send(self,person):
        person.card_send = 'Done'

class Person():
    def __init__(self,name,birthday):
        self.birthday = datetime.strptime(birthday, '%Y/%m/%d')
        self.card_send = 'Not done'
        self.name = name


