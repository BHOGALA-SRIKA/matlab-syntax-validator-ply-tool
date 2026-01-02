import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    'program : statement_list'
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : function_declaration
                 | loop
                 | selection
                 | print_statement
                 | return_statement'''
    p[0] = p[1]

def p_function_declaration(p):
    'function_declaration : FUNCTION ID LPAREN RPAREN LBRACE statement_list RBRACE'
    p[0] = ('function_declaration', p[2], p[6])

def p_loop(p):
    '''loop : FOR LPAREN ID RPAREN LBRACE statement_list RBRACE
            | WHILE LPAREN ID RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('loop', p[1], p[3], p[6])

def p_selection(p):
    '''selection : IF LPAREN ID RPAREN LBRACE statement_list RBRACE
                 | IF LPAREN ID RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    else:
        p[0] = ('if_else', p[3], p[6], p[10])

def p_print_statement(p):
    'print_statement : PRINT LPAREN ID RPAREN SEMICOLON'
    p[0] = ('print', p[3])

def p_return_statement(p):
    'return_statement : RETURN ID SEMICOLON'
    p[0] = ('return', p[2])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}' on line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()