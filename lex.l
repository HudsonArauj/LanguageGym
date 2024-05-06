%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "y.tab.h"

char* yyval;

%}
%option yylineno
%option noyywrap


IF if
ELSE else
END end
PRINT print
REPEAT repeat
READ read
VAR var
LPAREN (
RPAREN )
LBRACE {
RBRACE }
COMMA ,
EQ ==
GT >
LT <
AND and
OR or
PLUS +
MINUS -
MULT *
DIV /
ASSIGN =
NOT not
INT [0-9]
STRING \"([^\\\"]|\\.)*\" 
IDENTIFIER [a-zA-Z_][a-zA-Z0-9_]*
NEWLINE \n


%%

[ \t]            ; /* Ignora espaços em branco e tabulações */
"if"             { yyval = strdup(yytext); return IF; }
"else"           { yyval = strdup(yytext); return ELSE; }
"print"         { yyval = strdup(yytext); return PRINT; }
"repeat"        { yyval = strdup(yytext); return REPEAT; }
"read"           { yyval = strdup(yytext); return READ; }
"var"           { yyval = strdup(yytext); return VAR; }
"int"            { yyval = strdup(yytext); return INT; }
"str"            { yyval = strdup(yytext); return STRING; }
"("              { yyval = strdup(yytext); return LPAREN; }
")"              { yyval = strdup(yytext); return RPAREN; }
"{"              { yyval = strdup(yytext); return LBRACE; }
"}"              { yyval = strdup(yytext); return RBRACE; }
","              { yyval = strdup(yytext); return COMMA; }
"=="             { yyval = strdup(yytext); return EQ; }
">"              { yyval = strdup(yytext); return GT; }
"<"              { yyval = strdup(yytext); return LT; }
"and"            { yyval = strdup(yytext); return AND; }
"or"             { yyval = strdup(yytext); return OR; }
"+"              { yyval = strdup(yytext); return PLUS; }
"-"              { yyval = strdup(yytext); return MINUS; }
"*"              { yyval = strdup(yytext); return MULT; }
"/"              { yyval = strdup(yytext); return DIV; }
"="              { yyval = strdup(yytext); return ASSIGN; }
"not"            { yyval = strdup(yytext); return NOT; }

[0-9]+                 { yyval = strdup(yytext); return INT; }
[a-zA-Z_][a-zA-Z0-9_]* { yyval = strdup(yytext); return IDENTIFIER; }
\"([^\\\"]|\\.)*\"     { yyval = strdup(yytext); return STRING; }

#.?\n   ; // Ignora comentários de uma linha */
"\\\n"  ; /* Ignora quebras de linha precedidas por \ */

\n      { yyval = strdup(yytext); return NEWLINE; }
.       { yyval = strdup(yytext); printf("%s",yyval); }

%%

