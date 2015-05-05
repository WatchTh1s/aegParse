# -*- coding: utf-8 -*-
import ply.lex as lex
import re


#Additional idents   

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
   'choose menu'    : 'CH_MENU_START',
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
"AEG_COLOR",
#Define vartypes
"AEG_INT",
"AEG_STR",
"AEG_BMP",
#Define operators
"AEG_SEMICOLON",
"AEG_DIVISION",
"AEG_COMMA",
"AEG_SETVAL",
"AEG_COMPARES",
"AEG_BOOLOPS",
#Everything else
"AEG_IDENT"
] + list(reserved.values())

#Lex tokens definitions
#This is all GLOBAL tokens tha CAN be used


t_ignore = ' \t\f'
t_AEG_NPC = r'npc'
t_AEG_DIVISION = r'\/\s'
#Commentaries
def t_AEG_COMMENT(t):
    r'\/\/.*\n|\/\/|\/\/.*\r'
    pass
#Define vartypes
def t_AEG_INT(t):
    r'\d+[\s\,\/]'
    t.value = int(t.value)
    return t
t_AEG_STR = r'"([^"])*"'
t_AEG_BMP = r'[0-9]{1}_[a-zA-Z0-9_]*'
#Define operators
t_AEG_SETVAL = r'\='
t_AEG_COLOR = 'r\^[0-9A-F]{6}'
t_AEG_SEMICOLON = r':'
t_AEG_COMMA = r'\,'
t_AEG_COMPARES = r'\>|\<|>=\<=|==|<>|!='
t_AEG_BOOLOPS = r'\||&&|&'

def t_AEG_IDENT(t):
    r'[a-zA-Z0-9_\']\w*'
    t.type = reserved.get(t.value,'AEG_IDENT')    # Check for reserved words
    return t

def t_newline(t):
    r'[\n\r]+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print ("Illegal character '%s'" % t.value[0]+" "+str(t.lexer.lineno))
    t.lexer.skip(1)

def Process(data):
    lexer = lex.lex(reflags=re.UNICODE | re.DOTALL)
    ParsedTokens=[]
    lexer.input(data)
    
    while True:
        tok = lexer.token() # читаем следующий токен
        if not tok: break      # закончились печеньки
        ParsedTokens.append(tok)
    return ParsedTokens
