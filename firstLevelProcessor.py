#!/usr/bin/python3

#first level message processing program. this processes incoming data from sensors, visual, audio, sonar etc

# by christopher Rehm. 15 dec 2019

import os
import sys
#import time
import grendelconfig as gc

DEBUG = True

############################################################

def shutdownMe():
    gc.debugBreakPoint("Closing down first level processor", "FLP")
    pass

def activateCam1():
    pass

def activateCam2():
    pass

def activateHearing():
    pass

def deactivateHearing():
    pass

def sendInternetInquiry():
    pass

def moveHead():
    pass

def moveWiglaf():
    pass

def moveAsmo():
    pass

def recieveInternet():
    pass

def processFoto():
    pass

def ProcessInfo():
    pass

def ProcessVideo():
    pass

def ProcessHumanspeech():
    pass

def shutdown():
    pass

########################################################
firsttime =  True
run = True
while (run == True):
    gc.debugBreakPoint("Starting PY loop", "firstLevelProcessor")
    #check for incoming new message
    newMsgs = os.listdir(gc.msgPathPY)
    gc.debugBreakPoint("-+-+-+-+-+-++ starting firstlevelprocessor-+-+-+-+-+-+-+-+-", "FLP")
    if firsttime == True:
        os.chdir(gc.msgPathPY)
        gc.makeMsg("PY","Py startup","starting py program","3", "AI" ,"NOONE", "NONE")
        firsttime = False
    gc.debugBreakPoint("Now getting messages for flp","flp")
    for each in newMsgs:
        mymessage = gc.message()
        if DEBUG == True: print(each)
        mydata = mymessage.read(each,"PY")
        # select a processing program and a location to run  process
        if mymessage.title == "newfoto":
            #print(msgDataPiece)
            if DEBUG == True: print("sending new foto data for processing")
            #send off command to do process
        elif mymessage.title == "newaudio":
            if DEBUG == True: print("sending new audio data for processing")
            #send off command to do process
        elif mymessage.title == "newtext":
            if DEBUG == True: print("sending new text data for processing")
            #send off command to do process
        elif mymessage.title == "shutdown":
            #save any data
            shutdownMe()
            sys.exit()
        else:
            if DEBUG == True: print("I don't know how to process that data")
            pass#
        #move message to processed folder
        os.system('mv ' + gc.msgPathPY + "/" + each + ' ' + gc.msgPath + '/processedMsgs/')
    gc.makeMsg("PY","testttttt","arggggg blahblahblah and blah","7", "AI" ,"NOONE", "NONE")
    gc.debugBreakPoint("End loop" , "firstLevelProcessor")
    #do it again