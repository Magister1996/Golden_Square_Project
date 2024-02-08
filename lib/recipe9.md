# 1. Describe the Problem

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were

Two clases: Car and Tyres

Tyre class needed position, pressure, tread depth and history

a list to hold history: key = date and value is old info

update funciton to change information and update dictionary

Car class nested dictionary key = object value = info

a display function to show all the information

# 2. Design the Function Signature

class Car()
    def __init__(self)
        dicitonary of dictionaries

    def add(self, object)
        add dicionary of tire and current info to parent dic

    def display(self)
        displays current tyres and most up to date readings.

class Tyre()
    def __init__(self, position, pressure, depth):
        self.position
        self.pressure
        self.depth
        self.time
        self.history_list = []
    
    def update(position, pressure and depth)
        List is updated with a dicionary of old info and time
        self variables are updated

# 3. Create Examples as Tests

def add
When a dic is added, assert dic is present in parent dic

def display
Add several dics, assert all are returned from functions

Tyre init
assert all the tyre values are as inputted

tyre update
assert all new values are present

tyre history
return a list of old values

# 4. Implement the Behaviour
