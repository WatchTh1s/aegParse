# -*- coding: utf-8 -*-
import ply.lex as lex
import re
#States

state = {
         ("division","exclusive"),
         
         }

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
"AEG_EVENT",
"AEG_COLOR",
#Define vartypes
"AEG_INT",
"AEG_STR",
"AEG_BMP",
#Define operators
"AEG_DIVISION",
"AEG_COMMA",
"AEG_SETVAL",
"AEG_COMPARE",
"AEG_BOOLOPS",
#Everything else
] + list(reserved.values()) + ["AEG_IDENT"]

#Lex tokens definitions
t_ignore = ' \t\f'
t_AEG_NPC = r'npc'
#------------------------------------------------------ def t_begin_division(t):
    #--------------------------------------------------------------------- r'\/'
def t_AEG_COMMENT(t):
        r'/{2}.*?[\n\r]+?|/\*.*\*/'
        pass

def t_AEG_DIVISION(t):
    r'/'
#   t.value = int(t.value)
    return t
#Commentaries
#Define vartypes

t_AEG_STR = r'"([^"])*"'
t_AEG_BMP = r'[0-9]{1}_[a-zA-Z0-9_]*'
#Define operators
t_AEG_SETVAL = r'\='
t_AEG_COLOR = 'r\^[0-9A-F]{6}'

t_AEG_COMMA = r'\,'
t_AEG_COMPARE = r'\>|\<|>=\<=|==|<>|!='
t_AEG_BOOLOPS = r'\||&&|&'

def t_AEG_IDENT(t):
    r'On[a-zA-Z0-9]*\:|[a-zA-Z][a-z0-9A-Z\_\.\']*|[0-9]+_[a-z0-9A-Z_\'\_]*|[a-zA-Z]'
    t.type = reserved.get(t.value,'AEG_IDENT')    # Check for reserved words
    if re.match('On[a-zA-Z0-9]*\:', t.value):
        t.type = 'AEG_EVENT'
    return t

def t_AEG_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'[\n\r]+|\r\n'
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
