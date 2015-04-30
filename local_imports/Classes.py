# -*- coding: utf-8 -*-

from re import match


class aegNPC():
    
    code = []
    
    def __init__(self, initline):
    
        self.location   = initline[0]
        self.name       = initline[1]
        self.inimage    = initline[2]
        self.x          = initline[3]
        if len(initline)>=5:
            self.y          = initline[4]
        if len(initline)>=6:
            self.asimuth     = initline[5]
        if len(initline)>=7:
            self.touchx     = initline[6]
        if len(initline)>=8:
            self.touchy     = initline[7]
   
    def addCodeLine (self, line):
        if not match(r'^npc', line):
            self.code.append(line)
    
    # Dummy method
    def Compare(self,aegNPC):
        
        result = True
        
        return result
    
    #Dummy method
    #------------------------------------------------------- def codeTree(self):
        #------------------------------------------------ for line in self.code:
            #--------------------------------------- if match(r'^On.*\:$',line):
                #--------------------------------------------- state = "isEvent"
                #--------------------------------------------------- self.Code()
#------------------------------------------------------------------------------ 
        #-------------------------------------------------------------- return 1

class Code (aegNPC):
    Events = []
    
    def __init__ (self,Event):
        self.Events = [""]
    def addEvent(self,Event):
        self.Events.append(Event)    