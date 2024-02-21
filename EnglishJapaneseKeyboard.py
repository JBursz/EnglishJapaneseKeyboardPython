import tkinter as tk
from tkinter import ttk
from CustomButton import ChangingButton

class ENJPKeyboard():
    # setup main window and frames
    root = tk.Tk()
    root.title("English and Japanese Keyboard")
    frame0 = ttk.Frame(root, takefocus=0)
    frame0.grid(column=0, row=0, sticky="nesw")
    frame0.grid_columnconfigure(0, weight=1)
    frame0.grid_rowconfigure(0, weight=1)

    frame1 = ttk.Frame(root, takefocus=0)
    frame1.grid(column=0, row=1, sticky='nesw')
    frame1.grid_columnconfigure(0, weight=1)

    # configure weights of window for better resizing
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)

    # variables for checkbox and textbox
    isTopWindow = tk.IntVar()
    entryText = tk.StringVar()
    textBox = tk.Text(frame0, font="Helvetica 32", state='disabled', height=4)
    textBox.grid(column=0, row=0, rowspan=2, sticky="nesw")
    
    # default font style
    ttk.Style().configure('TButton', font=('Helvetica', 14))
    ttk.Style().map("TEntry", foreground=[("disabled", "black")])

    # these variables are used to check if English letter should be lower or upper case
    # ...and characterMode is used to check which alphabet were are in (English, Hiragana, Katakana)
    isShift = 0
    isCaps=0
    characterMode= tk.StringVar()
    
    changingButtonList = []   # contains all changing buttons to use in for loop
    
    def __init__(self):
        # set references to class variables for easy access
        frame0=ENJPKeyboard.frame0
        frame1=ENJPKeyboard.frame1
        root=ENJPKeyboard.root
        entryText=ENJPKeyboard.entryText
        textBox=ENJPKeyboard.textBox
        isShift=ENJPKeyboard.isShift

        scrollBar = ttk.Scrollbar(frame0, orient='vertical', command=textBox.yview)
        scrollBar.grid(column=1, row=0, rowspan=2, sticky="ns")

        textBox['yscrollcommand']=scrollBar.set

        # watch for changes to entryText and set textBox
        entryText.trace_add('write', self.textChanged)

        # copy to clipboard button
        ttk.Button(frame0, text="Copy", padding=3, width=6, command=lambda: self.copyClipboard()).grid(column=2, row=0, sticky="nesw")
        # clear all text button
        ttk.Button(frame0, text="Clear", padding=3, width=6, command=lambda: self.clearAll()).grid(column=2, row=1, sticky='nesw')
        
        # CREATE KEYBOARD BUTTONS
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='`', shiftValue='~', hiragana='ろ', katakana='ロ', text="`", column=0, row=1, sticky="nesw"))        
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='1', shiftValue='!', hiragana='ぬ', katakana='ヌ', text="1", column=1, row=1,sticky="nesw"))        
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='2', shiftValue='@', hiragana='ふ', katakana='フ', text="2", column=2, row=1,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='3', shiftValue='#', hiragana='あ', katakana='ア', text="3", column=3, row=1,sticky="nesw"))        
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='4', shiftValue='$', hiragana='う', katakana='ウ', text="4", column=4, row=1,sticky="nesw"))        
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='5', shiftValue='%', hiragana='え', katakana='エ', text="5", column=5, row=1,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='6', shiftValue='^', hiragana='お', katakana='オ', text="6", column=6, row=1, sticky="nesw"))        
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='7', shiftValue='&', hiragana='や', katakana='ヤ', text="7", column=7, row=1,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='8', shiftValue='*', hiragana='ゆ', katakana='ユ', text="8", column=8, row=1,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='9', shiftValue='(', hiragana='よ', katakana='ヨ', text="9", column=9, row=1,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='0', shiftValue=')', hiragana='わ', katakana='ワ', text="0", column=10, row=1,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='-', shiftValue='_', hiragana='ほ', katakana='ホ', text="-", column=11, row=1,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='=', shiftValue='+', hiragana='へ', katakana='ヘ', text="=", column=12, row=1,sticky="nesw"))
        ttk.Button(frame1, text="Back", command=lambda:self.backspace(), padding=4, width=4).grid(column=13, row=1, sticky="nesw")
        
        ttk.Button(frame1, text="Tab", padding=4, width=3, command=lambda: self.tabKey()).grid(column=0, row=2, sticky="nesw")
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='q', shiftValue='Q', hiragana='た', katakana='タ', text="q", column=1, row=2,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='w', shiftValue='W', hiragana='て', katakana='テ', text="w", column=2, row=2,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='e', shiftValue='E', hiragana='い', katakana='イ', text="e", column=3, row=2,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='r', shiftValue='R', hiragana='す', katakana='ス', text="r", column=4, row=2,sticky="nesw"))        
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='t', shiftValue='T', hiragana='か', katakana='カ', text="t", column=5, row=2,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='y', shiftValue='Y', hiragana='ん', katakana='ン', text="y", column=6, row=2, sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='u', shiftValue='U', hiragana='な', katakana='ナ', text="u", column=7, row=2,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='i', shiftValue='I', hiragana='に', katakana='ニ', text="i", column=8, row=2,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='o', shiftValue='O', hiragana='ら', katakana='ラ', text="o", column=9, row=2,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='p', shiftValue='P', hiragana='せ', katakana='セ', text="p", column=10, row=2,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='[', shiftValue='{', hiragana='゛', katakana='゛', text="[", column=11, row=2,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue=']', shiftValue='}', hiragana='゜', katakana='゜', text="]", column=12, row=2,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='\\', shiftValue='|', hiragana='む', katakana='ム', text="\\", column=13, row=2, sticky="nesw"))
        
        ttk.Button(frame1, text="Caps", command=lambda: self.toggleCaps(), padding=4, width=4).grid(column=0, row=3, sticky="nesw")
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='a', shiftValue='A', hiragana='ち', katakana='チ', text="a", column=1, row=3,sticky="nesw"))        
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='s', shiftValue='S', hiragana='と', katakana='ト', text="s", column=2, row=3, sticky="nesw"))        
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='d', shiftValue='D', hiragana='し', katakana='シ', text="d", column=3, row=3,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='f', shiftValue='F', hiragana='は', katakana='ハ', text="f", column=4, row=3, sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='g', shiftValue='G', hiragana='き', katakana='キ', text="g", column=5, row=3,sticky="nesw"))        
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='h', shiftValue='H', hiragana='く', katakana='ク', text="h", column=6, row=3, sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='j', shiftValue='J', hiragana='ま', katakana='マ', text="j", column=7, row=3, sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='k', shiftValue='K', hiragana='の', katakana='ノ', text="k", column=8, row=3, sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='l', shiftValue='L', hiragana='り', katakana='リ', text="l", column=9, row=3,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue=';', shiftValue=':', hiragana='れ', katakana='レ', text=";", column=10, row=3, sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue="'", shiftValue='"', hiragana='け', katakana='ケ', text="'", column=11, row=3, sticky="nesw"))
        ttk.Button(frame1, text="Enter", command=lambda: self.enterKey(), padding=4, width=5).grid(column=12, row=3, sticky="nesw")
        
        ttk.Button(frame1, text="Shift", command=lambda: self.toggleShift(), padding=4, width=5).grid(column=0, row=4, sticky="nesw")
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='z', shiftValue='Z', hiragana='つ', katakana='ツ', text="z", column=1, row=4, sticky="nesw"))        
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='x', shiftValue='X', hiragana='さ', katakana='サ', text="x", column=2, row=4, sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='c', shiftValue='C', hiragana='そ', katakana='ソ', text="c", column=3, row=4, sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='v', shiftValue='V', hiragana='ひ', katakana='ヒ', text="v", column=4, row=4, sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='b', shiftValue='B', hiragana='こ', katakana='コ', text="b", column=5, row=4, sticky="nesw"))        
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='n', shiftValue='N', hiragana='み', katakana='ミ', text="n", column=6, row=4,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='m', shiftValue='M', hiragana='も', katakana='モ', text="m", column=7, row=4, sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue=',', shiftValue='<', hiragana='ね', katakana='ネ', text=",", column=8, row=4, sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='.', shiftValue='>', hiragana='る', katakana='ル', text=".", column=9, row=4,sticky="nesw"))
        self.changingButtonList.append(ChangingButton(frame1, defaultValue='/', shiftValue='?', hiragana='め', katakana='ル', text="/", column=10, row=4,sticky="nesw"))
        ttk.Button(frame1, text="Shift", command=lambda: self.toggleShift(), padding=4, width=5).grid(column=11, row=4, sticky="nesw")
        
        ttk.Button(frame1, text="space",command=lambda: self.spacebar()).grid(column=12, row=4, sticky="nesw", columnspan=2)
        # -----END OF KEYBOARD BUTTONS------------------------

        # RadioButtons for changing alphaabet
        ttk.Radiobutton(frame1, text="Romanji", variable=self.characterMode, value="romanji", command=lambda: self.toggleJP()).grid(column=1, columnspan=3, row=5,sticky="nesw")
        ttk.Radiobutton(frame1, text="Hiragana", variable=self.characterMode, value="hiragana", command=lambda: self.toggleJP()).grid(column=4,columnspan=3, row=5,sticky="nesw")
        ttk.Radiobutton(frame1, text="Katakana", variable=self.characterMode, value="katakana", command=lambda: self.toggleJP()).grid(column=7,columnspan=3, row=5,sticky="nesw")
        # Checkbox to toggle if window is always on top
        ttk.Checkbutton(frame1, text="Topmost Window", variable=self.isTopWindow, command=lambda: self.toggleTopWindow()).grid(column=9, columnspan=3, row=5, sticky="nesw")
        self.characterMode.set("romanji")

        # Configure column and row weights for equal spacing when resizing window
        for column in range(14):
            frame1.columnconfigure(column, weight=2)

        for row in range(6):
            frame1.rowconfigure(row, weight=1)


        # Go through all changing buttons and set command for when button is pressed
        for i in range(len(self.changingButtonList)):
            self.changingButtonList[i].config(command=lambda i=i: self.sendInput(self.changingButtonList[i], self.entryText), padding=0, width=4)
        
        root.minsize(325,350)
        root.bind('<Configure>', self.resize) #resize will run when window is resized and will change font sizes to match
        root.mainloop()


    def sendInput(self, b, entry):
        '''Send character in correct alphabet to the textbox when a button is pressed.'''
        character = b.calculateInput(self.isShift, self.characterMode.get())
        entry.set(entry.get() + character)
        if self.isShift==1 and self.isCaps==0:
            self.toggleShift()
    
    def toggleShift(self):
        '''Commands for when Shift or CapsLock buttons are pressed.'''
        if self.isShift==0:
            self.isShift=1
        else:
            self.isShift=0
            self.isCaps=0
        for widget in self.frame1.winfo_children():
            if isinstance(widget, ChangingButton):
                widget.configure(text=widget.calculateInput(self.isShift, self.characterMode.get()))

    def toggleCaps(self):
        if self.isCaps==0:
            self.isCaps=1
            self.isShift=1
        else:
            self.isCaps=0
            self.isShift=0
        for widget in self.frame1.winfo_children():
            if isinstance(widget, ChangingButton):
                widget.configure(text=widget.calculateInput(self.isShift, self.characterMode.get()))

    def toggleJP(self):
        '''Called when one of the radio buttons is pressed. Will go through a loop and set all button texts to chosen alphabet.'''
        for widget in self.frame1.winfo_children():
            if isinstance(widget, ChangingButton):
                widget.configure(text=widget.calculateInput(self.isShift, self.characterMode.get()))
    
    def resize(self, event):
        '''Resize the text on buttons and textbox to match window size, called when window is resized.'''
        if(isinstance(event.widget, tk.Tk)):
            windowWidth, windowHeight = self.root.winfo_width(), self.root.winfo_height()
            if(windowWidth <= 1924 and windowWidth > 1000):
                ttk.Style().configure('TButton', font=('Helvetica', 24))
                self.textBox.config(font='Helvetica 24')
            elif(windowWidth <= 1000 and windowWidth > 500):
                ttk.Style().configure('TButton', font=('Helvetica', 14))
                self.textBox.config(font='Helvetica 14')
            elif(windowWidth <= 500):
                ttk.Style().configure('TButton', font=('Helvetica', 8))
                self.textBox.config(font='Helvetica 8')
            self.root.update()
    
    # commands for extra keyboard buttons (spacebar, tab, backspace, enter)
    def spacebar(self):
        self.entryText.set(self.entryText.get() + " ")

    def tabKey(self):
        self.entryText.set(self.entryText.get() + "\t")

    def backspace(self):
        s=self.entryText.get()
        s=s[:-1]
        self.entryText.set(s)

    def enterKey(self):
        self.entryText.set(self.entryText.get() + "\n")

    def copyClipboard(self):
        '''Command for copy to clipboard button.'''
        self.root.clipboard_clear()
        self.root.clipboard_append(self.entryText.get())

    def toggleTopWindow(self):
        '''Command for TopMostWindow checkbox.'''
        if self.isTopWindow.get()== 1:
            print("top " + str(self.isTopWindow.get()))
            self.root.wm_attributes("-topmost",1)
        else:
            print("not top "+ str(self.isTopWindow))
            self.root.wm_attributes("-topmost",0)

    def textChanged(self, var, index, mode):
        '''Set textbox when stringVar is changed.'''
        self.textBox.config(state='normal')
        self.textBox.delete(1.0, tk.END)
        self.textBox.insert(1.0, self.entryText.get())
        self.textBox.config(state='disabled')
        self.textBox.see(tk.END)

    def clearAll(self):
        '''Clear all text when clear button is pressed.'''
        self.entryText.set("")

keyboard = ENJPKeyboard()
