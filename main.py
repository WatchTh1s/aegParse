# -*- coding: utf-8 -*-

from local_imports.methods import initopts
from local_imports.methods import getSCFileList
from local_imports.methods import parsesc
import os
#import re
from local_imports.aegLex import aegLex
#from local_imports.aegYacc import aegParser

def main ( ):
        
    SCFileLists = []
    opts = initopts()
    for source in opts.sdir:
        SCFileLists.append(getSCFileList(source, opts.isdebug, opts.uselist))    

    #Init lexical parser    
    aeglexer = aegLex()
    #aeglexer.build()
    
    #Init parser
    #aegparser = aegParser()

    for sclist in SCFileLists:
        for sc in sclist:
            #Generate a list of objects for every NPC in current file
            print ("Parsing file "+sc)
            #Generating lexical file
            result = parsesc(os.path.abspath(sc), opts.isdebug, opts.forceout
                        , aeglexer
                        )
             
            
            
    
    #print (str(SCFileList.__len__()) + "  files lexic parsed")
    
    #Here is token by token comparsion of .lex-files
    


if __name__ == "__main__":
    main()