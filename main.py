# -*- coding: utf-8 -*-

from local_imports.methods import init
from local_imports.methods import getSCFileList
from local_imports.methods import parsesc



 
def main ( ):
    opts = init()
   
    SCFileList=getSCFileList(opts.sdir, opts.isdebug)    
    
    total = []
    for sc in SCFileList:
        npcs=parsesc(sc)
        
        for npc in npcs:
            total.append(npc)
        
        # here should be vocabulary generation
    print ("Total list of NPCs generated")
    #--------------------------------------------------- for line in dictionary:
        #------------------------------------------------ opts.dfile.write(line)


    
    
if __name__ == "__main__":
    main()