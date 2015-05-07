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

    def p_rule_0(self,p):
        """symbol1 : symbol2"""
        p[0] = p[1]