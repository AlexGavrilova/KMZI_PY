import sys, os

if len(sys.argv) != 5:
    print "Invalid arguments! Enter <input_file.txt> <output_file.txt> <1> (or <2>) <key>."
    sys.exit(0)

if not os.path.isfile(sys.argv[1]) :
    print "Cannot open file: ", sys.argv[1]
    sys.exit(0)

inputFile = open(sys.argv[1],'r')
ch = inputFile.read(1)

outputFile = open(sys.argv[2], 'w')

if (sys.argv[3] != '1') and (sys.argv[3] != '2'):
    print "Error! Enter <1> - encryption or <2> - decryption."
    sys.exit(0)
    
strKey = sys.argv[4]
key = []

for i in range(len(strKey)):
    key.append(ord(strKey[i]))

for i in range(len(key)):
    while len(ch) != 0:
        if (sys.argv[3] == '1'):
            brr = (ord(ch) + key[i]) % 256
        if (sys.argv[3] == '2'):
            brr = ((ord(ch) - key[i]) + 256) % 256
        outputFile.write(chr(brr))
        ch = inputFile.read(1)
        if i == len(key):
            i = 0

inputFile.close()
outputFile.close()


