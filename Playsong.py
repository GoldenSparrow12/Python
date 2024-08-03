from pygame import mixer

mixer.init()
mixer.music.load("Love You Oye.mp3")
mixer.music.set_volume(1)
mixer.music.play()
while True:
    print("Press P For Paush R for Restart ")
    print("Press Q for Quit")
    inr = input().upper()

    if inr == "P":
        mixer.music.pause()
    elif inr == "R":
        mixer.music.unpause()
    elif inr == "Q":
        mixer.music.stop()
        break
