#!/usr/bin/python3

#first level message processing program. this processes incoming data from sensors, visual, audio, sonar etc

# by christopher Rehm. 15 dec 2019

import os
import sys
import time
import grendelconfig as gc

run = True
while (run == True):
    print("starting message handling loop now")
    #check for incoming new message
    newMsgs = os.listdir(gc.msgPathPY)
    #print(newMsgs)
    #print ('***********')
    for each in newMsgs:
        mymessage = gc.message.read(each,"PY")

        # select a processing program and a location to run  process
        if mymessage[1] == "newfoto":
            #print(msgDataPiece)
            print("sending new foto data for processing")
            #send off command to do process
        elif mymessage[1] == "newaudio":
            print("sending new audio data for processing")
            #send off command to do process
        elif mymessage[1] == "newtext":
            print("sending new text data for processing")
            #send off command to do process
        elif mymessage[1] == "shutdownGrendel":
            #save any data
            sys.exit()
        else:
            print("I don't know how to process that data")
            print(mymessage)
            x= input("blabblah")
    mytime = time.time()
    mymessage = gc.message
    mymessage.write(mytime,"testttttt","arggggg blahblahblah and blah", "AI", "!" , "PY","NOONE", "NONE")
    myanswer = input("any key to continue")
    #move message to processed folder
    os.system('mv ' + gc.msgPathPY + "/" + each + ' ' + gc.msgPath + '/processedMsgs/')
    #do it again
