# -*- coding: utf-8 -*-

import os, argparse, re
from test.test_pep277 import filenames


def init():
#Initialization of options    
    optParser = argparse.ArgumentParser(description='Aegis vocabulary generator')

    optParser.add_argument(
                 '-s', 
                 '--sdir', 
                 required=True,
                 nargs='+',
                 dest='sdir',
                 help="Directory where source files are stored SDIR", 
                 )

    optParser.add_argument(
                 '-d', 
                 '--dfile-path',
                 required=True,
                 dest='dfilepath',
                 help='Dest file to where dictionary should be put DFILE', 
                 )

    optParser.add_argument(
                 '-b', 
                 '--debug',
                 required=False,
                 action='store_true',
                 default=False,
                 dest='isdebug',
                 help="Dest file to where dictionary should be put DFILE", 
                 )

    optParser.add_argument(
                 '-f', 
                 '--forced-out', 
                 required=False,
                 action='store_true',
                 default=False,
                 dest='forceout',
                 help="Dest file to where dictionary should be put DFILE", 
                 )
    
    opts = optParser.parse_args()
    
    #Getting REAL paths
    for sdir in opts.sdir:
        if not os.path.isdir(sdir):
            raise BaseException("List of source direcroties contains invalid path "+sdir)
        else:
            opts.sdir
            #----------------------------------- opts.sdir=os.path.abspath(sdir)
            
            print('Source path is '+ sdir)
    
    dfilePath = os.path.abspath(opts.dfilepath)
    #Checking our file for being writeable
    if not os.path.exists(dfilePath):
        try:
            opts.dfile=open(dfilePath, 'w')
            opts.dfilepath=dfilePath
        except:
            raise BaseException("Can't open file "+sdir+" for writing.")
    elif os.path.exists(dfilePath ) and opts.forceout:
        try:
            open(dfilePath, 'w+').close()
        except:
            raise BaseException("Can't open existing file "+dfilePath+" for writing.")
    elif os.path.exists(dfilePath) and not opts.forceout:
        raise BaseException("Can't use existing output file w/o --force")
    return opts

#Return all *sc files in given directories
def getSCFileList(sdirs, isdebug):
    aegScriptList=[]    
    for folder in sdirs:
        for root, dirs, filenames in os.walk(folder):
            for filename in filenames:    
                if re.match('^.*\.sc?', filename) : 
                    aegScriptList.append(os.path.abspath(os.path.join(root,filename)))
                    if isdebug:
                        print("Added file "+os.path.abspath(os.path.join(root,filename))+" to list.")
    return aegScriptList

#Dummy
def parsesc (sc):
    return 1