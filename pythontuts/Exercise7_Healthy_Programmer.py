#Healthy Programmer
# 9am-5pm
# Water-water.mp3 (3.5 litres)-Drank-Log
# Eyes-eyes.mp3-every 30 min -EyDone-Log
# Physical activity-physical.mp3 every-45 min-ExDone-Log
# pygame module to play audio
# from python_play.player import play_it
# import time
#
# while(time.localtime):
#     play_it("/Users/Admin/PycharmProject/pythontuts/water.mp3.mp3")

from pygame import mixer
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a== stopper:
            mixer.music.stop()
            break

if __name__ == '__main__':
    musiconloop("water.mp3.mp3","stop")



