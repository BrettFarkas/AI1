#FARKAS UNIVERSL NETWORK, F.U.N.
#DEMONSTRATION HERE: https://www.youtube.com/watch?v=yEr52Ce3u64
#EXAMPLE PROGRAM SHOWING THE BASICS OF THE SYSTEM
#SEE NOTES AT THE END FOR IDEAS FOR IMPROVEMENTS

import pygame, sys
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Cause/Effect Neural Network")
screen = pygame.display.set_mode((930,500),0,32)
clock = pygame.time.Clock()
                                 #A PROGRAM WHICH CONNECTS NEURONS BASED ON WHEN THEY ARE ACTIVATED
                                                        #By Brett Farkas

#COLORS
Green = (0,250,154)
Yellow = (255,255,0)
Red = (220,20,60)
Blue = (30,144,255)
DarkBlue = (0,0,255)
Gray = (108,123,139)
global NeuronStop
NeuronStop = 0
global startDrawX
global startDrawY
global unusedneurons
unusedneurons = 5
global i
global x
global y
global z
MakeANewNeuron=0
####################################################################################### THE BUTTONS
#buttons=[(50,450),(200,450),(350,450),(500,450),(650,450),(800,450)] 40 wide
#x for neurons ellipses: 70, 220, 370, 520, 670, 820 (add 150 each time)20 wide


NeuronCenters= [(90,470),(240,470),(390,470),(540,470),(690,470),(840,470),
                (90,360),(240,360),(390,360),(540,360),(690,360),(840,360),
                (90,300),(240,300),(390,300),(540,300),(690,300),(840,300),
                (90,250),(240,250),(390,250),(540,250),(690,250),(840,250),
                (90,200),(240,200),(390,200),(540,200),(690,200),(840,200),
                (90,150),(240,150),(390,150),(540,150),(690,150),(840,150),
                (90,100),(240,100),(390,100),(540,100),(690,100),(840,100),
                (90,50),(240,50),(390,50),(540,50),(690,50),(840,50)]


NeuronColor=[DarkBlue,DarkBlue,DarkBlue,DarkBlue,DarkBlue,DarkBlue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,
Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue,Blue]


####################################################################################### THE NEURONS (48 total)

NeuronActive = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
NeuronActivatedTime = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
NeuronNewlyActivated = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

NeuronCurrentActivationLevel = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
NeuronActivationThreshold = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#NeuronPartialActivationStartTime = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

OutgoingNeuronsConnectedTo = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

OutgoingNeuronStrength = [[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5],[.5]]
#[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]

IncomingNeuronsConnectedTo =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

IncomingNeuronsActivated =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]#to figure out how many in the chain have been activated, need to use this when a neuron is first activated, send it out to this array

IncomingNeuronStrength = [ [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[] ]

TopOfTheChain= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

SimultaneousNeuronsConnectedTo=[ [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[] ]#when it is lit simultaneously with others that are not at the top of a chain

#######################################################################################

#TO DO : 
#
#
#



global milli

while True: 
        #time
#       clock.get_time()
        
        #milli = clock.tick()
        #seconds = milli/1000.0
#       milli= clock.get_rawtime()

#       milli=clock.get_time()
        milli = pygame.time.get_ticks()

        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                        #points.append(event.pos) #appends the mouse coordinate to the list of points USE THIS TO ADD NEURONS

                        x,y = pygame.mouse.get_pos() #this gets the coordinates of the mouse arrow

                        #####################################################################################################
                        # MAKE THE BUTTONS ACTIVE
                        if x > 50 and x < 50 + 80:
                                if y > 450 and y < 490: 
                                        NeuronActive[0] = 1
                                        NeuronActivatedTime[0] = milli
                                        NeuronNewlyActivated[0] = 1
                                        TopOfTheChain[0] = 1

                        elif x > 200 and x < 200 + 80:
                                if y > 450 and y < 490: 
                                        NeuronActive[1] = 1
                                        NeuronActivatedTime[1] = milli
                                        NeuronNewlyActivated[1] = 1
                                        TopOfTheChain[1] = 1

                        elif x > 350 and x < 350 + 80:
                                if y > 450 and y < 490: 
                                        NeuronActive[2] = 1
                                        NeuronActivatedTime[2] = milli
                                        NeuronNewlyActivated[2] = 1
                                        TopOfTheChain[2] = 1
                                                                        
                                        

                        elif x > 500 and x < 500 + 80:
                                if y > 450 and y < 490: 
                                        NeuronActive[3] = 1
                                        NeuronActivatedTime[3] = milli
                                        NeuronNewlyActivated[3] = 1
                                        TopOfTheChain[3] = 1

                        elif x > 650 and x < 650 + 80:
                                if y > 450 and y < 490: 
                                        NeuronActive[4] = 1
                                        NeuronActivatedTime[4] = milli
                                        NeuronNewlyActivated[4] = 1
                                        TopOfTheChain[4] = 1

                        elif x > 800 and x < 800 + 80:
                                if y > 450 and y < 490: 
                                        NeuronActive[5] = 1
                                        NeuronActivatedTime[5] = milli
                                        NeuronNewlyActivated[5] = 1
                                        TopOfTheChain[5] = 1
                                        

        #########################################################################################################################
        #Turn On half activated
        for i in range(6,48):
                if NeuronCurrentActivationLevel[i] >= NeuronActivationThreshold[i] : #turn on partially activated neurons that are above 1
                        NeuronActive[i] = 1
                        NeuronActivatedTime[i] = milli
                        NeuronNewlyActivated[i] = 1 #tell that the neuron has just now been activated
                        TopOfTheChain[i] = 1
                        
                        for x in range(0,len(IncomingNeuronsActivated[i])): #turns off the top of the chain in older neurons    
                                if(IncomingNeuronsActivated[i][x] == 1):
                                        TopOfTheChain[IncomingNeuronsConnectedTo[i][x]] = 0
                                        
                                        
                        NeuronCurrentActivationLevel[i] = 0 #should change this later on, instead of resetting it, to pass the activation upwards                       
                        for x in range(0,len(IncomingNeuronsConnectedTo[i])): #turns off the top of the chain in older neurons  
                                if(IncomingNeuronsActivated[i][x] == 1):
                                        TopOfTheChain[IncomingNeuronsConnectedTo[i][x]] = 0

        ########################################################################################################################
        #CONNECT TO A NEW THIRD NEURON
        #unused neurons = 6                                             
                        
        for i in range(0,48):
                if NeuronNewlyActivated[i] == 1: #(if it's newly activated)
                                        
#PSEUDOCODE: TO DO LATER: If primary is already connected to an active ThirdNeuron in its forward list, reinforce the connection.

                        #If it does not have one that it should, (check the primary's forward connections against the currently lit ones), then create a new one.
                        for x in range(0,48):
                                if NeuronActive[x] == 1 and x != i: #(don't connect to itself, old neuron lit is X, new one is I
                                        if TopOfTheChain[x] == 1 : #if it is the neuron at the top of a chain
                                                
                                        #FIGURE OUT WHICH THIRD NEURONS IT IS ALREADY CONNECTED TO
                                        #Look at the Last Neuron in the incoming connection list
                                                

#                                               
                                                                
                                                                        
#                                               elif(len(IncomingNeuronsConnectedTo[x]) > 0):
#                                                       for z in range(0,len(IncomingNeuronsConnectedTo[x])):
#                                                               if (IncomingNeuronsConnectedTo[x][z] == i):
#                                                                       MakeANewNeuron = 0 
#                                                               else: 
#                                                                       MakeANewNeuron = 1 # if there is not already an incoming connection
#                                               else:
#                                                       MakeANewNeuron = 1
                                                        
                                                NeuronStop = 0
                                        #Check to see if it (i) is already connected to the old one (x) directly in the incoming list
                                                if (len(IncomingNeuronsActivated[x]) > 0):
                                                        for z in range(1,len(IncomingNeuronsActivated[x])):
                                                                
                                                                if (IncomingNeuronsActivated[x][z] == 0 and IncomingNeuronsActivated[x][z-1] == 1):
                                                                        
                                                                        if (IncomingNeuronsConnectedTo[x][z] == i):
                                                                                MakeANewNeuron = 0
                                                                                NeuronStop = 1
                                                                                
                                                                                break
                                                                        else: 
                                                                                MakeANewNeuron = 1
                                                                                
                                                                                break
                                                                elif (IncomingNeuronsActivated[x][z] == 1 and len(IncomingNeuronsActivated[x]) == z + 1): #if it has reached the end of the incoming neurons list
                                                                #if i is already directly connected to x
                                                                        if (IncomingNeuronsConnectedTo[x][z] == i):
                                                                                MakeANewNeuron = 0
                                                                                NeuronStop = 1
                                                                        else: 
                                                                                MakeANewNeuron = 1
                                                                                
                                #This finds third neurons that are already connected to an old active one
                                #NEED TO COMPARE THE ORDER OF 0 AND 1 IN THIS STATEMENT 
                                                if(len(OutgoingNeuronsConnectedTo[x]) > 0):#if there are any outgoing neurons
                                                        for z in range(0,len(OutgoingNeuronsConnectedTo[x])):
                                                                if(len(IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[x][z]]) > 0):
                                                                        for w in range(1,len(IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[x][z]])): 
                                                                                
                                                                                if (IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[x][z]][w] == i and IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[x][z]][w-1] == x ):#and IncomingNeuronsActivated[OutgoingNeuronsConnectedTo[x][z]][w-1] == 1): #if there is already an outgoing connection to that neuron                                    
                                                                                        MakeANewNeuron = 0 #if any one is a match, this = 0
                                                                                        NeuronStop = 1 
                                                                                        
                                                                                        
                                                                                        break
                                                                                else: 
                                                                                        MakeANewNeuron = 1 # if there is not already an outgoing connection to the old neuron   
                                                                                        
                                                                                        

                                                else: 
                                                        MakeANewNeuron = 1
                                                        
                                                        
                                        elif (TopOfTheChain[x] != 1): #the simultaneous neuron code goes here, it is not at the top at the chain but is active
                                                        SimultaneousNeuronsConnectedTo[unusedneurons].append(x)#append the old neuron x to the simultaneous list                
                                                        
                                        if (MakeANewNeuron == 1 and unusedneurons <= 48 and NeuronStop!=1): 
                                                
                                                
                                                unusedneurons += 1 #CREATING A NEW NEURON HERE, TURN IT ON 
                                                NeuronActive [unusedneurons] = 1
                                                NeuronNewlyActivated[unusedneurons] = 1
                                                NeuronActivatedTime[unusedneurons] = milli
                                                #print unusedneurons
                                                

                                                IncomingNeuronsConnectedTo[unusedneurons].append(x) #add the first lit neuron to the incoming
                                                IncomingNeuronsConnectedTo[unusedneurons].append(i) #add the second lit neuron to the incoming
                                                IncomingNeuronsActivated[unusedneurons].append(1)
                                                IncomingNeuronsActivated[unusedneurons].append(1)

                                                IncomingNeuronStrength[unusedneurons].append(.5) #.5 for now, can adjust it later
                                                IncomingNeuronStrength[unusedneurons].append(.5) #the strength for backtracking a connection, the second one here is the second connection, listed second like the second incoming neuron is
                                                
                                                OutgoingNeuronsConnectedTo[x].append(unusedneurons)
                                                OutgoingNeuronsConnectedTo[i].append(unusedneurons)
                                                OutgoingNeuronStrength[x].append(.5)
                                                OutgoingNeuronStrength[i].append(.5)

                                                TopOfTheChain[unusedneurons] = 1 #the new top of the chain
                                                TopOfTheChain[i] = 0 #turn off the old neuron
                                                TopOfTheChain[x] = 0 #turn off the newer neuron

                                                MakeANewNeuron = 0      
                                                
                                                
                                                

                        #PSEUDOCODE: The NEW one is in ThirdNeuronArray.  It should have the old neuron listed first, plus the new neuron.
                                        #append new ones to the incoming list [unusedneuron]
                                        #also append to the outgoing list on the original neuron X
                        #PSEUDOCODE: Don't create neurons past #48
#PSEUDOCODE: Handle the simultaneous array.  They each have their own strengths to fire the neuron. 
#PSEUDOCODE: The simultaneous neurons' strengths are divided by the number of neurons, and rounded up?  Or the triggering will work if the value is at least above .9                   
                                                

        #########################################################################################################################
        # If a Neuron is Newly Activated then Half-Activate Neurons Up the Chain and also Below It
        #note- reset the activation time on a neuron when it is hit again with the NeuronPartialActivationStartTime[]


        for i in range(0,48):
                if NeuronNewlyActivated[i] == 1:
                        if (len(OutgoingNeuronsConnectedTo[i]) > 0):

                                



                                #Half-Activate the neurons higher up (the ones in the outgoing list)
                                for x in range(0,len(OutgoingNeuronsConnectedTo[i]) ): # I is the name of the list, X are the items in it
                                                                                
                                        if (len(IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[i][x]]) > 0):
                                                for y in range(0,len(IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[i][x]])):
                                                        if (IncomingNeuronsActivated[OutgoingNeuronsConnectedTo[i][x]][y] == 0):
                                                                if(IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[i][x]][y] == i):
                                                                        NeuronCurrentActivationLevel[OutgoingNeuronsConnectedTo[i][x]] = NeuronCurrentActivationLevel[OutgoingNeuronsConnectedTo[i][x]] + OutgoingNeuronStrength[i][x]
                                                                        
                                                                        IncomingNeuronsActivated[OutgoingNeuronsConnectedTo[i][x]][y] = 1 #mark the incoming neuron as activated
                                                                break



                        #MARK THE INCOMING NEURONS ACTIVATED                                    
                                #mark incoming neurons activated (mark the original on the higher ups' list)
#                               for z in range(0, len(OutgoingNeuronsConnectedTo[i])):
#                                       for w in range(0,len(IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[i][z]])):
#                                               if (IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[i][z]][w] == i):#if it finds the incoming neuron
#                                                       IncomingNeuronsActivated[OutgoingNeuronsConnectedTo[i][z]][w] = 1 #mark the incoming neuron as activated
                                
                        #RESET THE TIME ON THE NEURON FARTHER UP (as it keeps getting hit by other neurons the time keeps resetting)
                                        #NeuronActivatedTime[OutgoingNeuronsConnectedTo[i][x] ] = milli

                        #HALF-ACTIVATING THE INCOMING NEURONS (down below)
                        if(len(IncomingNeuronsConnectedTo[i]) > 0):
                                for x in range(0,len(IncomingNeuronsConnectedTo[i]) ): # I is the name of the list, X are the items in it
                                        NeuronCurrentActivationLevel[IncomingNeuronsConnectedTo[i][x]] = NeuronCurrentActivationLevel[IncomingNeuronsConnectedTo[i][x]] + IncomingNeuronStrength[i][x]  # This confusing thing half-activates down to the incoming neurons
                                        
                        NeuronNewlyActivated[i] = 0 #reset the newly activated tag so it doesn't keep adding

                        
        #########################################################################################################################
        #REINFORCE CONNECTIONS and DIMINISH THEM(or put this with the third neuron connection code
        #PSEUDOCODE: If a half-activated neuron gets activated, then reinforce it. Also increase the threshold. If it doesn't, then diminish it.
                #  if the connection strength gets really weakened then delete the connection off the appended incoming and outgoing lists

        #For GOOD connections, Reinforce them a lot, or maybe add a separate activation list that will max them

        ##########################################################################################################################
        #Turn old Neurons OFF, Change Neuron Colors
        for i in range(0,48):
                if NeuronActive[i] == 1 : 
                        NeuronColor[i] = Red #turn active neurons Red
                        if milli - NeuronActivatedTime[i] > 2000:#can make the times different for different neurons in the future
                                NeuronActive[i] = 0
                                NeuronColor[i] = Blue
                                TopOfTheChain[i] = 0 #top of chain switched off
                                NeuronCurrentActivationLevel[i] = 0                             
                                
                                

                                #this turns off partial activations on upwards neurons, subtracts from their activation
                                if (len(OutgoingNeuronsConnectedTo[i]) > 0):
                                        for x in range(0,len(OutgoingNeuronsConnectedTo[i]) ): # I is the name of the list, X are the items in it
                                                for w in range(0,len(IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[i][x]])): #if the neuron is actually activating the neuron above it, then subtract away
                                                        if(IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[i][x]][w] == i and IncomingNeuronsActivated[OutgoingNeuronsConnectedTo[i][x]][w] == 1):
                                                                NeuronCurrentActivationLevel[OutgoingNeuronsConnectedTo[i][x]] = NeuronCurrentActivationLevel[OutgoingNeuronsConnectedTo[i][x] ] - OutgoingNeuronStrength[i][x] #subtracts away from the activation level
                                                                

                                #incoming neurons activated turned off
                                if(len(IncomingNeuronsActivated[i]) > 0):#This turns off the IncomingNeuronsActivated list in a targeted way
                                        for z in range(0, len(IncomingNeuronsActivated[i])):
                                                IncomingNeuronsActivated[i][z] = 0
                                
                                #turns off incoming neurons activated list in a targeted way
                                if(len(OutgoingNeuronsConnectedTo[i]) > 0):
                                        for z in range(0, len(OutgoingNeuronsConnectedTo[i])):
                                                for w in range(0,len(IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[i][z]])):
                                                        if (IncomingNeuronsConnectedTo[OutgoingNeuronsConnectedTo[i][z]][w] == i):
                                                                IncomingNeuronsActivated[OutgoingNeuronsConnectedTo[i][z]][w] = 0



                        #if (IncomingNeuronsActivated[i] > 0): #This turns off the IncomingNeuronsActivated list
                        #       for x in range (0,len(IncomingNeuronsActivated[i]) ):
                        #               IncomingNeuronsActivated[i][x] = 0                      
                
                else:
                        if NeuronCurrentActivationLevel[i] > 0 : #half-activated neurons are Yellow
                                NeuronColor[i] = Yellow
                        if i < 6:
                                NeuronColor[i] = DarkBlue #buttons are darkblue
                        else:
                                NeuronColor[i] = Blue

        
                

        ############################################################################################################################            
        #DRAW GREEN LINES BETWEEN CONNECTED NEURONS - need to make Simultaneous a different color like gray)
        for i in range(6,48): #this is going to draw the lines twice, once from each neuron, can fix that later
                if (len(SimultaneousNeuronsConnectedTo[i]) > 0):
                        for x in range(0,len(SimultaneousNeuronsConnectedTo[i])):
                                
                                if (NeuronActive[i] >= 1 and NeuronActive[SimultaneousNeuronsConnectedTo[i][x]] >= 1 or NeuronCurrentActivationLevel[i] > 0 or  NeuronCurrentActivationLevel[SimultaneousNeuronsConnectedTo[i][x]] > 0): #draws yellow lines
                                        pygame.draw.line(screen,Yellow,NeuronCenters[i],NeuronCenters[SimultaneousNeuronsConnectedTo[i][x]],5)
                                else: 
                                        pygame.draw.line(screen,Gray,NeuronCenters[i],NeuronCenters[SimultaneousNeuronsConnectedTo[i][x]],5)


#draws a green line from the original to the next one

        for i in range(0,48): #this is going to draw the lines twice, once from each neuron, can fix that later
                if (len(OutgoingNeuronsConnectedTo[i]) > 0 ):
                        for x in range(0,len(OutgoingNeuronsConnectedTo[i])):# I is the name of the list, X are the items in it
                                
                                if (NeuronActive[i] >= 1 and NeuronActive[OutgoingNeuronsConnectedTo[i][x]] >= 1 or NeuronCurrentActivationLevel[i] > 0 or  NeuronCurrentActivationLevel[OutgoingNeuronsConnectedTo[i][x]] > 0): #draws yellow lines
                                        pygame.draw.line(screen,Yellow,NeuronCenters[i],NeuronCenters[OutgoingNeuronsConnectedTo[i][x]],5)
                                        
                                else: 
                                        pygame.draw.line(screen,Green,NeuronCenters[i],NeuronCenters[OutgoingNeuronsConnectedTo[i][x]],5)#draws a green line from the original to the next one

        #NeuronCenters[i]
        #pygame.draw.line(screen,(176,23,31),(500,250),(600,250),5)
        
        #pygame.draw.line(screen,Green,(Connection1X,Connection1Y),(Connection2X,Connection2Y),5)

        #DRAW THE GREEN LINES (before you draw the neurons)
        #connections=[(90,470),(240,360)]#testing the green line
        #pygame.draw.line(screen,Green,connections[0],connections[1],5)
        
        #DRAW THE HALF ACTIVATED LINES


        ############################################################################################################################
        
        # DRAW NEURONS (# 6-48, 42 total)
        startDrawX=70
        startDrawY = 350
        for i in range (6,48): 
                pygame.draw.ellipse(screen, NeuronColor[i], (startDrawX,startDrawY,40,20), 0)
                startDrawX = startDrawX + 150
                if startDrawX > 820: #reset startDraw to draw the next row up
                        startDrawX=70
                        startDrawY = startDrawY - 50

                
        

        # DRAW BUTTONS
        buttonstart = 50
        for i in range(0,6):
                pygame.draw.ellipse(screen, NeuronColor[i], (buttonstart,450,80,40), 0)
                buttonstart = buttonstart + 150




        

        pygame.display.update()


#Copyright 2012 Brett Farkas
#This program is free software: you can redistribute it and/or modify
 #   it under the terms of the GNU General Public License as published by
  #  the Free Software Foundation, either version 3 of the License, or
   # (at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.
#
 #   You should have received a copy of the GNU General Public License
  #  along with this program.  If not, see <http://www.gnu.org/licenses/>.

#NOTES: TO ADD: IF SOMETHING GOOD HAPPENS THEN IT REINFORCES THE NEURONS LEADING TO IT BY A LARGE AMOUNT
#               IF SOMETHING BAD IS AVOIDED THEN THAT IS GOOD (if a half-activated bad is avoided because of an action)
                #CREATE A LOT OF INPUTS AND 100,000 NEURONS (THE SAME AMOUNT OF NEURONS AS A FRUIT FLY'S BRAIN)
                #WHAT SHOULD THE RATIO BE OF INPUTS TO NEURONS?
                #CAN WORK ON ADJUSTING VARIABLES SUCH AS THE DURATION OF A NEURON'S LIT TIME, AND REINFORCEMENT STRENGTHS
                #CAN DO AWAY WITH THE 'TOP OF THE CHAIN' IF TOP ONES STAY LIT LONGER?
                #AN ALTERNATIVE TO 'TOP OF THE CHAIN' IS TO HAVE LOWER LEVEL ONES SWITCH OFF IMMEDIATELY, THEY GIVE THEIR LIGHT AWAY
                #CURRENTLY THE ACTIVATION LEVEL OF THE NEURON IS PUT BACK AT ZERO AFTER THE NEURON HAS BECOME ACTIVE.  IN THE FUTURE THE NEURON COULD PASS ITS ACTIVATION UPWARDS LIKE A BATON
                #THERE SHOULD BE A SHORT TERM MEMORY SECTION WITH A FINITE SET NUMBER OF NEURONS, AND THEN A LONG TERM SET OF NEURONS THAT IS INFORMED BY THE SHORT TERM INFORMATION.  IT RECORDS THE HIGHER-LEVEL CONNECTIONS?  COULD HAVE ONE SET OF NEURONS THAT TAKE IN LIGHT DATA, THEN ANOTHER SET OF SOME OTHER SENSOR DATA, AND ONLY ALLOW CROSS CONNECTIONS AT THE HIGHEST LEVELS?

#need to revise OutgoingNeuronStrength to allow for changing values, changing strengths

#problem- The 'top of the chain' lets a large chain of neurons build up, but it ignores smaller independent connections that could form even though 
#there is other stuff going on before it.  The chain would be ABCD, but maybe CD would be a good connection on its own, it's ignored.

#for the final version: make all the arrays dyanamic, including the number of neurons.  The user can decide how many inputs they want at the beginning and everything else will just adjust.  The user also designates what is good and what is bad.





#


