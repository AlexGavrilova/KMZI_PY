import sys, os

if len(sys.argv) != 5:
    print "Incorrect arguments! Enter <input_file.txt> <output_file.txt> <1> (or <2>) <key>."
    sys.exit(0)

if not os.path.isfile(sys.argv[1]):
    print "Cannot open file: ", sys.argv[1]
    sys.exit(0)

inputFile = open(sys.argv[1],'r')
ch = inputFile.read(1)

outputFile = open(sys.argv[2], 'w')

if (sys.argv[3] != '1') and (sys.argv[3] != '2'):
    print "Error! Enter <1> - encryption or <2> - decryption."
    sys.exit(0)

key = int(sys.argv[4])
if(key < 1 or key > 255):
    print "Error! Incorrect key."
    sys.exit(0)

while len(ch) != 0:
    if (sys.argv[3] == '1'):
        brr = (ord(ch) + key) % 256
    if (sys.argv[3] == '2'):
        brr = ((ord(ch) - key) + 256) % 256
    outputFile.write(chr(brr))
    ch = inputFile.read(1)

inputFile.close()
outputFile.close()
