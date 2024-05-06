%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
extern void yyerror(const char *s);
%}

%token IF 
%token ELSE 
%token PRINT 
%token REPEAT 
%token VAR 
%token READ 
%token LPAREN 
%token RPAREN 
%token LBRACE 
%token RBRACE 
%token COMMA 
%token EQ 
%token GT 
%token LT 
%token AND 
%token OR 
%token PLUS 
%token MINUS 
%token MULT 
%token DIV 
%token ASSIGN 
%token NOT 
%token INT 
%token STRING 
%token IDENTIFIER 
%token NEWLINE 
%token PUSH_UPS 
%token SQUATS 
%token PLANK 
%token CRUNCHES LUNGES

%%

program: EXERCISE_ROUTINE
        | program EXERCISE_ROUTINE;

block : NEWLINE EXERCISE_ROUTINES ;

EXERCISE_ROUTINES : EXERCISE_ROUTINE
                  | EXERCISE_ROUTINES EXERCISE_ROUTINE ;

EXERCISE_ROUTINE : assign
                 | print
                 | repeat
                 | if  
                 | exercise_instruction ;

assign : IDENTIFIER ASSIGN bexpression NEWLINE
       | VAR IDENTIFIER ASSIGN bexpression NEWLINE
       | VAR IDENTIFIER NEWLINE ;

print : PRINT LPAREN bexpression RPAREN NEWLINE ;

repeat : REPEAT LPAREN INT RPAREN LBRACE block RBRACE NEWLINE 
       | REPEAT LPAREN IDENTIFIER RPAREN LBRACE block RBRACE NEWLINE;

if : IF LPAREN bexpression RPAREN LBRACE block RBRACE ELSE LBRACE block RBRACE NEWLINE
   | IF LPAREN bexpression RPAREN block NEWLINE ;

bexpression : bexpression OR bterm
            | bterm ;

bterm : bterm AND rexpression
      | rexpression ;

exercise_instruction : PUSH_UPS LPAREN INT RPAREN NEWLINE
                     | SQUATS LPAREN INT RPAREN NEWLINE
                     | PLANK LPAREN INT RPAREN NEWLINE
                     | CRUNCHES LPAREN INT RPAREN NEWLINE
                     | LUNGES LPAREN INT RPAREN NEWLINE ;

rexpression : rexpression EQ expression
            | rexpression GT expression
            | rexpression LT expression
            | expression ;

expression : expression PLUS term
           | expression MINUS term
           | term ;

term : term MULT factor
     | term DIV factor
     | factor ;

factor : PLUS factor
       | MINUS factor
       | NOT factor
       | INT 
       | STRING 
       | LPAREN bexpression RPAREN
       | IDENTIFIER 
       | READ LPAREN RPAREN ;

%%

void yyerror(const char *s) {
    extern int yylineno;
    extern char *yytext;

    /* mensagem de erro exibe o símbolo que causou erro e o número da linha */
    printf("\nErro (%s): símbolo \"%s\" (linha %d)\n", s, yytext, yylineno);
}

int main() {
    yyparse();
    return 0;
}
