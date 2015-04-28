# -*- coding: utf-8 -*-



class aegNPC():
    
    def __init__(self, initline):
        self.code = []
        self.city       = initline[1]
        self.name       = initline[2]
        self.inimage    = initline[3]
        self.x          = initline[4]
        if len(initline)==6:
            self.y          = initline[5]
        if len(initline)==7:
            self.inname     = initline[6]
        if len(initline)==8:
            self.touchx     = initline[7]
        if len(initline)==9:
            self.touchy     = initline[8]
   
