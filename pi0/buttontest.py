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

KeyStart = Button(15)
KeyStop = Button(16)
KeySelect = Button(1)
KeyStepOver = Button(6)
KeyStepInto = Button(10)
KeyStepOut = Button(11)
KeyRunToCursor = Button(26)
KeyRunSection = Button(27)
KeyRunAndAdvance = Button(28)
KeyEvaluateSelection = Button(29)

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