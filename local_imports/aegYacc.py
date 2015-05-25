# -*- coding: utf-8 -*-
import ply.yacc as yacc
from local_imports.aegLex import aegLex


class aegParser:
    def __init__(self):
        self.lexer = aegLex()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self,write_tables=0,debug=False)

    def parse(self,data):
        if data:
            return self.parser.parse(data,self.lexer.lexer,0,0,None)
        else:
            return []

    def p_error(self,p):
        print ('Error!')
        print (p)
        print

    def p_rule_npc(self,p):
        #""" : """
        'npc : AEG_NPC AEG_STR AEG_STR AEG_NPCBMP AEG_INT AEG_INT AEG_INT AEG_INT AEG_INT'
        p[0] = p[1]
        
    def p_rule_string(self,p):
        #""" : """
        '''string : string '+' AEG_IDENT 
                | AEG_IDENT + string
                | AEG_STR'''
        
        p[0] = p[1]
    
    def p_rule_dialog(self,p):
        #""" : """
        '''dialog : DIALOG string 
                | DIALOG AEG_STR'''
        
        p[0] = p[1]
        
    def p_statement_assign(self,p):
        'statement : NAME "=" expression'
#        names[p[1]] = p[3]
