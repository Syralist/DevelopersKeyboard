import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

FlankenMerker = 0

while True:
    Taster = GPIO.input(24)
    if not Taster == FlankenMerker:
        if Taster:
            print("pressed")
        else:
            print("released")
        FlankenMerker = Taster
