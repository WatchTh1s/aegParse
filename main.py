# -*- coding: utf-8 -*-

from local_imports.methods import init
from local_imports.methods import getSCFileList
from local_imports.methods import parsesc


 
def main ( ):
    opts = init()
    #---------------------------------------------------------- sdirs=opts.sdirs
    SCFileList=getSCFileList(opts.sdir, opts.isdebug)    
    
    for sc in SCFileList:
        dictionary=parsesc(sc)
    
    for line in dictionary:
        opts.dfile.write(line)

    
if __name__ == "__main__":
    main()