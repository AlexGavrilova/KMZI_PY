#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
import Tkinter as tk
import tkMessageBox

def caesar(InputFile,OutputFile, Key, EnDec):
    if not os.path.isfile(InputFile):
        tkMessageBox.showerror("Error!","File isn't found.")
        sys.exit(0)

    inputFile = open(InputFile,'r')
    ch = inputFile.read(1)

    outputFile = open(OutputFile, 'w')

    key = int(Key);
    if(key < 1 or key > 255):
        tkMessageBox.showerror("Error!","Invalid key.")
        sys.exit(0)

    while len(ch) != 0:
        if (EnDec == '1'):
            brr = (ord(ch) + key) % 256
        if (EnDec == '2'):
            brr = ((ord(ch) - key) + 256) % 256
        outputFile.write(chr(brr))
        ch = inputFile.read(1)

    inputFile.close()
    outputFile.close()
    return True

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
	self.title('Caesar chiper')
	self.InFile = tk.Label(self, text = "Input file: ")
	self.OutFile = tk.Label(self, text = "Output file: ")
        self.Key = tk.Label(self, text = "Key(1,2,3...): ")
        self.entryInFile = tk.Entry(self)
        self.entryOutFile = tk.Entry(self)
        self.entryKey = tk.Entry(self)
        self.buttonEncrypt = tk.Button(self, text="Encrypt", command=self.on_button_encrypt)
        self.buttonDecrypt = tk.Button(self, text="Decrypt", command=self.on_button_decrypt)

        self.InFile.place(x = 10, y = 10)
        self.entryInFile.place(x = 100, y = 10)
	self.OutFile.place(x = 10, y = 50)
        self.entryOutFile.place(x = 100, y = 50)
        self.Key.place(x = 10, y = 100)
        self.entryKey.place(x = 100, y = 100)
        self.buttonEncrypt.place(x = 20, y = 150)
        self.buttonDecrypt.place(x = 120, y = 150)

    def on_button_encrypt(self):
        Key = self.entryKey.get()
        if len(Key) == 0:
            sys.exit(0)
        OutputFile = self.entryOutFile.get()
	if len(OutputFile) == 0:
            sys.exit(0)
        InputFile = self.entryInFile.get()
	if len(InputFile) == 0:
            sys.exit(0)
        EnDec = '1'
        start = caesar(InputFile,OutputFile, Key, EnDec)
        tkMessageBox.showinfo("Success!","File is encrypted.")

    def on_button_decrypt(self):
        Key = self.entryKey.get()
        if len(Key) == 0:
            sys.exit(0)
        OutputFile = self.entryOutFile.get()
	if len(OutputFile) == 0:
            sys.exit(0)
        InputFile = self.entryInFile.get()
	if len(InputFile) == 0:
            sys.exit(0)
        EnDec = '2'
        start = caesar(InputFile,OutputFile, Key, EnDec)
        tkMessageBox.showinfo("Success!","File is decrypted.")

app = SampleApp()
app.mainloop()


