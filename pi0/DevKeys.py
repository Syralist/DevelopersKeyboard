import os
import sys
os.chdir(sys.path[0])

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
        self.ImageDraw.rectangle([0, 0, self.width, self.height], fill=0, outline=0)
        self.ImageDraw.line([0, 27, self.width, 27], fill=255, width=1)
        self.ImageDraw.text((2, 2), name, font=self.Font, fill=255)

    def SetIcon(self, icon):
        self.Image.paste(self.Icons[icon], (self.IconLeft, self.IconTop))
    
    def SetFunctionName(self, name):
        self.ImageDraw.rectangle([self.FunctionNameLeft, self.FunctionNameTop, self.width, self.height-15], fill=0, outline=0)
        self.ImageDraw.text((self.FunctionNameLeft, self.FunctionNameTop), self.FunctionNames[name],  font=self.Font, fill=255)
    
    def SetShortcut(self, Text):
        self.ImageDraw.rectangle([self.ShortcutLeft, self.ShortcutTop, self.width, self.height], fill=0, outline=0)
        if not Text:
            Text = '-not set-'
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

    def SetDisplay(self, Function):
        print(Function)
        (Text, IsSpecialKey, Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin) = Shortcuts[self.Programms[self.ProgrammIndex]][Function]
        self.Display.SetIcon(Function)
        self.Display.SetFunctionName(Function)
        self.Display.SetShortcut(Text)
        self.Display.UpdateScreen()
        if Text:
            if IsSpecialKey:
                self.KeycodeSender.sendSpecialKey(Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin)
            else:
                self.KeycodeSender.sendPrintable(Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin)

    def PressedKeySelect(self):
        print("Select")
        self.ProgrammIndex += 1
        if self.ProgrammIndex >= len(self.Programms):
            self.ProgrammIndex = 0
        self.Display.SetProgramm(self.Programms[self.ProgrammIndex])
        self.Display.UpdateScreen()

    def PressedKeyRun(self):
        Function = "Run"
        self.SetDisplay(Function)

    def PressedKeyStop(self):
        Function = "Stop"
        self.SetDisplay(Function)

    def PressedKeyStepOver(self):
        Function = "StepOver"
        self.SetDisplay(Function)

    def PressedKeyStepInto(self):
        Function = "StepInto"
        self.SetDisplay(Function)

    def PressedKeyStepOut(self):
        Function = "StepOut"
        self.SetDisplay(Function)

    def PressedKeyRunToCursor(self):
        Function = "RunToCursor"
        self.SetDisplay(Function)

    def PressedKeyRunSection(self):
        Function = "RunSection"
        self.SetDisplay(Function)

    def PressedKeyRunAndAdvance(self):
        Function = "RunAndAdvance"
        self.SetDisplay(Function)

    def PressedKeyEvaluateSelection(self):
        Function = "EvaluateSelection"
        self.SetDisplay(Function)

Shortcuts = {}
Shortcuts['Matlab'] = {} # (Text, IsSpecialKey, Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin)
Shortcuts['Matlab']['Run'] = ('F5', True, 'F5', False, False, False, False, False)
Shortcuts['Matlab']['Stop'] = ('Shift+F5', True, 'F5', True, False, False, False, False)
Shortcuts['Matlab']['StepOver'] = ('F10', True, 'F10', False, False, False, False, False)
Shortcuts['Matlab']['StepInto'] = ('F11', True, 'F11', False, False, False, False, False)
Shortcuts['Matlab']['StepOut'] = ('Shift+F11', True, 'F11', True, False, False, False, False)
Shortcuts['Matlab']['RunToCursor'] = ('Shift+F10', True, 'F10', True, False, False, False, False)
Shortcuts['Matlab']['RunSection'] = ('Strg+Enter', False, '\n', False, True, False, False, False)
Shortcuts['Matlab']['RunAndAdvance'] = ('St+Sh+Enter', False, '\n', True, True, False, False, False)
Shortcuts['Matlab']['EvaluateSelection'] = ('F9', True, 'F9', False, False, False, False, False)
Shortcuts['VisualStudio'] = {} # (Text, IsSpecialKey, Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin)
Shortcuts['VisualStudio']['Run'] = ('F5', True, 'F5', False, False, False, False, False)
Shortcuts['VisualStudio']['Stop'] = ('Shift+F5', True, 'F5', True, False, False, False, False)
Shortcuts['VisualStudio']['StepOver'] = ('F10', True, 'F10', False, False, False, False, False)
Shortcuts['VisualStudio']['StepInto'] = ('F11', True, 'F11', False, False, False, False, False)
Shortcuts['VisualStudio']['StepOut'] = ('Shift+F11', True, 'F11', True, False, False, False, False)
Shortcuts['VisualStudio']['RunToCursor'] = (None, None, None, None, None, None, None, None)
Shortcuts['VisualStudio']['RunSection'] = (None, None, None, None, None, None, None, None)
Shortcuts['VisualStudio']['RunAndAdvance'] = (None, None, None, None, None, None, None, None)
Shortcuts['VisualStudio']['EvaluateSelection'] = (None, None, None, None, None, None, None, None)
Shortcuts['Eclipse'] = {} # (Text, IsSpecialKey, Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin)
Shortcuts['Eclipse']['Run'] = ('F11', True, 'F11', False, False, False, False, False)
Shortcuts['Eclipse']['Stop'] = ('Strg+F2', True, 'F2', False, True, False, False, False)
Shortcuts['Eclipse']['StepOver'] = ('F6', True, 'F6', False, False, False, False, False)
Shortcuts['Eclipse']['StepInto'] = ('F5', True, 'F5', False, False, False, False, False)
Shortcuts['Eclipse']['StepOut'] = ('F7', True, 'F7', False, False, False, False, False)
Shortcuts['Eclipse']['RunToCursor'] = ('Strg+R', False, 'r', True, None, None, None, None)
Shortcuts['Eclipse']['RunSection'] = (None, None, None, None, None, None, None, None)
Shortcuts['Eclipse']['RunAndAdvance'] = (None, None, None, None, None, None, None, None)
Shortcuts['Eclipse']['EvaluateSelection'] = ('F8', True, 'F8', False, False, False, False, False)
Shortcuts['Notepad++'] = {} # (Text, IsSpecialKey, Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin)
Shortcuts['Notepad++']['Run'] = ('F6', True, 'F6', False, False, False, False, False)
Shortcuts['Notepad++']['Stop'] = (None, None, None, None, None, None, None, None)
Shortcuts['Notepad++']['StepOver'] = (None, None, None, None, None, None, None, None)
Shortcuts['Notepad++']['StepInto'] = (None, None, None, None, None, None, None, None)
Shortcuts['Notepad++']['StepOut'] = (None, None, None, None, None, None, None, None)
Shortcuts['Notepad++']['RunToCursor'] = (None, None, None, None, None, None, None, None)
Shortcuts['Notepad++']['RunSection'] = (None, None, None, None, None, None, None, None)
Shortcuts['Notepad++']['RunAndAdvance'] = (None, None, None, None, None, None, None, None)
Shortcuts['Notepad++']['EvaluateSelection'] = (None, None, None, None, None, None, None, None)
Shortcuts['VBA'] = {} # (Text, IsSpecialKey, Key, ModShift, ModCtrl, ModAlt, ModSuper, ModWin)
Shortcuts['VBA']['Run'] = ('F5', True, 'F5', False, False, False, False, False)
Shortcuts['VBA']['Stop'] = (None, None, None, None, None, None, None, None)
Shortcuts['VBA']['StepOver'] = ('Shift+F8', True, 'F8', True, False, False, False, False)
Shortcuts['VBA']['StepInto'] = ('F8', True, 'F8', False, False, False, False, False)
Shortcuts['VBA']['StepOut'] = ('St+Sh+F8', True, 'F8', True, True, False, False, False)
Shortcuts['VBA']['RunToCursor'] = ('Strg+F8', True, 'F8', False, True, False, False, False)
Shortcuts['VBA']['RunSection'] = (None, None, None, None, None, None, None, None)
Shortcuts['VBA']['RunAndAdvance'] = (None, None, None, None, None, None, None, None)
Shortcuts['VBA']['EvaluateSelection'] = (None, None, None, None, None, None, None, None)

myDisplay = Display()
myKeycodeSender = KeycodeSender()
myDevKeys = DevKeys(myDisplay, myKeycodeSender)

print("Willkommen!")

try:
    pause()
except KeyboardInterrupt:
    print("Good Bye!")

myDisplay = Display()
myKeycodeSender = KeycodeSender()
myDevKeys = DevKeys(myDisplay, myKeycodeSender)

print("Willkommen!")

try:
    pause()
except KeyboardInterrupt:
    print("Good Bye!")
