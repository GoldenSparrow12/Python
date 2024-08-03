# from time import *
# start=time()
# for i in range(10):
#         print(i)
# print (time()-start)
# local =asctime(localtime(time()))
# print(local)
# lis =["harshit","jay","hau","hhdhdh","jajuw","hsdj"]
# print (" is ".join(lis))
from pygame import mixer
mixer.init()
mixer.music.load ("Love You Oye.mp3")
mixer.music.set_volume(1)
mixer.music.play()
print ("Press P for Push and a for restart Q for Quit")
inr = input()
while(True):
    if inr=="P":
        mixer.music.pause()
    elif inr =="a":
        mixer.music.unpause()
    elif inr =="q":
        mixer.music.stop()
        break