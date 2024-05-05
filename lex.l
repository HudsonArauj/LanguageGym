%{
#include "y.tab.h"
%}

%option noyywrap

%%

[ \t\n]         ; // Ignorar espaços em branco e novas linhas

"var"           { return VAR; }
"print"         { return PRINT; }
"read"          { return READ; }
"repeat"        { return REPEAT; }
"if"            { return IF; }
"else"          { return ELSE; }
"PUSH_UPS"      { yylval.str = strdup(yytext); return EXERCISE_NAME; }
"SQUATS"        { yylval.str = strdup(yytext); return EXERCISE_NAME; }
"PLANK"         { yylval.str = strdup(yytext); return EXERCISE_NAME; }
"CRUNCHES"      { yylval.str = strdup(yytext); return EXERCISE_NAME; }
"LUNGES"        { yylval.str = strdup(yytext); return EXERCISE_NAME; }
"=="            { return EQ; }
">"             { return GT; }
"<"             { return LT; }
"+"             { return PLUS; }
"-"             { return MINUS; }
"*"             { return MULT; }
"/"             { return DIV; }
"("             { return LPAREN; }
")"             { return RPAREN; }

[a-zA-Z_][a-zA-Z0-9_]*   { yylval.str = strdup(yytext); return IDENTIFIER; }
[0-9]+          { yylval.num = atoi(yytext); return NUMBER; }

.               { yyerror("Invalid character"); }

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int yywrap(void) {
    return 1;
}
