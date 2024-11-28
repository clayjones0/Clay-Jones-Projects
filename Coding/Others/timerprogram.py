import time
import pygame
from pygame import mixer

#python -m venv venv
#venv\Scripts\activate

dtime = int(1)

print("This is a timer")

print("Enter hours")
hours = int(input())

print("Enter minutes")
minutes = int(input())

print("Enter seconds")
seconds = int(input())

total = seconds + (60 * minutes) + (3600 * hours)

i = int(0)
while i <= total:

    print(i, "s")
    i = i + 1
    time.sleep(dtime)




if i-1 == total:
    print("Alarm!!!!!")
    pygame.init()
    alarm_sfx = pygame.mixer.Sound("mixkit-classic-alarm-995.wav")
    alarm_sfx.play()
    time.sleep(5)
    pygame.quit()
