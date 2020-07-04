#!/usr/bin/python3

"""Physical processing program.

# first level message processing program.
# this processes incoming data from sensors, visual, audio, sonar etc

# by Christopher Rehm. 15 dec 2019
"""

import os
# import sys
# import time
import grendelShares.grendelconfig as gc
# import grendelShares.i2cComm as i2CC

import subprocess
import datetime


############################################################
def shutdownMe():
    """Shutdown system.

    Returns
    -------
    None.

    """
    gc.debugBreakPoint("Closing down first level processor", "FLP")
    pass


##################################################
def activateCam1(numberOfFotos, sleepTime):
    """Activate camera 1.

    Parameters
    ----------
    numberOfFotos : TYPE
        DESCRIPTION.
    sleepTime : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    # os.system("ssh pi command")
    subprocess.call("/media/grendel102/grendelSmallPrograms/camN.py", numberOfFotos, sleepTime)


###################################################
def activateCam2(numberOfFotos, sleepTime):
    """Activate camera 2.

    Parameters
    ----------
    numberOfFotos : TYPE
        DESCRIPTION.
    sleepTime : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    subprocess.call("/media/grendel102/grendelSmallPrograms/camIR.py", numberOfFotos, sleepTime)


###################################################
def activateHearing():
    """Activate hearing microphones.

    Returns
    -------
    None.

    """
    pass


###################################################
def deactivateHearing():
    """Deactivate hearing microphones.

    Returns
    -------
    None.

    """
    pass


###################################################
def sendInternetInquiry():
    """Send internet inquiry.

    Returns
    -------
    None.

    """
    pass


###################################################
def moveHead(amount, direction):
    """Move head.

    Parameters
    ----------
    amount : TYPE
        DESCRIPTION.
    direction : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    pass


###################################################
def moveWiglaf(distance, direction):
    """Move wieglaf somewhere.

    Parameters
    ----------
    distance : TYPE
        DESCRIPTION.
    direction : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    pass


###################################################
def moveAsmo(distance, direction):
    """Move asmo somewhere.

    Parameters
    ----------
    distance : TYPE
        DESCRIPTION.
    direction : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    pass


###################################################
def recieveInternet(message, info, info2):
    """Recieve internet message.

    Parameters
    ----------
    message : TYPE
        DESCRIPTION.
    info : TYPE
        DESCRIPTION.
    info2 : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    pass


###################################################
def processFoto(message, info, info2):
    """Process a foto.

    Parameters
    ----------
    message : TYPE
        DESCRIPTION.
    info : TYPE
        DESCRIPTION.
    info2 : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    pass


###################################################
# def processInfo():
#     pass


###################################################
def processVideo():
    """Process a video clip.

    Returns
    -------
    None.

    """
    pass


###################################################
def processHumanSpeech(message, info, info2):
    """Process a voice clip.

    Parameters
    ----------
    message : TYPE
        DESCRIPTION.
    info : TYPE
        DESCRIPTION.
    info2 : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    pass


###################################################
# def shutdown():
#     pass


###################################################
def f_default(*args, **kwargs):
    """Execute default message when switch does not work."""
    print("Received a message I have no idea what to do with.")


###################################################
def processMessage(case):
    """Message processing switch function.

    Parameters
    ----------
    case : TYPE
        DESCRIPTION.
    messagePath : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    return {
        "newfoto": processFoto,
        "newaudio": processHumanSpeech,
        "newvideo": processVideo,
        "shutdown": shutdownMe
        }.get(case, f_default)


########################################################
counter = 0
firsttime = True
run = True
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
    # check for incoming new message
    print(datetime.datetime.now().time())
    newMsgs = os.listdir(gc.msgPathPY)
    for each in newMsgs:
        mymessage = gc.message()
        mydata = mymessage.read(each, "PY")
        # select a processing program and a location to run  process
        processMessage(mymessage.title)(gc.message)
        os.system('mv '
                  + gc.msgPathPY
                  + "/"
                  + each
                  + ' '
                  + gc.msgPath
                  + '/processedMsgs/')
    if counter % 100000 == 0:
        gc.makeMsg("PY",
                   "100000 Cycle message",
                   "marks 100000 more cycles from startup",
                   "7",
                   "AI",
                   "NOONE",
                   "NONE")
