class Camera:

    def take_photo(self):
        print("Photo Captured")


class MusicPlayer:

    def play_music(self):
        print("Playing Music")


class SmartPhone(Camera, MusicPlayer):
    pass


phone = SmartPhone()

phone.take_photo()
phone.play_music()