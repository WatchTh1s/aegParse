# -*- coding: utf-8 -*-

from local_imports.methods import init
from local_imports.methods import getSCFileList
from local_imports.methods import parsesc
import os
import re

def main ( ):
        

    opts = init()
    # os.chdir(".\lex")
   
    SCFileList=getSCFileList(opts.sdir, opts.isdebug, opts.uselist)    
    
    
    for sc in SCFileList:
        #Generate a list of objects for every NPC in current file
        print ("Parsing file "+sc)
        #Generating lexical file
        lex=parsesc(os.path.abspath(sc), opts.isdebug, opts.forceout)
         
        
        
    
    


if __name__ == "__main__":
    main()