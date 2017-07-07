from picamera import PiCamera
from time import sleep, strftime, localtime
import os

camera = PiCamera()

def takeSnap(filePath):
    camera.capture(os.path.join(filePath,strftime('%y%m%d-%H%M%S.jpeg',localtime())))
