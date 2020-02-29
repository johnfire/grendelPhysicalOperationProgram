#!/usr/bin/python3

#first level message processing program. this processes incoming data from sensors, visual, audio, sonar etc

# by christopher Rehm. 15 dec 2019

import os
import sys
#import time
import grendelconfig as gc

firsttime =  True
run = True
while (run == True):
    print("starting message handling loop now")
    gc.debugBreakPoint("starting PY loop", "firstLevelProcessor")
    #check for incoming new message
    newMsgs = os.listdir(gc.msgPathPY)
    gc.debugBreakPoint("-+-+-+-+-+-++ starting firstlevelprocessor-+-+-+-+-+-+-+-+-", "FLP")
    if firsttime == True:
        gc.makeMsg("PY","Py startup","starting py program","AI", "3" ,"NOONE", "NONE")
        firsttime = False
    gc.debugBreakPoint("now gettin messGES for flp","flp")
    for each in newMsgs:
        mymessage = gc.message()
        print(each)
        mydata = mymessage.read(each,"PY")
        # select a processing program and a location to run  process
        if mymessage.title == "newfoto":
            #print(msgDataPiece)
            print("sending new foto data for processing")
            #send off command to do process
        elif mymessage.title == "newaudio":
            print("sending new audio data for processing")
            #send off command to do process
        elif mymessage.title == "newtext":
            print("sending new text data for processing")
            #send off command to do process
        elif mymessage.title == "shutdown":
            #save any data
            sys.exit()
        else:
            print("I don't know how to process that data")
            pass#
        #move message to processed folder
        os.system('mv ' + gc.msgPathPY + "/" + each + ' ' + gc.msgPath + '/processedMsgs/')
        #os.system('mv ' + gc.msgPathAI + "/" + each + ' ' + gc.msgPath + '/processedMsgs/')
    gc.makeMsg("PY","testttttt","arggggg blahblahblah and blah","AI", "!" ,"NOONE", "NONE")
    gc.debugBreakPoint("end loop" , "firstLevelProcessor")
    #do it again