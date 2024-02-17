import tkinter as tk
from tkinter import ttk
from tkinter import font

#A custom button type that extends from ttk.Button. Allows for changing button value between different alphabets
class ChangingButton(ttk.Button):
	
	def __init__(self, parent, defaultValue, shiftValue, hiragana, katakana, column, row, sticky, *args, **kwargs):
		ttk.Button.__init__(self, parent, *args, **kwargs)
		self.grid(row=row, column=column, sticky=sticky)
		self.defaultValue=defaultValue
		self.shiftValue=shiftValue
		self.hiragana=hiragana
		self.katakana=katakana

	#checks isShift and character mode and returns the correct character
	def calculateInput(self, isShift, characterMode):
		if characterMode=="hiragana":
			return self.hiragana
		elif characterMode=="katakana":
			return self.katakana
		else:
			if isShift==0:
				#print("defalt = " + self.defaultValue)
				return self.defaultValue
			else:
				return self.shiftValue
