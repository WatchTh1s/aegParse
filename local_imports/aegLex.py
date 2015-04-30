# -*- coding: utf-8 -*-
import ply.lex as lex
import re


#Additional idents   

reserved = {
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
}

literals = "+-*[]()"+['/{1}']
 
tokens = [

#Commentaries
"AEG_COMMENT",
#Basic
"AEG_NPC",
#Define vartypes
"AEG_INT",
"AEG_STR",
"AEG_BOOL",
#Define operators
#"AEG_SEMICOLON",
"AEG_COMMA",
"AEG_SETVAL",
"AEG_COMPARES",
"AEG_BOOLOPS",
"AEG_GLOBALVARS",
"AEG_NPCEVENT",

#"AEG_NPCBMP",
#Everything else
"AEG_IDENT"
] + list(reserved.values())

#Lex tokens definitions
#This is all GLOBAL tokens tha CAN be used


t_ignore = '\ \t\f'
t_AEG_NPC = r'npc'
t_AEG_NPCEVENT = 'On[a-zA-Z]*?:'
t_AEG_GLOBALVARS = 'v\[[0-9a-zA-Z_]+?\]'
#Commentaries
def t_AEG_COMMENT(t):
    r'\/\/\.+'
    pass
#Define vartypes
def t_AEG_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t
t_AEG_STR = r'"(\\.|[^"])*"'
#t_AEG_NPCBMP = r'[0-9]{1}[0-9A-Z_]*'
#Define operators
t_AEG_SETVAL = r'\='
#t_AEG_SEMICOLON = r':'
t_AEG_COMMA = r'\,'
t_AEG_COMPARES = r'\>|\<|>=\<=|==|<>|!='
t_AEG_BOOLOPS = r'\||&&|&'

def t_AEG_IDENT(t):
    r'[a-zA-Z_0-9_]\w*'
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
