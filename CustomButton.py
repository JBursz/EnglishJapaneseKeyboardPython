from tkinter import ttk

class ChangingButton(ttk.Button):
    '''A custom button type that extends from ttk.Button. Allows for changing button value between different alphabets.'''
    def __init__(self, parent, defaultValue, shiftValue, hiragana, katakana, column, row, sticky, *args, **kwargs):
        ttk.Button.__init__(self, parent, *args, **kwargs)
        self.grid(row=row, column=column, sticky=sticky)
        self.defaultValue=defaultValue
        self.shiftValue=shiftValue
        self.hiragana=hiragana
        self.katakana=katakana

    def calculateInput(self, isShift, characterMode):
        '''Checks isShift and character mode and returns the correct character.'''
        if characterMode=="hiragana":
            return self.hiragana
        elif characterMode=="katakana":
            return self.katakana
        else:
            if isShift==0:
                return self.defaultValue
            else:
                return self.shiftValue
