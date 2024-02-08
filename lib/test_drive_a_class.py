class MusicLibary():
    def __init__(self):
        self.song_list = []
    
    def add(self,Artist,Song):
        self.song_list.append({'Artist':Artist,'Song':Song})
    
    def show(self):
        return self.song_list
    