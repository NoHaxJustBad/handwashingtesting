import RPi.GPIO as GPIO
import time
import requests
import vlc
import random
GPIO.setmode(GPIO.BCM)
PIR_PIN = 17

GPIO.setup(PIR_PIN, GPIO.IN)
video = '/home/pi/Videos/handwashingvideotimer.mp4'
print("Setup complete...")
print("Starting script")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected")
            x+=1
            y=0
            if x==30:
                media_player = vlc.MediaPlayer()
                media = vlc.Media(video)
			    media_player.set_media(media)
                media_player.toggle_fullscreen()
                media_player.play()
			    # Record new previous state
			    previousstate = 1
			    #Wait 120 seconds before looping again
		    	print("Waiting 30 seconds")
                media_player.stop()

        else:
            print("no motion detected")
            x=0
            y+=1
            if y=50:
                media_player.stop()
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Quitting")
    GPIO.cleanup()
