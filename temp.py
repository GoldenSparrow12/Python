from pygame import mixer
from datetime import datetime
from time import time


def playsong(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(1)
    mixer.music.play()
    while True:
        input_from_user = input().upper()
        if input_from_user == stopper:
            mixer.music.stop()
            break


def filesave(msg):
    with open("log.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    working_start = datetime(datetime.now().year,datetime.now().month,datetime.now().day,9)
    working_end = datetime(datetime.now().year,datetime.now().month,datetime.now().day,18)
    if working_start<datetime.now()<working_end:
        water_init = time()
        eye_init = time()
        ex_init = time()
        water_sec = 1 * 60
        eye_sec = 2 * 60
        ex_sec = 1.5 * 60
        while True:
            if time() - water_init > water_sec:
                print("Time to drank water.For stop write 'Drank'")
                playsong("Love You Oye.mp3", "DRANK")
                filesave("Drank Water at")
                water_init = time()
            if time() - eye_init > eye_sec:
                print("Time to eye rest.For stop write 'EyeDone'")
                playsong("Love You Oye.mp3", "EYEDONE")
                filesave("Rest Eyes at")
                eye_init = time()
            if time() - ex_init > ex_sec:
                print("Time To Exercise.For stop alarm enter 'ExDone'")
                playsong("Love You Oye.mp3", "EXDONE")
                filesave("Exercise done at")
                exercise_init = time()
    else:
        print("Not Working Hour")
