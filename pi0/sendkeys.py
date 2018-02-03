iModNone = 0
iModLCtrl = 1 << 0
iModLShift = 1 << 1
iModLAlt = 1 << 2
iModLWin = 1 << 3
iModRCtrl = 1 << 4
iModRShift = 1 << 5
iModRAlt = 1 << 6
iModRSuper = 1 << 7
bModCtrl = "0x%x" % iModLCtrl
bModShift = "0x%x" % iModLShift
bModAlt = "0x%x" % iModLAlt
bModWin = "0x%x" % iModLWin
bNull = "0x00"
bReleaseAll = bytes(int(x,0) for x in [bNull, bNull, bNull, bNull, bNull, bNull, bNull, bNull])

# print("0x%x" % (iModLCtrl | iModLAlt))

Printables = {}

Printables["de_DE"] = {
    'A' : ("0x04", "0x%x" % iModLShift, False),
    'a' : ("0x04", "0x%x" % iModNone, False),
    'B' : ("0x05", "0x%x" % iModLShift, False),
    'b' : ("0x05", "0x%x" % iModNone, False),
    'C' : ("0x06", "0x%x" % iModLShift, False),
    'c' : ("0x06", "0x%x" % iModNone, False),
    'D' : ("0x07", "0x%x" % iModLShift, False),
    'd' : ("0x07", "0x%x" % iModNone, False),
    'E' : ("0x08", "0x%x" % iModLShift, False),
    'e' : ("0x08", "0x%x" % iModNone, False),
    'F' : ("0x09", "0x%x" % iModLShift, False),
    'f' : ("0x09", "0x%x" % iModNone, False),
    'G' : ("0x0a", "0x%x" % iModLShift, False),
    'g' : ("0x0a", "0x%x" % iModNone, False),
    'H' : ("0x0b", "0x%x" % iModLShift, False),
    'h' : ("0x0b", "0x%x" % iModNone, False),
    'I' : ("0x0c", "0x%x" % iModLShift, False),
    'i' : ("0x0c", "0x%x" % iModNone, False),
    'J' : ("0x0d", "0x%x" % iModLShift, False),
    'j' : ("0x0d", "0x%x" % iModNone, False),
    'K' : ("0x0e", "0x%x" % iModLShift, False),
    'k' : ("0x0e", "0x%x" % iModNone, False),
    'L' : ("0x0f", "0x%x" % iModLShift, False),
    'l' : ("0x0f", "0x%x" % iModNone, False),
    'M' : ("0x10", "0x%x" % iModLShift, False),
    'm' : ("0x10", "0x%x" % iModNone, False),
    'N' : ("0x11", "0x%x" % iModLShift, False),
    'n' : ("0x11", "0x%x" % iModNone, False),
    'O' : ("0x12", "0x%x" % iModLShift, False),
    'o' : ("0x12", "0x%x" % iModNone, False),
    'P' : ("0x13", "0x%x" % iModLShift, False),
    'p' : ("0x13", "0x%x" % iModNone, False),
    'Q' : ("0x14", "0x%x" % iModLShift, False),
    'q' : ("0x14", "0x%x" % iModNone, False),
    'R' : ("0x15", "0x%x" % iModLShift, False),
    'r' : ("0x15", "0x%x" % iModNone, False),
    'S' : ("0x16", "0x%x" % iModLShift, False),
    's' : ("0x16", "0x%x" % iModNone, False),
    'T' : ("0x17", "0x%x" % iModLShift, False),
    't' : ("0x17", "0x%x" % iModNone, False),
    'U' : ("0x18", "0x%x" % iModLShift, False),
    'u' : ("0x18", "0x%x" % iModNone, False),
    'V' : ("0x19", "0x%x" % iModLShift, False),
    'v' : ("0x19", "0x%x" % iModNone, False),
    'W' : ("0x1a", "0x%x" % iModLShift, False),
    'w' : ("0x1a", "0x%x" % iModNone, False),
    'X' : ("0x1b", "0x%x" % iModLShift, False),
    'x' : ("0x1b", "0x%x" % iModNone, False),
    'Y' : ("0x1c", "0x%x" % iModLShift, False),
    'y' : ("0x1c", "0x%x" % iModNone, False),
    'Z' : ("0x1d", "0x%x" % iModLShift, False),
    'z' : ("0x1d", "0x%x" % iModNone, False),
    '0' : ("0x27", "0x%x" % iModNone, False),
    '1' : ("0x1e", "0x%x" % iModNone, False),
    '2' : ("0x1f", "0x%x" % iModNone, False),
    '3' : ("0x20", "0x%x" % iModNone, False),
    '4' : ("0x21", "0x%x" % iModNone, False),
    '5' : ("0x22", "0x%x" % iModNone, False),
    '6' : ("0x23", "0x%x" % iModNone, False),
    '7' : ("0x24", "0x%x" % iModNone, False),
    '8' : ("0x25", "0x%x" % iModNone, False),
    '9' : ("0x26", "0x%x" % iModNone, False),
    ' ' : ("0x2c", "0x%x" % iModNone, False),
    '!' : ("0x1e", "0x%x" % iModLShift, False),
    '\"' : ("0x1f", "0x%x" % iModLShift, False),
    '#' : ("0x31", "0x%x" % iModNone, False),
    '$' : ("0x21", "0x%x" % iModLShift, False),
    '%' : ("0x22", "0x%x" % iModLShift, False),
    '&' : ("0x23", "0x%x" % iModLShift, False),
    '\'' : ("0x31", "0x%x" % iModLShift, False),
    '(' : ("0x25", "0x%x" % iModLShift, False),
    ')' : ("0x26", "0x%x" % iModLShift, False),
    '*' : ("0x30", "0x%x" % iModLShift, False),
    '+' : ("0x30", "0x%x" % iModNone, False),
    '´' : ("0x2e", "0x%x" % iModNone, True),
    '-' : ("0x38", "0x%x" % iModNone, False),
    '.' : ("0x37", "0x%x" % iModNone, False),
    ',' : ("0x36", "0x%x" % iModNone, False),
    '/' : ("0x24", "0x%x" % iModLShift, False),
    ':' : ("0x37", "0x%x" % iModLShift, False),
    ';' : ("0x36", "0x%x" % iModLShift, False),
    '<' : ("0x64", "0x%x" % iModNone, False),
    '=' : ("0x27", "0x%x" % iModLShift, False),
    '>' : ("0x64", "0x%x" % iModLShift, False),
    '?' : ("0x2d", "0x%x" % iModLShift, False),
    '@' : ("0x14", "0x%x" % iModRSuper, False),
    '[' : ("0x25", "0x%x" % iModRSuper, False),
    '\\' : ("0x2d", "0x%x" % iModRSuper, False),
    ']' : ("0x26", "0x%x" % iModRSuper, False),
    '^' : ("0x35", "0x%x" % iModNone, True),
    '_' : ("0x38", "0x%x" % iModLShift, False),
    '`' : ("0x2e", "0x%x" % iModLShift, True),
    '{' : ("0x2f", "0x%x" % iModRSuper, False),
    '|' : ("0x64", "0x%x" % iModRSuper, False),
    '}' : ("0x27", "0x%x" % iModRSuper, False),
    '~' : ("0x30", "0x%x" % iModRSuper, False),
    '\t' : ("0x2b", "0x%x" % iModNone, False),
    '\n' : ("0x28", "0x%x" % iModNone, False),
    'µ' : ("0x10", "0x%x" % iModRSuper, False),
    '°' : ("0x35", "0x%x" % iModLShift, False),
    '§' : ("0x20", "0x%x" % iModLShift, False),
    'ä' : ("0x34", "0x%x" % iModNone, False),
    'Ä' : ("0x34", "0x%x" % iModLShift, False),
    'ö' : ("0x33", "0x%x" % iModNone, False),
    'Ö' : ("0x33", "0x%x" % iModLShift, False),
    'ü' : ("0x2f", "0x%x" % iModNone, False),
    'Ü' : ("0x2f", "0x%x" % iModLShift, False),
    'ß' : ("0x2d", "0x%x" % iModNone, False),
    '€' : ("0x08", "0x%x" % iModRSuper, False),
}

SpecialKeys = {
    'ESC' : "0x29",
    'BACKSPACE' : "0x2a",
    'CAPSLOCK' : "0x39",
    'F1' : "0x3a",
    'F2' : "0x3b",
    'F3' : "0x3c",
    'F4' : "0x3d",
    'F5' : "0x3e",
    'F6' : "0x3f",
    'F7' : "0x40",
    'F8' : "0x41",
    'F9' : "0x42",
    'F10' : "0x43",
    'F11' : "0x44",
    'F12' : "0x45",
    'PRINTSCREEN' : "0x46",
    'SCROLLLOCK' : "0x47",
    'PAUSE' : "0x48",
    'INSERT' : "0x49",
    'HOME' : "0x4a",
    'PAGEUP' : "0x4b",
    'DELETE' : "0x4c",
    'END' : "0x4d",
    'PAGEDOWN' : "0x4e",
    'RIGHTARROW' : "0x4f",
    'LEFTARROW' : "0x50",
    'DOWNARROW' : "0x51",
    'UPARROW' : "0x52",
}

KeypadKeys = {
    'NUMLOCK' : "0x53",
    '/' : "0x54",
    '*' : "0x55",
    '-' : "0x56",
    '+' : "0x57",
    'ENTER' : "0x58",
    '1' : "0x59",
    '2' : "0x5a",
    '3' : "0x5b",
    '4' : "0x5c",
    '5' : "0x5d",
    '6' : "0x5e",
    '7' : "0x5f",
    '8' : "0x60",
    '9' : "0x61",
    '0' : "0x62",
    '.' : "0x63",
    '=' : "0x67",
}


# print(Printables["de_DE"])

class KeycodeSender:
    def __init__(self, locale = "de_DE", device = r"/dev/hidg0"):
        self.PrintableKeys = Printables[locale]
        self.SpecialKeys = SpecialKeys
        self.KeypadKeys = KeypadKeys

    def sendPrintable(self, key):
        KeyCode, ModCode, Dead = self.PrintableKeys[key]
        Sequence = bytes(int(x,0) for x in [ModCode, bNull, KeyCode, bNull, bNull, bNull, bNull, bNull])
        with open(device, 'wb') as fp:
            fp.write(Sequence)
            fp.write(bReleaseAll)
            if Dead:
                fp.write(Sequence)
                fp.write(bReleaseAll)

    def sendKeypadKey(self, key):
        Sequence = bytes(int(x,0) for x in [bNull, bNull, self.KeypadKeys[key], bNull, bNull, bNull, bNull, bNull])
        with open(device, 'wb') as fp:
            fp.write(Sequence)
            fp.write(bReleaseAll)

    def sendSpecialKey(self, key, ModShift = False, ModCtrl = False, ModAlt = False, ModSuper = False):
        KeyCode = self.SpecialKeys[key]
        ModCode = "0x%x" % (iModLShift if ModShift else 0 | 
                            iModLCtrl if ModCtrl else 0 |
                            iModLAlt if ModAlt else 0 |
                            iModRSuper if ModSuper else 0)
        Sequence = bytes(int(x,0) for x in [ModCode, bNull, KeyCode, bNull, bNull, bNull, bNull, bNull])
        with open(device, 'wb') as fp:
            fp.write(Sequence)
            fp.write(bReleaseAll)


de_Keyboard = KeycodeSender()

de_Keyboard.sendPrintable('&')
de_Keyboard.sendKeypadKey('0')
de_Keyboard.sendSpecialKey('F1', ModShift = True)

# print(de_Keyboard)
