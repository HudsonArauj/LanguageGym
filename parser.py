from tokenizer import Tokenizer, Token

class Node:
    def evaluate(self, st):
        pass

class Program(Node):
    def __init__(self, routines):
        self.routines = routines

    def evaluate(self, st):
        for routine in self.routines:
            routine.evaluate(st)

class VarDecl(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def evaluate(self, st):
        st.set(self.name, self.value.evaluate(st))

class Assignment(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def evaluate(self, st):
        st.set(self.name, self.value.evaluate(st))

class Print(Node):
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, st):
        print(self.expression.evaluate(st))

class Repeat(Node):
    def __init__(self, times, routines):
        self.times = times
        self.routines = routines

    def evaluate(self, st):
        for _ in range(self.times.evaluate(st)):
            for routine in self.routines:
                routine.evaluate(st)

class If(Node):
    def __init__(self, condition, if_routines, else_routines=None):
        self.condition = condition
        self.if_routines = if_routines
        self.else_routines = else_routines

    def evaluate(self, st):
        if self.condition.evaluate(st):
            for routine in self.if_routines:
                routine.evaluate(st)
        elif self.else_routines:
            for routine in self.else_routines:
                routine.evaluate(st)

class Number(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return self.value

class Identifier(Node):
    def __init__(self, name):
        self.name = name

    def evaluate(self, st):
        return st.get(self.name)

class BinaryOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def evaluate(self, st):
        if self.op == '+':
            return self.left.evaluate(st) + self.right.evaluate(st)
        if self.op == '-':
            return self.left.evaluate(st) - self.right.evaluate(st)
        if self.op == '*':
            return self.left.evaluate(st) * self.right.evaluate(st)
        if self.op == '/':
            return self.left.evaluate(st) / self.right.evaluate(st)
        if self.op == '>':
            return self.left.evaluate(st) > self.right.evaluate(st)
        if self.op == '==':
            return self.left.evaluate(st) == self.right.evaluate(st)
        raise Exception(f'Unknown binary operator: {self.op}')

class String(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return self.value

class ExerciseInstruction(Node):
    def __init__(self, name, reps):
        self.name = name
        self.reps = reps

    def evaluate(self, st):
        print(f"Do {self.reps.evaluate(st)} reps of {self.name}")

class Parser:
    def __init__(self, source):
        self.tokenizer = Tokenizer(source)
        self.current_token = self.tokenizer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.tokenizer.get_next_token()
        else:
            # print(self.current_token.type)  # Debugging
            self.error(token_type)

    def error(self, token_type):
        raise Exception(f'Expected token {token_type}, got {self.current_token.type}')

    def parse(self):
        routines = []
        while self.current_token.type != 'EOF':
            routines.append(self.parse_exercise_routine())
        return Program(routines)

    def parse_exercise_routine(self):
        if self.current_token.type == 'VAR':
            return self.parse_var_decl()
        if self.current_token.type == 'IDENTIFIER':
            return self.parse_assignment()
        if self.current_token.type == 'PRINT':
            return self.parse_print()
        if self.current_token.type == 'REPEAT':
            return self.parse_repeat()
        if self.current_token.type == 'IF':
            return self.parse_if()
        self.error('Exercise Routine')

    def parse_var_decl(self):
        self.eat('VAR')
        name = self.current_token.value
        self.eat('IDENTIFIER')
        self.eat('ASSIGN')
        value = self.parse_expression()
        return VarDecl(name, value)

    def parse_assignment(self):
        name = self.current_token.value
        self.eat('IDENTIFIER')
        self.eat('ASSIGN')
        value = self.parse_expression()
        return Assignment(name, value)

    def parse_print(self):
        self.eat('PRINT')
        self.eat('LPAREN')
        expression = self.parse_expression()
        self.eat('RPAREN')
        return Print(expression)

    def parse_repeat(self):
        self.eat('REPEAT')
        self.eat('LPAREN')
        times = self.parse_expression()
        self.eat('RPAREN')
        self.eat('LBRACE')
        routines = []
        while self.current_token.type != 'RBRACE':
            routines.append(self.parse_exercise_routine())
        self.eat('RBRACE')
        return Repeat(times, routines)

    def parse_if(self):
        self.eat('IF')
        self.eat('LPAREN')
        condition = self.parse_expression()
        self.eat('RPAREN')
        self.eat('LBRACE')
        if_routines = []
        while self.current_token.type != 'RBRACE':
            if_routines.append(self.parse_exercise_routine())
        self.eat('RBRACE')
        else_routines = None
        if self.current_token.type == 'ELSE':
            self.eat('ELSE')
            self.eat('LBRACE')
            else_routines = []
            while self.current_token.type != 'RBRACE':
                else_routines.append(self.parse_exercise_routine())
            self.eat('RBRACE')
        return If(condition, if_routines, else_routines)

    def parse_expression(self):
        node = self.parse_term()
        while self.current_token.type in ('PLUS', 'MINUS', 'GT', '=='):
            op = self.current_token.value
            self.eat(self.current_token.type)
            node = BinaryOp(node, op, self.parse_term())
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            op = self.current_token.value
            self.eat(self.current_token.type)
            node = BinaryOp(node, op, self.parse_factor())
        return node

    def parse_factor(self):
        token = self.current_token
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return Number(token.value)
        if token.type == 'IDENTIFIER':
            self.eat('IDENTIFIER')
            return Identifier(token.value)
        if token.type == 'STRING':
            self.eat('STRING')
            return String(token.value)
        if token.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.parse_expression()
            self.eat('RPAREN')
            return node
        self.error('Factor')
    
    
    def parse_exercise_instruction(self):
        name = self.current_token.type
        if name == 'PUSH_UPS':
            self.eat('PUSH_UPS')
        elif name == 'SQUATS':
            self.eat('SQUATS')
        elif name == 'PLANK':
            self.eat('PLANK')
        elif name == 'CRUNCHES':
            self.eat('CRUNCHES')
        elif name == 'LUNGES':
            self.eat('LUNGES')
        else:
            self.eat('IDENTIFIER')
        self.eat('LPAREN')
        reps = self.parse_expression()
        self.eat('RPAREN')
        return ExerciseInstruction(name, reps)

    def parse_exercise_routine(self):
        if self.current_token.type == 'VAR':
            return self.parse_var_decl()
        if self.current_token.type == 'IDENTIFIER':
            return self.parse_assignment()
        if self.current_token.type == 'PRINT':
            return self.parse_print()
        if self.current_token.type == 'REPEAT':
            return self.parse_repeat()
        if self.current_token.type == 'IF':
            return self.parse_if()
        if self.current_token.type in ('PUSH_UPS', 'SQUATS', 'PLANK', 'CRUNCHES', 'LUNGES'):
            return self.parse_exercise_instruction()
        self.error('Exercise Routine')
