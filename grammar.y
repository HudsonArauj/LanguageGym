%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
void yyerror(const char *s);
%}

%union {
    int num;
    char *str;
}

%token <num> NUMBER
%token <str> IDENTIFIER EXERCISE_NAME
%token VAR PRINT READ REPEAT IF ELSE EQ GT LT PLUS MINUS MULT DIV LPAREN RPAREN COMMA SEMICOLON

%type <num> BOOLEAN_EXPRESSION EXPRESSION TERM FACTOR REL_EXPRESSION
%type <str> BOOLEAN_TERM ASSIGNMENT PRINT_STATEMENT READ_STATEMENT REPEAT_STATEMENT IF_STATEMENT ELSE_CLAUSE VARIABLE_DECLARATION EXERCISE_INSTRUCTION EXERCISE_ROUTINE

%%

program: /* empty */ | program exercise_routine;

exercise_routine: assignment SEMICOLON
                | print_statement SEMICOLON
                | read_statement SEMICOLON
                | repeat_statement SEMICOLON
                | if_statement SEMICOLON
                | variable_declaration SEMICOLON
                | exercise_instruction SEMICOLON;

assignment: IDENTIFIER '=' BOOLEAN_EXPRESSION;

print_statement: PRINT LPAREN BOOLEAN_EXPRESSION RPAREN;

read_statement: READ LPAREN RPAREN;

repeat_statement: REPEAT LPAREN NUMBER RPAREN statement_list;

if_statement: IF BOOLEAN_EXPRESSION statement_list else_clause;

else_clause: /* empty */
           | ELSE statement_list;

variable_declaration: VAR IDENTIFIER '=' BOOLEAN_EXPRESSION;

exercise_instruction: EXERCISE_NAME LPAREN NUMBER RPAREN;

statement_list: /* empty */ | statement_list statement;

statement: assignment
         | print_statement
         | read_statement
         | repeat_statement
         | if_statement
         | variable_declaration
         | exercise_instruction;

BOOLEAN_EXPRESSION: BOOLEAN_TERM
                   | BOOLEAN_EXPRESSION OR BOOLEAN_TERM;

BOOLEAN_TERM: REL_EXPRESSION
            | BOOLEAN_TERM AND REL_EXPRESSION;

REL_EXPRESSION: EXPRESSION
              | EXPRESSION EQ EXPRESSION
              | EXPRESSION GT EXPRESSION
              | EXPRESSION LT EXPRESSION;

EXPRESSION: TERM
          | EXPRESSION PLUS TERM
          | EXPRESSION MINUS TERM;

TERM: FACTOR
    | TERM MULT FACTOR
    | TERM DIV FACTOR;

FACTOR: MINUS FACTOR
      | PLUS FACTOR
      | NOT FACTOR
      | NUMBER
      | IDENTIFIER
      | LPAREN BOOLEAN_EXPRESSION RPAREN
      | READ;

NOT: "not";

OR: "or";

AND: "and";

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    yyparse();
    return 0;
}
