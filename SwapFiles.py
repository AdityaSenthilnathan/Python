file1nm = input("Enter name of file one")
file2nm = input("Enter name of file one")

def SwapFiles(file1, file2):
    File1 = open(str(file1), "r")
    File1rd = File1.read()
    File2 = open(str(file2), "r")
    File2rd = File2.read()

    File1ch = open(str(file1), "w")
    File2ch = open(str(file2), "w")

    File1ch.write(File2rd)
    File2ch.write(File1rd)
    print("Files have been swapped!")


SwapFiles(str(file1nm), str(file2nm))