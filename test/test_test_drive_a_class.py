from lib.test_drive_a_class import *

def test_add():
    test_libary = MusicLibary()
    test_libary.add('Kesha','Tiktok')
    assert test_libary.song_list == [{'Artist':'Kesha','Song':'Tiktok'}]
    
def test_show():
    test_libary = MusicLibary()
    test_libary.add('Kesha','Tiktok')
    test_libary.add('Neyo','Miss Independent')
    test_libary.add('Justin Bieber','Baby')
    assert test_libary.show() == [{'Artist':'Kesha','Song':'Tiktok'}, {'Artist':'Neyo','Song':'Miss Independent'}, {'Artist':'Justin Bieber','Song':'Baby'}]