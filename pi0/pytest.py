import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

FlankenMerker = 0

device = r"/dev/hidg0"
bNull = "0x00"
bModShift = "0x02"
bKeyA = "0x04"
bKeyZ = "0x1d"

bReleaseAll = bytes(int(x,0) for x in [bNull, bNull, bNull, bNull, bNull, bNull, bNull, bNull])
print(bReleaseAll)

bMod = bNull
bKey = bKeyZ
Test1 = bytes(int(x,0) for x in [bMod, bNull, bKey, bNull, bNull, bNull, bNull, bNull])
print(Test1)
bMod = bModShift
Test2 = bytes(int(x,0) for x in [bMod, bNull, bKey, bNull, bNull, bNull, bNull, bNull])
print(Test2)

def keyTest():
    with open(device, 'wb') as fp:
        fp.write(Test1)
        fp.write(bReleaseAll)
        fp.write(Test2)
        fp.write(bReleaseAll)

while True:
    Taster = GPIO.input(24)
    if not Taster == FlankenMerker:
        if Taster:
            print("pressed")
            keyTest()
        else:
            print("released")
        FlankenMerker = Taster
