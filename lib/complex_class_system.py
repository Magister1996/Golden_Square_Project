from datetime import datetime

class Car():
    def __init__(self):
        self.tyre_dic = {}
    
    def add(self, object):
        self.tyre_dic[object] = {'Position':object.position,'Pressure':object.pressure,'Tread-depth':object.depth}
        

    def display(self):
        return self.tyre_dic.items()

class Tyre():
    def __init__(self, position, pressure, depth):
        self.position = position
        self.pressure = pressure
        self.depth = depth
        self.time = datetime.today().strftime("%Y-%m-%d")
        self.history_list = []
    
    def update(self, position, pressure, depth):
        date_time = self.time.strftime("%Y/%m/%d")
        self.history_list.append({'Position':self.position,'Pressure':self.pressure,'Tread-depth':self.depth,'Time':date_time})
        self.position = position
        self.pressure = pressure
        self.depth = depth
        self.time = datetime.today().strftime("%Y-%m-%d")