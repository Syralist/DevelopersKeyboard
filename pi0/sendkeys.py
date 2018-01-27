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

print("0x%x" % (iModLCtrl | iModLShift))

Printables = {
    'A' : ("0x04", iModLShift),
    'a' : ("0x04", iModNone),
    'B' : ("0x05", iModLShift),
    'b' : ("0x05", iModNone),
    'C' : ("0x06", iModLShift),
    'c' : ("0x06", iModNone),
    'D' : ("0x07", iModLShift),
    'd' : ("0x07", iModNone),
    'E' : ("0x08", iModLShift),
    'e' : ("0x08", iModNone),
    'F' : ("0x09", iModLShift),
    'f' : ("0x09", iModNone),
    'G' : ("0x0a", iModLShift),
    'g' : ("0x0a", iModNone),
    'H' : ("0x0b", iModLShift),
    'h' : ("0x0b", iModNone),
    'I' : ("0x0c", iModLShift),
    'i' : ("0x0c", iModNone),
    'J' : ("0x0d", iModLShift),
    'j' : ("0x0d", iModNone),
    'K' : ("0x0e", iModLShift),
    'k' : ("0x0e", iModNone),
    'L' : ("0x0f", iModLShift),
    'l' : ("0x0f", iModNone),
    'M' : ("0x10", iModLShift),
    'm' : ("0x10", iModNone),
    'N' : ("0x11", iModLShift),
    'n' : ("0x11", iModNone),
    'O' : ("0x12", iModLShift),
    'o' : ("0x12", iModNone),
    'P' : ("0x13", iModLShift),
    'p' : ("0x13", iModNone),
    'Q' : ("0x14", iModLShift),
    'q' : ("0x14", iModNone),
    'R' : ("0x15", iModLShift),
    'r' : ("0x15", iModNone),
    'S' : ("0x16", iModLShift),
    's' : ("0x16", iModNone),
    'T' : ("0x17", iModLShift),
    't' : ("0x17", iModNone),
    'U' : ("0x18", iModLShift),
    'u' : ("0x18", iModNone),
    'V' : ("0x19", iModLShift),
    'v' : ("0x19", iModNone),
    'W' : ("0x1a", iModLShift),
    'w' : ("0x1a", iModNone),
    'X' : ("0x1b", iModLShift),
    'x' : ("0x1b", iModNone),
    'Y' : ("0x1c", iModLShift),
    'y' : ("0x1c", iModNone),
    'Z' : ("0x1d", iModLShift),
    'z' : ("0x1d", iModNone),
}

print(Printables)

def sendPrintable(key, Ctrl = False, Alt = False, Win = False):
    pass
