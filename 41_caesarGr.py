import sys, os
import Tkinter as tk
import tkFileDialog 
import tkMessageBox

def caesar(InputFile,OutputFile, Key, EnDec):
    ch = InputFile.read(1)

    outputFile = open(OutputFile, 'w')

    key = int(Key);
    if(key < 1 or key > 255):
        tkMessageBox.showerror("Error!","Incorrect key.")
        sys.exit(0)

    while len(ch) != 0:
        if (EnDec == '1'):
            brr = (ord(ch) + key) % 256
        if (EnDec == '2'):
            brr = ((ord(ch) - key) + 256) % 256
        outputFile.write(chr(brr))
        ch = InputFile.read(1)

    InputFile.close()
    outputFile.close()
    return True

class SampleApp(tk.Tk):
    def __init__(self):
        
        tk.Tk.__init__(self)
	self.title('Caesar chiper')
        self.geometry('300x150')
	self.OutFile = tk.Label(self, text = "Output file: ")
        self.Key = tk.Label(self, text = "Key(1,2,3...): ")
        self.entryOutFile = tk.Entry(self)
        self.entryKey = tk.Entry(self)
        
        self.buttonEncrypt = tk.Button(self, text="Encrypt", command=self.on_button_encrypt)
        self.buttonDecrypt = tk.Button(self, text="Decrypt", command=self.on_button_decrypt)
	
	self.OutFile.place(x = 10, y = 10)
	self.entryOutFile.place (x=100, y=10)
        self.Key.place(x = 10, y = 50)
        self.entryKey.place(x = 100, y = 50)
        self.buttonEncrypt.place(x = 20, y = 100)
        self.buttonDecrypt.place(x = 120, y = 100)

    def on_button_encrypt(self):
        InputFile = tkFileDialog.askopenfile()
        Key = self.entryKey.get()
        if len(Key) == 0:
            sys.exit(0)
        OutputFile = self.entryOutFile.get()
	if len(OutputFile) == 0:
            sys.exit(0)
        EnDec = '1'
        start = caesar(InputFile,OutputFile, Key, EnDec)
        tkMessageBox.showinfo("Success!","File is encrypted.")

    def on_button_decrypt(self):
        InputFile = tkFileDialog.askopenfile()
        Key = self.entryKey.get()
        if len(Key) == 0:
            sys.exit(0)
        OutputFile = self.entryOutFile.get()
	if len(OutputFile) == 0:
            sys.exit(0)
            sys.exit(0)
        EnDec = '2'
        start = caesar(InputFile,OutputFile, Key, EnDec)
        tkMessageBox.showinfo("Success!","File is decrypted.")

app = SampleApp()
app.mainloop()


