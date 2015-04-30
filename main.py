# -*- coding: utf-8 -*-

from local_imports.methods import init
from local_imports.methods import getSCFileList
from local_imports.methods import parsesc
from local_imports.aegLex import Process
from local_imports.methods import WriteVoc


def main ( ):
    opts = init()
   
    SCFileList=getSCFileList(opts.sdir, opts.isdebug)    
    
    
    for sc in SCFileList:
        #Generate a list of objects for every NPC in current file
        npcs=parsesc(sc)
         
        #inFileTotalNPC = []
        #for npc in npcs:
            #inFileTotalNPC.append(npc)
            #del npc
        fileopened = open(sc)
        code = fileopened.read()
        result=Process(code)
            #result=Process("\n".join(npc.code))
        #Write file vocab
        try:
            WriteVoc(result,opts.dfilepath)
        except:
            raise
            
        # here should be vocabulary generation
        
        del npcs
        
        #-------------------------------------------- for npc in inFileTotalNPC:
            
        #print ("Total list of NPCs generated for file "+sc+". It contains "+str(inFileTotalNPC.__len__())+" items.")
    #--------------------------------------------------- for line in dictionary:
        #------------------------------------------------ opts.dfile.write(line)


    
    
if __name__ == "__main__":
    main()