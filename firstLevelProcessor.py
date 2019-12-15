#!/usr/bin/python3

#first level message processing program. this processes incoming data from sensors, visual, audio, sonar etc

# by christopher Rehm. 15 dec 2019

import os
import json

msgPath = "/media/grendelData102/GrendelData/grendelMsgs/"
fotoPath = "/media/grendelData102/GrendelData/grendelFotos/"
audioPath = "/media/grendelData102/GrendelData/grendellAudio/"
grendelOtherData = "/media/grendelData102/GrendelData/grendelOtherData/"
grendelPeopleData = "/media/grendelData102/GrendelData/grendelPeopleData/"

run = True
#os.system('cd')
while (run == True):
    #check for incoming new message
    newMsgs = os.listdir(msgPath)
    #print(newMsgs)
    #print ('***********')
    for each in newMsgs:
        ##need method to check for new messages here, if none loop
        with open(msgPath + each) as f:
            msgData =json.load(f)

        msgType = msgData[0]
        msgDataPiece = msgData[1]
        msgTime =msgData[2]
        msgCreator = msgData[3]
    
        #print(each)
        #print(msgData)
        #print('!!!!!!!!!!!')
        #print (msgType,'   ', msgDataPiece,'   ',msgTime,'    ', msgCreator)


     #if its a kill message, set run level to false and break out of loop, kill program. 
        
        if msgData[0] == "kill":
            run = False
            break  
 
    # select a processing program and a location to run  process

        elif msgData[0] == "newfoto":
            #print(msgDataPiece)
            print("sending new foto data for processing")
            os.system('/media/grendelData102/lowLevelPrograms/processFoto.py '+ msgDataPiece)
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
        #print('////////////')
        #print(each)
        os.system('mv ' + msgPath + each + ' ' + msgPath + 'processedMsgs/')
     #do it again
	
