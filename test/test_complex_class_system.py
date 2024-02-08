from lib.complex_class_system import *
from datetime import datetime

def test_car_test_add():
    volvo = Car()
    tyre1 = Tyre('Front-Left','32psi', '20mm')
    volvo.add(tyre1)
    assert volvo.tyre_dic == {tyre1 : {'Position':'Front-Left','Pressure':'32psi','Tread-depth':'20mm'}}

def test_car_test_display():    
    volvo = Car()
    tyre1 = Tyre('Front-Left','32psi', '20mm')
    volvo.add(tyre1)
    tyre2 = Tyre('Front-Right','31psi', '15mm')
    volvo.add(tyre2)
    tyre3 = Tyre('Back-Left','30psi', '16mm')
    volvo.add(tyre3)
    tyre4 = Tyre('Back-Right','30psi', '17mm')
    volvo.add(tyre4)
    assert volvo.tyre_dic == {tyre1 : {'Position':'Front-Left','Pressure':'32psi','Tread-depth':'20mm'}, tyre2 : {'Position':'Front-Right','Pressure':'31psi','Tread-depth':'15mm'}, tyre3 : {'Position':'Back-Left','Pressure':'30psi','Tread-depth':'16mm'}, tyre4 : {'Position':'Back-Right','Pressure':'30psi','Tread-depth':'17mm'}}

def test_tyre_test_init():
    tyre1 = Tyre('Front-Left','32psi', '20mm')
    assert tyre1.position == 'Front-Left'
    assert tyre1.pressure == '32psi'
    assert tyre1.depth == '20mm'
    assert tyre1.time == datetime.today().strftime("%Y-%m-%d")

def test_tyre_update():
    tyre1 = Tyre('Front-Left','32psi', '20mm')
    tyre1.time = datetime.strptime('2023/10/23','%Y/%m/%d')
    tyre1.update('Front-Left','28psi','16mm')
    assert tyre1.position == 'Front-Left'
    assert tyre1.pressure == '28psi'
    assert tyre1.depth == '16mm'
    assert tyre1.time == datetime.today().strftime("%Y-%m-%d")

def test_tyre_history():
    tyre1 = Tyre('Front-Left','32psi', '20mm')
    tyre1.time = datetime.strptime('2023/10/23','%Y/%m/%d')
    tyre1.update('Front-Left','28psi','16mm')
    assert tyre1.history_list == [{'Position':'Front-Left','Pressure':'32psi','Tread-depth':'20mm','Time':'2023/10/23'}]
    tyre1.time = datetime.strptime('2023/12/31','%Y/%m/%d')
    tyre1.update('Front-Left','25psi','13mm')
    assert tyre1.history_list == [{'Position':'Front-Left','Pressure':'32psi','Tread-depth':'20mm','Time':'2023/10/23'},{'Position':'Front-Left','Pressure':'28psi','Tread-depth':'16mm','Time':'2023/12/31'}]
