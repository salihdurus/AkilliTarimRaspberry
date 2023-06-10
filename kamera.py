from picamera import PiCamera,Color   #modülümüzü ekledik
import time

camera = PiCamera()  #kameramızı tanımladık
camera.start_preview()