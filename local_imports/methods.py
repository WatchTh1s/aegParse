# -*- coding: utf-8 -*-

import os, argparse, re
#from local_imports.Classes import aegNPC
#from re import split
#from local_imports.aegYacc import aegParser



def initopts():
#Initialization of options    
    optParser = argparse.ArgumentParser(description='Aegis vocabulary generator')

    optParser.add_argument(
                 '-l', 
                 '--list-txt', 
                 required=False,
                 action='store_true',
                 default=False,
                 dest='uselist',
                 help="Relative path to list.txt files ", 
                 )

    optParser.add_argument(
                 '-s', 
                 '--sdir', 
                 required=True,
                 dest='sdir',
                 nargs=2,
                 help="Directory where source files are stored SDIR.\n Have to comply with list.txt option", 
                 )

    optParser.add_argument(
                 '-d', 
                 '--dfile-path',
                 required=False,
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
                 help="Additional processing information.", 
                 )

    optParser.add_argument(
                 '-f', 
                 '--forced-out', 
                 required=False,
                 action='store_true',
                 default=False,
                 dest='forceout',
                 help="Rewrite output files if exist.", 
                 )
    
    opts = optParser.parse_args()
    
    #Getting REAL paths
    for idx, sdir in enumerate(opts.sdir):
        if not os.path.isdir(sdir):
            raise BaseException("List of source direcroties contains invalid path ")
        else:
            sdir = os.path.abspath(sdir)
            opts.sdir.pop(idx)
            opts.sdir.insert(idx,sdir)
            print('Source path is '+ sdir)
    if opts.dfilepath:
        dfilePath = os.path.abspath(opts.dfilepath)
        #Checking our file for being writeable
        if not os.path.exists(dfilePath):
            try:
                opts.dfile=open(dfilePath, 'w')
                opts.dfilepath=dfilePath
            except:
                raise BaseException("Can't open file "+opts.sdir+" for writing.")
        elif os.path.exists(dfilePath ) and opts.forceout:
            try:
                open(dfilePath, 'w+').close()
            except:
                raise BaseException("Can't open existing file "+dfilePath+" for writing.")
        elif os.path.exists(dfilePath) and not opts.forceout:
            raise BaseException("Can't use existing output file w/o --force")
    return opts




#Return all *sc files in given directories
def getSCFileList(sdirs, isdebug, uselist):
    aegScriptList=[]   
    if not uselist:
        #for dir in sdirs:
            for folder in dir:
                for root, dirs, filenames in os.walk(folder):
                    for filename in filenames:    
                        if re.match('^.*\.sc$', filename) : 
                            aegScriptList.append(os.path.abspath(os.path.join(root,filename)))
                            if isdebug:
                                print("Added file "+os.path.abspath(os.path.join(root,filename))+" to list.")
        
    else:

        listpath=(os.path.join(sdirs,"list.txt"))
        fileopened = open(listpath)
        fileopened = fileopened.readlines()
        for string in fileopened:

            if not re.match(r'^;.*|\s', string):
                car = os.path.join(sdirs,"..",string)
                aegScriptList.append(car.strip())
        
    print (str(aegScriptList.__len__()) + " files found.")
    return aegScriptList

#Parse code
def parsesc (sc, 
             isdebug, 
             forceout, 
             aeglexer,
             #aegparser
             ):
    
    #fileopened = open(sc)
    data = open(sc).read()
    

    #Following line is for lexer teseting only
    result=aeglexer.Process(data)
    #result=aegParser.parse(data)

    if isdebug:
        #Write lexems into file
        lexfilename = os.path.abspath(sc)+".lex"
        try:
            Writef(result, lexfilename, forceout)
        except:
            raise
    
    return result

def Writef(result, dfile, forceout):
        if forceout and os.path.exists(dfile):
            try:
                os.remove(dfile)
            except:
                raise BaseException("Can't remove existing lexical file.")
        try:
            fileopened = open(dfile,'a')
        except:
            raise BaseException("Can't create lexical file.")
        
        for line in result:
            fileopened.write(str(line)+"\n")
        fileopened.close()