/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    IF = 258,                      /* IF  */
    ELSE = 259,                    /* ELSE  */
    PRINT = 260,                   /* PRINT  */
    REPEAT = 261,                  /* REPEAT  */
    VAR = 262,                     /* VAR  */
    READ = 263,                    /* READ  */
    LPAREN = 264,                  /* LPAREN  */
    RPAREN = 265,                  /* RPAREN  */
    LBRACE = 266,                  /* LBRACE  */
    RBRACE = 267,                  /* RBRACE  */
    COMMA = 268,                   /* COMMA  */
    EQ = 269,                      /* EQ  */
    GT = 270,                      /* GT  */
    LT = 271,                      /* LT  */
    AND = 272,                     /* AND  */
    OR = 273,                      /* OR  */
    PLUS = 274,                    /* PLUS  */
    MINUS = 275,                   /* MINUS  */
    MULT = 276,                    /* MULT  */
    DIV = 277,                     /* DIV  */
    ASSIGN = 278,                  /* ASSIGN  */
    NOT = 279,                     /* NOT  */
    INT = 280,                     /* INT  */
    STRING = 281,                  /* STRING  */
    IDENTIFIER = 282,              /* IDENTIFIER  */
    NEWLINE = 283,                 /* NEWLINE  */
    PUSH_UPS = 284,                /* PUSH_UPS  */
    SQUATS = 285,                  /* SQUATS  */
    PLANK = 286,                   /* PLANK  */
    CRUNCHES = 287,                /* CRUNCHES  */
    LUNGES = 288                   /* LUNGES  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define IF 258
#define ELSE 259
#define PRINT 260
#define REPEAT 261
#define VAR 262
#define READ 263
#define LPAREN 264
#define RPAREN 265
#define LBRACE 266
#define RBRACE 267
#define COMMA 268
#define EQ 269
#define GT 270
#define LT 271
#define AND 272
#define OR 273
#define PLUS 274
#define MINUS 275
#define MULT 276
#define DIV 277
#define ASSIGN 278
#define NOT 279
#define INT 280
#define STRING 281
#define IDENTIFIER 282
#define NEWLINE 283
#define PUSH_UPS 284
#define SQUATS 285
#define PLANK 286
#define CRUNCHES 287
#define LUNGES 288

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
