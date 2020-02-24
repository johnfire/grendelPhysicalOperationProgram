#!/usr/bin/python3

#first level message processing program. this processes incoming data from sensors, visual, audio, sonar etc

# by christopher Rehm. 15 dec 2019

import os
import sys
import time
import grendelconfig as gc

def makeMsg(title, text, primeRecipient, priority, otherRecievers, files):
    mytime = time.time()
    mymessage = gc.message()
    mymessage.write(mytime, title, text,primeRecipient, priority, "PY", otherRecievers, files)


firsttime =  True
run = True
while (run == True):
    print("starting message handling loop now")
    gc.debugBreakPoint("PY1")
    #check for incoming new message
    newMsgs = os.listdir(gc.msgPathPY)
    #print(newMsgs)
    #print ('***********')
    if firsttime == True:
        makeMsg("Py startup","starting py program","AI", "3" ,"NOONE", "NONE")
        firsttime = False
    for each in newMsgs:
        mymessage = gc.message()
        mymessage.read(each,"PY")
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
            #print(mymessage)
            makeMsg("testttttt","arggggg blahblahblah and blah","AI", "!" ,"NOONE", "NONE")
            gc.debugBreakPoint("PY2")
        #move message to processed folder
        os.system('mv ' + gc.msgPathPY + "/" + each + ' ' + gc.msgPath + '/processedMsgs/')
    #do it again