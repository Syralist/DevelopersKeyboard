from gpiozero import Button
from signal import pause

def PressedKeyStart():
    print("Start")
def PressedKeyStop():
    print("Stop")
def PressedKeySelect():
    print("Select")
def PressedKeyStepOver():
    print("StepOver")
def PressedKeyStepInto():
    print("StepInto")
def PressedKeyStepOut():
    print("StepOut")
def PressedKeyRunToCursor():
    print("RunToCursor")
def PressedKeyRunSection():
    print("RunSection")
def PressedKeyRunAndAdvance():
    print("RunAndAdvance")
def PressedKeyEvaluateSelection():
    print("EvaluateSelection")

KeyStart = Button(14)
KeyStop = Button(15)
KeySelect = Button(1)
KeyStepOver = Button(25)
KeyStepInto = Button(8)
KeyStepOut = Button(7)
KeyRunToCursor = Button(12)
KeyRunSection = Button(16)
KeyRunAndAdvance = Button(20)
KeyEvaluateSelection = Button(21)

KeyStart.when_pressed = PressedKeyStart
KeyStop.when_pressed = PressedKeyStop
KeySelect.when_pressed = PressedKeySelect
KeyStepOver.when_pressed = PressedKeyStepOver
KeyStepInto.when_pressed = PressedKeyStepInto
KeyStepOut.when_pressed = PressedKeyStepOut
KeyRunToCursor.when_pressed = PressedKeyRunToCursor
KeyRunSection.when_pressed = PressedKeyRunSection
KeyRunAndAdvance.when_pressed = PressedKeyRunAndAdvance
KeyEvaluateSelection.when_pressed = PressedKeyEvaluateSelection

pause()
