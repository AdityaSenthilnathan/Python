WordCount = ""
def Wordcountfromfile(file):
    F = open(str(file))
    ReadF = F.read()
    splitF = ReadF.split()
    print(len(splitF))

Wordcountfromfile("test.txt")