# -*- coding: utf-8 -*-
import ply.lex as lex
import re
#Reserved words dictionary

class aegLex(object):
    
    
    reserved = {
                
       'broadcastinmap' : 'BCAST',
       'enablenpc'      : 'ENNPC',
       'disablenpc'     : 'DISNPC',
       'cmdothernpc'    : 'CMDNPC',
       'InitTimer'      : 'TINIT',
       'callmonster'    : 'CALLMOB',
       'if'             : 'IF',
       'else'           : 'ELSE',
       'elseif'         : 'ELSEIF',
       'endif'          : 'endIF',
       'while'          : 'WHILE',
       'choose'         : 'CH_MENU_START',
       'menu'           : 'CH_MENU_CONT',
       'endchoose'      : 'CH_MENU_END',
       'break'          : 'BREAK',
       'return'         : 'RETURN',
       'close'          : 'CLOSE',
       'wait'           : 'WAIT',
       'case'           : 'CASE',
       'dialog'         : 'DIALOG',
       'var'            : 'VAR',
       'checkpoint'     : 'CHECKPOINT',
       'getitem'        : 'GETITEM',
       'jobchange'      : 'JOBCHANGE',
       'npc'            : 'NPC',
    }
    
    literals = "%+-*[](){}"
     
    tokens = [
    
    #Commentaries
    "AEG_COMMENT",
    #Basic
    "AEG_NPC",
    "AEG_NPCBMP",
    "AEG_EVENT",
    #"AEG_COLOR",
    #Define vartypes
    "AEG_INT",
    "AEG_STR",
    #Define operators
    "AEG_DIVISION",
    "AEG_COMMA",
    "AEG_SETVAL",
    "AEG_COMPARE",
    "AEG_BOOL",
    #Everything else
    ] + list(reserved.values()) + ["AEG_IDENT"]
    
    #Lex tokens definitions
    t_ignore = ' \t\f'
    t_AEG_NPC = r'npc'
    
    
    #Commentaries
    def t_AEG_COMMENT(self,t):
            r'/{2}.*?[\n\r]+?|/\*(.|[\r\n])*?\*/'
            pass
    
    #In string comments like "MyCuteString#DefinitionOfHellMode cuz i want to do something"... just fuck it
    t_AEG_STR       = r'"([^"\r\n])*"'
    
    #Define operators
    t_AEG_SETVAL    = r'\='
#    t_AEG_COLOR     = 'r\^[0-9A-F]{6}'
    
    t_AEG_COMMA     = r'\,'
    t_AEG_COMPARE   = r'\>|\<|>=\<=|==|<>|!='
    t_AEG_BOOL      = r'\||&&|&'

    def t_AEG_DIVISION(self,t):
        r'/'
        return t
    

    
    def t_AEG_IDENT(self,t):
        r'On[a-zA-Z0-9]*\:|[a-zA-Z][a-z0-9A-Z\_\.\']*|[0-9]+_[a-z0-9A-Z_\'\_]*|[a-zA-Z]'
        t.type = self.reserved.get(t.value,'AEG_IDENT')    # Check for reserved words
        if re.match('On[a-zA-Z0-9]*\:', t.value):
            t.type = 'AEG_EVENT'
        if re.match('[0-9]+_[a-z0-9A-Z_\'\_]*', t.value):
            t.type = 'AEG_NPCBMP'
        return t
    
    def t_AEG_INT(self,t):
        r'\d+'
        t.value = int(t.value)
        return t
    
    def t_newline(self,t):
        r'[\n\r]+|\r\n'
        t.lexer.lineno += len(t.value)
    
    
    def t_error(self,t):
        print ("Illegal character '%s'" % t.value[0]+" "+str(t.lexer.lineno))
        t.lexer.skip(1)
    
    # Build the lexer
    def __init__(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
    
    def Process(self,data):
        ParsedTokens=[]
        self.lexer.lineno = 0
        self.lexer.input(data)
        
        while True:
            tok = self.lexer.token() # читаем следующий токен
            if not tok: break      # закончились печеньки
            ParsedTokens.append(tok)
        return ParsedTokens
