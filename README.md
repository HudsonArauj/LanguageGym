# LanguageGym

## Descrição
O LanguageGym é um projeto de criação de uma linguagem para a disciplina de Logica de Programação. A ideia é criar uma linguagem que seja simples e intuitiva para que programar um treino seja mais fácil e divertido.


## EBNF
```
PROGRAM = { EXERCISE_ROUTINE };
EXERCISE_ROUTINE = ( ASSIGNMENT | PRINT | REPEAT | IF | VARIABLE_DECLARATION | EXERCISE_INSTRUCTION), "\n" ;
ASSIGNMENT = IDENTIFIER, "=", BOOLEAN_EXPRESSION;
PRINT = "print", "(", BOOLEAN_EXPRESSION , ")" ;
READ = "read", "(", ")" ;
REPEAT="repeat","(",NUMBER,")","\n",{EXERCISE_ROUTINE},;

IF  = "if", BOOLEAN_EXPRESSION,"\n", {EXERCISE_ROUTINE}, ["else", "\n", {EXERCISE_ROUTINE}];
VARIABLE_DECLARATION = "var", IDENTIFIER, [ "=", BOOLEAN_EXPRESSION] ;
EXERCISE_INSTRUCTION = EXERCISE_NAME ,"(" ,NUMBER, ")";
BOOLEAN_EXPRESSION = BOOLEAN_TERM, { ("or" ), BOOLEAN_TERM};
BOOLEAN_TERM = REL_EXPRESSION, { ("and" ), REL_EXPRESSION};
REL_EXPRESSION= EXPRESSION, { ("==" |">"|"<"), EXPRESSION};

EXPRESSION = TERM, { ("+" | "-"), TERM } ;
TERM = FACTOR, { ("*" | "/"), FACTOR } ;
FACTOR = (("+" | "-"|"not"), FACTOR) | NUMBER | IDENTIFIER | "(" , BOOLEAN_EXPRESSION , ")" | READ  ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( "a" | "..." | "z" | "A" | "..." | "Z" ) ;
DIGIT = ( "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0" ) ; 

EXERCISE_NAME       = ("PUSH_UPS"
                      | "SQUATS"
                      | "PLANK"
                      | "CRUNCHES"
                      | "LUNGES");
```

## Exemplos
```
var sets = 3;
var squats_per_set = 15;

repeat(sets) {
    squats(squats_per_set);
    plank(30);
}

if (squats_per_set > 10) {
    lunges(12);
} else {
    crunches(20);
}

custom_routine(3);
```


Neste exemplo, definimos variáveis para o número de séries (sets) e o número de agachamentos por série (squats_per_set). Em seguida, usamos instruções de loop (repeat) e condicionais (if-else) para criar uma rotina de exercícios dinâmica.

