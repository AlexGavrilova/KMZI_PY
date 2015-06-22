#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
import Tkinter as tk
import tkMessageBox

nb = 4  
nr = 10  
nk = 4  

Sbox = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

InvSbox = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]

Rcon = [[0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
]


def encrypt(input_bytes, key):

    state = [[] for j in range(4)]
    for r in range(4):
        for c in range(nb):
            state[r].append(input_bytes[r + 4 * c])

    KeyEndec = KeyExpansion(key)

    state = AddRoundKey(state, KeyEndec)

    for rnd in range(1, nr):
        state = SubBytes(state)    
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(state, KeyEndec, rnd)

    state = SubBytes(state)
    
    state = ShiftRows(state)
    
    state = AddRoundKey(state, KeyEndec, rnd + 1)
    
    output = [None for i in range(4 * nb)]
    for r in range(4):
        for c in range(nb):
            output[r + 4 * c] = state[r][c]

    return output


def decrypt(cipher, key):

    state = [[] for i in range(nb)]
    for r in range(4):
        for c in range(nb):
            state[r].append(cipher[r + 4 * c])

    KeyEndec = KeyExpansion(key)

    state = AddRoundKey(state, KeyEndec, nr)

    rnd = nr - 1
    while rnd >= 1:
        state = ShiftRows(state, inv=True)
        state = SubBytes(state, inv=True)
        state = AddRoundKey(state, KeyEndec, rnd)
        state = MixColumns(state, inv=True)

        rnd -= 1
        

    state = ShiftRows(state, inv=True)
    state = SubBytes(state, inv=True)
    state = AddRoundKey(state, KeyEndec, rnd)

    output = [None for i in range(4 * nb)]
    for r in range(4):
        for c in range(nb):
            output[r + 4 * c] = state[r][c]

    return output


def SubBytes(state, inv=False):

    if inv == False:  
        box = Sbox
    else:  
        box = InvSbox

    for i in range(len(state)):
        for j in range(len(state[i])):
            row = state[i][j] // 0x10
            col = state[i][j] % 0x10

            BoxElem = box[16 * row + col]
            state[i][j] = BoxElem

    return state


def ShiftRows(state, inv=False):

    count = 1

    if inv == False:  
        for i in range(1, nb):
            state[i] = LeftShift(state[i], count)
            count += 1
    else:  
        for i in range(1, nb):
            state[i] = RightShift(state[i], count)
            count += 1

    return state


def MixColumns(state, inv=False):

    for i in range(nb):
        if inv == False:  
            s0 = Mul02(state[0][i]) ^ Mul03(state[1][i]) ^ state[2][i] ^ state[3][i]            
            s1 = state[0][i] ^ Mul02(state[1][i]) ^ Mul03(state[2][i]) ^ state[3][i]
            s2 = state[0][i] ^ state[1][i] ^ Mul02(state[2][i]) ^ Mul03(state[3][i])
            s3 = Mul03(state[0][i]) ^ state[1][i] ^ state[2][i] ^ Mul02(state[3][i])
            
        else:  
            s0 = Mul0e(state[0][i]) ^ Mul0b(state[1][i]) ^ Mul0d(state[2][i]) ^ Mul09(state[3][i])
            s1 = Mul09(state[0][i]) ^ Mul0e(state[1][i]) ^ Mul0b(state[2][i]) ^ Mul0d(state[3][i])
            s2 = Mul0d(state[0][i]) ^ Mul09(state[1][i]) ^ Mul0e(state[2][i]) ^ Mul0b(state[3][i])
            s3 = Mul0b(state[0][i]) ^ Mul0d(state[1][i]) ^ Mul09(state[2][i]) ^ Mul0e(state[3][i])

        state[0][i] = s0
        state[1][i] = s1
        state[2][i] = s2
        state[3][i] = s3

    return state


def KeyExpansion(key):

    KeySymbols = [ord(symbol) for symbol in key]

    if len(KeySymbols) < 4 * nk:
        for i in range(4 * nk - len(KeySymbols)):
            KeySymbols.append(0x01)

    KeyEndec = [[] for i in range(4)]
    for r in range(4):
        for c in range(nk):
            KeyEndec[r].append(KeySymbols[r + 4 * c])

    for col in range(nk, nb * (nr + 1)):  
        if col % nk == 0:
            tmp = [KeyEndec[row][col - 1] for row in range(1, 4)]
            tmp.append(KeyEndec[0][col - 1])

            for j in range(len(tmp)):
                SboxRow = tmp[j] // 0x10
                SboxCol = tmp[j] % 0x10
                SboxElem = Sbox[16 * SboxRow + SboxCol]
                tmp[j] = SboxElem

            for row in range(4):
                s = (KeyEndec[row][col - 4]) ^ (tmp[row]) ^ (Rcon[row][int(col / nk - 1)])
                KeyEndec[row].append(s)

        else:
            for row in range(4):
                s = KeyEndec[row][col - 4] ^ KeyEndec[row][col - 1]
                KeyEndec[row].append(s)

    return KeyEndec


def AddRoundKey(state, KeyEndec, round=0):

    for col in range(nk):
        s0 = state[0][col] ^ KeyEndec[0][nb * round + col]
        s1 = state[1][col] ^ KeyEndec[1][nb * round + col]
        s2 = state[2][col] ^ KeyEndec[2][nb * round + col]
        s3 = state[3][col] ^ KeyEndec[3][nb * round + col]

        state[0][col] = s0
        state[1][col] = s1
        state[2][col] = s2
        state[3][col] = s3

    return state

def LeftShift(array, count):

    res = array[:]
    for i in range(count):
        temp = res[1:]
        temp.append(res[0])
        res[:] = temp[:]

    return res


def RightShift(array, count):

    res = array[:]
    for i in range(count):
        tmp = res[:-1]
        tmp.insert(0, res[-1])
        res[:] = tmp[:]

    return res


def Mul02(num):

    if num < 0x80:
        res = (num << 1)
    else:
        res = (num << 1) ^ 0x1b

    return res % 0x100


def Mul03(num):

    return (Mul02(num) ^ num)


def Mul09(num):

    return Mul02(Mul02(Mul02(num))) ^ num


def Mul0b(num):

    return Mul02(Mul02(Mul02(num))) ^ Mul02(num) ^ num


def Mul0d(num):

    return Mul02(Mul02(Mul02(num))) ^ Mul02(Mul02(num)) ^ num


def Mul0e(num):

    return Mul02(Mul02(Mul02(num))) ^ Mul02(Mul02(num)) ^ Mul02(num)


def readFile(file, ifBinary):
    byte = ''
    data = []

    while True:
        byte = file.read(1)
        if byte == '':
            break
        if ifBinary:
            data.append(ord(byte))
        else:
            data.append(byte)
    return data

def workFile(keyFile,nameFile,EnDec):
    print keyFile
    print nameFile
    print EnDec
    inputFile = open(nameFile, 'rb')
    inputData = readFile(inputFile, True)
    if  len(inputData) == 0:
        sys.exit
    keyInFile = open(keyFile, 'r')
    key = readFile(keyInFile, False)
    if len(key) == 0 or len(key) > 16:
        sys.exit
    encryptOrNot = True
    action = EnDec
    if action == '1' or action == '2':
        if action == '2':
            encryptOrNot = False
        else:
            sys.exit

    arrayOf16ByteBlocks = []
    while len(inputData) % 16 != 0:
        inputData.append(0x00)

    sixteenByteBlock = []
    for item in inputData:
        sixteenByteBlock.append(item)
        if len(sixteenByteBlock) == 16:
            arrayOf16ByteBlocks.append(sixteenByteBlock)
            sixteenByteBlock = []

    outputData = []

    if encryptOrNot:
        for item in arrayOf16ByteBlocks:
            sixteenByteBlock = encrypt(item, key)

            for byte in sixteenByteBlock:
                outputData.append(byte)
    else:
        for item in arrayOf16ByteBlocks:
            sixteenByteBlock = decrypt(item, key)

            for byte in sixteenByteBlock:
                outputData.append(byte)

        while outputData[len(outputData) - 1] == 0x0:
            outputData.pop();

    currentPath = os.path.dirname(os.path.abspath(__file__))
    outputFileName = currentPath + '//' + nameFile

    if encryptOrNot:
        outputFileName += '_1.txt'
    else:
        outputFileName += '_2.txt'

    outputFile = open(outputFileName, 'wb')

    for item in outputData:
        outputFile.write(chr(item))

    outputFile.close()
    return True

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
	self.title('aes')
	self.geometry('300x200')
	self.textNameFile = tk.Label(self, text = "Input file: ")
	self.textKeyFile = tk.Label(self, text = "Key file: ")
        self.entryNameFile = tk.Entry(self)
        self.entryKeyFile = tk.Entry(self)
        self.buttonEncrypt = tk.Button(self, text="Encrypt", command=self.on_button_encrypt)
        self.buttonDecrypt = tk.Button(self, text="Decrypt", command=self.on_button_decrypt)

	self.textNameFile.place(x = 10, y = 10)
        self.entryNameFile.place(x = 100, y = 10)
	self.textKeyFile.place(x = 10, y = 50)
        self.entryKeyFile.place(x = 100, y = 50)
        self.buttonEncrypt.place(x = 10, y = 100)
        self.buttonDecrypt.place(x = 100, y = 100)

    def on_button_encrypt(self):
        keyFile = self.entryKeyFile.get()
	if len(keyFile) == 0:
            sys.exit()
        nameFile = self.entryNameFile.get()
	if len(nameFile) == 0:
            sys.exit()
        EnDec = '1'
        final = workFile(keyFile,nameFile, EnDec)
        tkMessageBox.showinfo("Success!","File is encrypted.")

    def on_button_decrypt(self):
        keyFile = self.entryKeyFile.get()
	if len(keyFile) == 0:
            sys.exit()
        nameFile = self.entryNameFile.get()
	if len(nameFile) == 0:
            sys.exit()
	EnDec = '2'
        final = workFile(keyFile,nameFile, EnDec)
        tkMessageBox.showinfo("Success!","File is decrypted.")

app = SampleApp()
app.mainloop()

