import re

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.current_char = source[0] if source else None

    def advance(self):
        self.position += 1
        self.current_char = self.source[self.position] if self.position < len(self.source) else None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_token(self):
        self.skip_whitespace()

        if self.current_char is None:
            return Token('EOF', None)

        if self.current_char.isalpha():
            return self.get_identifier_or_keyword()

        if self.current_char.isdigit():
            return self.get_number()

        if self.current_char == '=':
            self.advance()
            return Token('ASSIGN', '=')

        if self.current_char == '(':
            self.advance()
            return Token('LPAREN', '(')

        if self.current_char == ')':
            self.advance()
            return Token('RPAREN', ')')

        if self.current_char == '{':
            self.advance()
            return Token('LBRACE', '{')

        if self.current_char == '}':
            self.advance()
            return Token('RBRACE', '}')

        if self.current_char == '>':
            self.advance()
            return Token('GT', '>')

        if self.current_char == '+':
            self.advance()
            return Token('PLUS', '+')

        if self.current_char == '-':
            self.advance()
            return Token('MINUS', '-')

        if self.current_char == '*':
            self.advance()
            return Token('MULTIPLY', '*')

        if self.current_char == '/':
            self.advance()
            return Token('DIVIDE', '/')

        if self.current_char == '"':
            self.advance()
            return self.get_string()

        self.error()

    def get_identifier_or_keyword(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        if result in ('print', 'while', 'if', 'else', 'then', 'do', 'end', 
            'not', 'read', 'or', 'and', 'local', 'repeat', 'var', 
            'push_ups', 'squats', 'plank', 'crunches', 'lunges'):
            return Token(result.upper(), result)
        return Token('IDENTIFIER', result)

    def get_number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token('NUMBER', int(result))

    def get_string(self):
        result = ''
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # Skip closing quote
        return Token('STRING', result)

    def error(self):
        raise Exception(f'Unexpected character: {self.current_char}')
