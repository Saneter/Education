'''
Travis Jarratt
CIS 1600 - Fall 2019
Saint Louis University
Assignment 3
'''
import os

filenameone = input("Please enter a filename to encrypt: ")
filenametwo = input("Please enter a filename to write to: ")
filelist = os.listdir('.')
if filenameone in filelist:
    # the file exists
    print("File " + filenameone + " was found and will be read")
    with open(filenameone, 'r') as fn1:
        with open(filenametwo, 'w') as fn2:
            data = fn1.read()
            dataUpper = data.upper()
            print(dataUpper)
            print("Extra credit? ;-)")
            fn2.write(dataUpper)
            fn1.close()
            fn2.close()

else:
    print("The file ", filenameone, " does not exist")
