# 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

As a user
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"

Two classes, one containing the calender and one to create person objects.

Calender functions: add, update, nearest birthdays, upcoming age and card sent or not

# 2. Design the Function Signature

class Calender()
    def innit
        list = []

    def add(object)
        add object to list

    def update_date(name)
        update date in the list (call person update function)
        set sent birthday card to no

    def update name(old name)
        update the name in the list (call person update function)

    def nearest birthdays
        list comprehension of all the objects with a birthdate within the next 6 months

    def upcoming birthdays
        return a an int of the upcoming age of the person called

    def sent card 
        set sent card to done.


# 3. Create Examples as Tests

Give an object to the add function
assert the list contains a single item

Give an object to the class and run the update name function
assert the name change has happened

give an object to the class and run the update age function
assert the birthdate change has happened

give several objects to the class
assert the nearest birthday function returns the correct selection

give object to the class
assert that the upcoming age returns the objects current age plus 1

give an object to the class
assert the sent card function changes the varibale in the person object



# 4. Implement the Behaviour
