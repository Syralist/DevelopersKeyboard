from gpiozero import Button
from signal import pause

from sendkeys import KeycodeSender

from Adafruit_SSD1306 import SSD1306_128_64 as OLED
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Display():
    def __init__(self):
        self.Display = OLED(rst=24, i2c_address=0x3C)
        self.Display.begin()
        self.Display.clear()
        self.Display.display()

        self.width = self.Display.width
        self.height = self.Display.height
        self.Image = Image.new('1', (self.width, self.height))
        self.ImageDraw = ImageDraw.Draw(self.Image)

        self.IconTop = 33
        self.IconLeft = 2
        self.Icons = {}
        self.Icons['Run'] = Image.open('Run.bmp').convert('1')
        self.Icons['Stop'] = Image.open('Stop.bmp').convert('1')
        self.Icons['StepOver'] = Image.open('StepOver.bmp').convert('1')
        self.Icons['StepInto'] = Image.open('StepInto.bmp').convert('1')
        self.Icons['StepOut'] = Image.open('StepOut.bmp').convert('1')
        self.Icons['RunToCursor'] = Image.open('RunToCursor.bmp').convert('1')
        self.Icons['RunSection'] = Image.open('RunSection.bmp').convert('1')
        self.Icons['RunAndAdvance'] = Image.open('RunAndAdvance.bmp').convert('1')
        self.Icons['EvaluateSelection'] = Image.open('EvaluateSelection.bmp').convert('1')

        self.Font = ImageFont.load_default()
        self.Font = ImageFont.truetype('FreeMono.ttf', 16)
        self.FunctionNameTop = 33
        self.FunctionNameLeft = 2 + 30 + 4
        self.FunctionNames = {}
        self.FunctionNames['Run'] = 'Run'
        self.FunctionNames['Stop'] = 'Stop'
        self.FunctionNames['StepOver'] = 'Step Over'
        self.FunctionNames['StepInto'] = 'Step Into'
        self.FunctionNames['StepOut'] = 'Step Out'
        self.FunctionNames['RunToCursor'] = 'R To Cursor'
        self.FunctionNames['RunSection'] = 'R Section'
        self.FunctionNames['RunAndAdvance'] = 'R + Advance'
        self.FunctionNames['EvaluateSelection'] = 'Eval Selec'

        self.ShortcutTop = 33 + 15
        self.ShortcutLeft = 2 + 30 + 4

    def SetProgramm(self, name):
        self.ImageDraw.line([0, 27, self.width, 27], fill=255, width=1)
        self.ImageDraw.text((2, 2), name, font=self.Font, fill=255)

    def SetIcon(self, icon):
        self.Image.paste(self.Icons[icon], (self.IconLeft, self.IconTop))
    
    def SetFunctionName(self, name):
        self.ImageDraw.rectangle([self.FunctionNameLeft, self.FunctionNameTop, self.width, self.height-15], fill=0, outline=0)
        self.ImageDraw.text((self.FunctionNameLeft, self.FunctionNameTop), self.FunctionNames[name],  font=self.Font, fill=255)
    
    def SetShortcut(self, Text):
        self.ImageDraw.rectangle([self.ShortcutLeft, self.ShortcutTop, self.width, self.height], fill=0, outline=0)
        self.ImageDraw.text((self.ShortcutLeft, self.ShortcutTop), Text,  font=self.Font, fill=255)

    def UpdateScreen(self):
        self.Display.clear()
        self.Display.image(self.Image)
        self.Display.display()

class DevKeys():
    def __init__(self, display, keycodesender):
        self.Display = display
        
        self.KeycodeSender = keycodesender

        self.Programms = list(Shortcuts.keys())
        self.ProgrammIndex = 0

        self.Display.SetProgramm(self.Programms[self.ProgrammIndex])
        self.Display.UpdateScreen()

        self.KeyRun = Button(14)
        self.KeyStop = Button(15)
        self.KeySelect = Button(1)
        self.KeyStepOver = Button(25)
        self.KeyStepInto = Button(8)
        self.KeyStepOut = Button(7)
        self.KeyRunToCursor = Button(12)
        self.KeyRunSection = Button(16)
        self.KeyRunAndAdvance = Button(20)
        self.KeyEvaluateSelection = Button(21)

        self.KeyRun.when_pressed = self.PressedKeyRun
        self.KeyStop.when_pressed = self.PressedKeyStop
        self.KeySelect.when_pressed = self.PressedKeySelect
        self.KeyStepOver.when_pressed = self.PressedKeyStepOver
        self.KeyStepInto.when_pressed = self.PressedKeyStepInto
        self.KeyStepOut.when_pressed = self.PressedKeyStepOut
        self.KeyRunToCursor.when_pressed = self.PressedKeyRunToCursor
        self.KeyRunSection.when_pressed = self.PressedKeyRunSection
        self.KeyRunAndAdvance.when_pressed = self.PressedKeyRunAndAdvance
        self.KeyEvaluateSelection.when_pressed = self.PressedKeyEvaluateSelection


    def PressedKeyRun(self):
        print("Run")
        (Text, IsSpecialKey, Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin) = Shortcuts[self.Programms[self.ProgrammIndex]]["Run"]
        self.Display.SetIcon("Run")
        self.Display.SetFunctionName("Run")
        self.Display.SetShortcut(Text)
        self.Display.UpdateScreen()
        if IsSpecialKey:
            self.KeycodeSender.sendSpecialKey(Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin)
        else:
            self.KeycodeSender.sendPrintable(Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin)

    def PressedKeyStop(self):
        print("Stop")
        self.Display.SetIcon("Stop")
        self.Display.SetFunctionName("Stop")
        self.Display.UpdateScreen()

    def PressedKeySelect(self):
        print("Select")
        # self.Display.SetIcon("Run")
        # self.Display.UpdateScreen()

    def PressedKeyStepOver(self):
        print("StepOver")
        self.Display.SetIcon("StepOver")
        self.Display.SetFunctionName("StepOver")
        self.Display.UpdateScreen()

    def PressedKeyStepInto(self):
        print("StepInto")
        self.Display.SetIcon("StepInto")
        self.Display.SetFunctionName("StepInto")
        self.Display.UpdateScreen()

    def PressedKeyStepOut(self):
        print("StepOut")
        self.Display.SetIcon("StepOut")
        self.Display.SetFunctionName("StepOut")
        self.Display.UpdateScreen()

    def PressedKeyRunToCursor(self):
        print("RunToCursor")
        self.Display.SetIcon("RunToCursor")
        self.Display.SetFunctionName("RunToCursor")
        self.Display.UpdateScreen()

    def PressedKeyRunSection(self):
        print("RunSection")
        self.Display.SetIcon("RunSection")
        self.Display.SetFunctionName("RunSection")
        self.Display.UpdateScreen()

    def PressedKeyRunAndAdvance(self):
        print("RunAndAdvance")
        self.Display.SetIcon("RunAndAdvance")
        self.Display.SetFunctionName("RunAndAdvance")
        self.Display.UpdateScreen()

    def PressedKeyEvaluateSelection(self):
        print("EvaluateSelection")
        self.Display.SetIcon("EvaluateSelection")
        self.Display.SetFunctionName("EvaluateSelection")
        self.Display.UpdateScreen()

Shortcuts = {}
Shortcuts['Matlab'] = {} # (Text, IsSpecialKey, Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin)
Shortcuts['Matlab']['Run'] = ('F5', True, 'F5', False, False, False, False, False)

myDisplay = Display()
myKeycodeSender = KeycodeSender()
myDevKeys = DevKeys(myDisplay, myKeycodeSender)

print("Willkommen!")

try:
    pause()
except KeyboardInterrupt:
    print("Good Bye!")