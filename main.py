# -*- coding: utf-8 -*-

from local_imports.methods import initopts
from local_imports.methods import getSCFileList
from local_imports.methods import parsesc
import os
import re
from local_imports.aegLex import aegLex
from local_imports.aegYacc import aegParser

def main ( ):
        

    opts = initopts()
   
    SCFileList=getSCFileList(opts.sdir, opts.isdebug, opts.uselist)    

    #Init lexical parser    
    #aeglexer = aegLex()
    #aeglexer.build()
    
    #Init parser
    aegparser = aegParser()
    
    for sc in SCFileList:
        #Generate a list of objects for every NPC in current file
        print ("Parsing file "+sc)
        #Generating lexical file
        lex=parsesc(os.path.abspath(sc), opts.isdebug, opts.forceout
                    , aegparser
                    )
         
        
        
    
    


if __name__ == "__main__":
    main()