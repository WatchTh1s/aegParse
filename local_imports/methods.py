# -*- coding: utf-8 -*-

import os, argparse, re
from local_imports.Classes import aegNPC
from re import split
from local_imports.aegYacc import aegParser



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
                 help="Directory where source files are stored SDIR.\n Have to comply with list.txt option", 
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

    if not os.path.isdir(opts.sdir):
        raise BaseException("List of source direcroties contains invalid path ")
    else:
        opts.sdir
        opts.sdir=os.path.abspath(opts.sdir)
        
        print('Source path is '+ opts.sdir)

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
        for folder in sdirs:
            for root, dirs, filenames in os.walk(folder):
                for filename in filenames:    
                    if re.match('^.*\.sc$', filename) : 
                        aegScriptList.append(os.path.abspath(os.path.join(root,filename)))
                        if isdebug:
                            print("Added file "+os.path.abspath(os.path.join(root,filename))+" to list.")
        return aegScriptList
    else:

        listpath=(os.path.join(sdirs,"list.txt"))
        fileopened = open(listpath)
        fileopened = fileopened.readlines()
        for string in fileopened:

            if not re.match(r'^;.*|\s', string):
                car = os.path.join(sdirs,"..",string)
                aegScriptList.append(car.strip())
        return aegScriptList

#Parse code
def parsesc (sc, 
             isdebug, 
             forceout, 
             aegparser
             ):
    
    fileopened = open(sc)
    data = fileopened.read()
    fileopened.close()

    #Following line is for lexer teseting only
    #result=aeglexer.Process(code)
    result=aegParser.parse(data)

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