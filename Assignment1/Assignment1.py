import os
import time
from threading import Thread

# open log.txt
log = open('log.txt', 'w+')

# slice is 10Kbytes
slice = 10000

current = time.time()


# defining function that copies and pastes in binary format
def binary_copy(fileName, newName):
    init = time.time() - current
    log.write('{:<7.2f}Start copying {} to {}\n'.format(init, fileName, newName))
    file = open(fileName, 'rb')
    newFile = open(newName, 'wb')
    while True:
        bdata = file.read(slice)
        newFile.write(bdata)
        if not bdata:
            break
    end = time.time() - current
    log.write('{:<7.2f}{} is copied completely\n'.format(end, newName))
    newFile.close()


# main loop
while True:
    fileName = input('Input the file name : ')
    if fileName == 'exit':
        exit()
    newName = input('Input the new name : ')
    th = Thread(target=binary_copy, args=(fileName, newName))
    th.start()
