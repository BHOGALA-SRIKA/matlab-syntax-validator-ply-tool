import ply.lex as lex

# List of token names
tokens = (
    'FUNCTION', 'RETURN', 'IF', 'ELSE', 'FOR', 'WHILE',
    'PRINT', 'ID', 'NUMBER',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'EQUALS'
)

# Regular expression rules for simple tokens
t_FUNCTION = r'function'
t_RETURN = r'return'
t_IF = r'if'
t_ELSE = r'else'
t_FOR = r'for'
t_WHILE = r'while'
t_PRINT = r'print'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'

# Identifier rule
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Number rule
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = ' \t'

# Newline rule
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()