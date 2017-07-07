from picamera import PiCamera
from time import sleep, strftime, localtime
import os

camera = PiCamera

def takeSnap(filePath):
    camera.start_preview()
    sleep(5)
    camera.capture(os.path.join(filePath,strftime(localtime)))
    camera.stop_preview()