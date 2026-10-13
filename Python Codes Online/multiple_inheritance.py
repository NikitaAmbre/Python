# III. Multiple Inheritance
# 1. Smart Device
# Create:
# MusicPlayer → play_music()
# Camera → take_photo()
# Create SmartDevice inheriting from both and demonstrate both features.

class MusicPlayer:
    def __init__(self,m_name,r_date):
        self.m_name=m_name
        self.r_date=r_date

    def play_music(self):
        print(f'song name is:{self.m_name},release date:{self.r_date}')

class Camera:
    def __init__(self,c_name):
        self.c_name=c_name

    def take_photo(self):
        print(f'camera name is : {self.c_name}')

class Device(MusicPlayer,Camera):
    def __init__(self, m_name, r_date,c_name,d_name):
        MusicPlayer.__init__(self,m_name, r_date)
        Camera.__init__(self,c_name)
        self.d_name=d_name

    def display(self):
        print(f'device name:{self.d_name}')

    def display_all(self):
        super().play_music()
        super().take_photo()
        print(f'device name:{self.d_name}')

d1=Device('safar','01-01-2026','Canon','Vivo')

d1.play_music()
print()
d1.take_photo()
print()
d1.display()
print()
d1.display_all()



        