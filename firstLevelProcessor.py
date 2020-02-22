#!/usr/bin/python3

#first level message processing program. this processes incoming data from sensors, visual, audio, sonar etc

# by christopher Rehm. 15 dec 2019

import os
import json
import grendelconfig as gc

run = True
while (run == True):
    print("starting message handling loop now")
    #check for incoming new message
    newMsgs = os.listdir(gc.msgPathPY)
    #print(newMsgs)
    #print ('***********')
    for each in newMsgs:
        if os.path.isfile(gc.msgPathPY + "/" + each):
            ##need method to check for new messages here, if none loop
            with open(gc.msgPathPY + "/" + each) as f:
                msgData =json.load(f)
            #if its a kill message, set run level to false and break out of loop, kill program.
            if msgData[0] == "kill":
                run = False
                break
            # select a processing program and a location to run  process
            elif msgData[0] == "newfoto":
                #print(msgDataPiece)
                print("sending new foto data for processing")
                pass
                #send off command to do process
            elif msgData[0] == "newaudio":
                print("sending new audio data for processing")
                #send off command to do process
            elif msgData[0] == "newtext":
                print("sending new text data for processing")
                #send off command to do process
            else:
                print("I don't know how to process that data")
                print(each)
            #move message to processed folder
            os.system('mv ' + gc.msgPathPY + "/" + each + ' ' + gc.msgPath + '/processedMsgs/')
            #do it again
        else:
            pass
            #do nothing, loop and wait for more messages