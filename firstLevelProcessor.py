#!/usr/bin/python3

# first level message processing program.
# this processes incoming data from sensors, visual, audio, sonar etc

# by christopher Rehm. 15 dec 2019

import os
import sys
# import time
import grendelShares.grendelconfig as gc
import grendelShares.i2cComm as i2CC
import subprocess
import datetime

DEBUG = True


############################################################
def shutdownMe():
    gc.debugBreakPoint("Closing down first level processor", "FLP")
    pass


def activateCam1(numberOfFotos, sleepTime):
    subprocess.call("/media/grendel102/grendelSmallPrograms/camN.py", numberOfFotos, sleepTime)


def activateCam2(numberOfFotos, sleepTime):
    subprocess.call("/media/grendel102/grendelSmallPrograms/camIR.py", numberOfFotos, sleepTime)


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
firsttime = True
run = True
gc.debugBreakPoint("-+-+-+starting firstlevelprocessor+-+-+-", "FLP")
if firsttime is True:
    os.chdir(gc.msgPathPY)
    gc.makeMsg("PY",
               "Py startup",
               "starting py program",
               "3",
               "AI",
               "NOONE",
               "NONE")
    firsttime = False
while (run is True):
    gc.debugBreakPoint("Starting PY loop", "firstLevelProcessor")
    # check for incoming new message
    print(datetime.datetime.now().time())
    gc.debugBreakPoint("Now getting messages for flp", "flp")
    newMsgs = os.listdir("/media/grendelData102/GrendelData/grendelMsgs/PY")
    for each in newMsgs:
        mymessage = gc.message()
        if DEBUG is True: print(each)
        mydata = mymessage.read(each, "PY")
        # select a processing program and a location to run  process
        if mymessage.title == "newfoto":
            # print(msgDataPiece)
            if DEBUG is True: print("sending new foto data for processing")
            # send off command to do process
        elif mymessage.title == "newaudio":
            if DEBUG is True: print("sending new audio data for processing")
            # send off command to do process
        elif mymessage.title == "newtext":
            if DEBUG is True: print("sending new text data for processing")
            # send off command to do process
        elif mymessage.title == "shutdown":
            os.system('mv ' + gc.msgPathPY + "/" + each + ' ' + gc.msgPath + '/processedMsgs/')
            # save any data
            shutdownMe()
            sys.exit()
        else:
            if DEBUG is True: print("I don't know how to process that data")
        # move message to processed folder
        os.system('mv '
                  + gc.msgPathPY
                  + "/"
                  + each
                  + ' '
                  + gc.msgPath
                  + '/processedMsgs/')
    gc.makeMsg("PY",
               "testttttt",
               "arggggg blahblahblah and blah",
               "7",
               "AI",
               "NOONE",
               "NONE")
    #os.system('mv ' + gc.msgPathPY + "/" + each + ' ' + gc.msgPath + '/processedMsgs/')

    gc.debugBreakPoint("End loop", "firstLevelProcessor")
