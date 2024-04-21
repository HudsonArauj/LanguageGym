# LanguageGym

## Descrição
O LanguageGym é um projeto de criação de uma linguagem para a disciplina de Logica de Programação. A ideia é criar uma linguagem que seja simples e intuitiva para que programar um treino seja mais fácil e divertido.


## EBNF
```
PROGRAM             = lambda | EXERCISE_ROUTINE 
EXERCISE_ROUTINE    = EXERCISE_INSTRUCTION | LOOP_STATEMENT | CONDITIONAL_STATEMENT | VARIABLE_DECLARATION | FUNCTION_DEFINITION | RETURN_STATEMENT 
STATEMENT_LIST      = STATEMENT | STATEMENT_LIST STATEMENT
STATEMENT           =  EXERCISE_ROUTINE 
EXERCISE_INSTRUCTION = EXERCISE_NAME "(" [EXERCISE_DETAILS] ")" ";"
EXERCISE_DETAILS    = NUMBER | MACHINE_NAME | NUMBER "," MACHINE_NAME
LOOP_STATEMENT      = "REPEAT" "(" NUMBER ")" "{" STATEMENT_LIST "}" ";"
CONDITIONAL_STATEMENT = "IF" "(" CONDITION ")" "{" STATEMENT_LIST "}"
                          ["ELSE" "{" STATEMENT_LIST "}"] ";"
VARIABLE_DECLARATION = "VAR" IDENTIFIER "=" EXPRESSION ";"
FUNCTION_DEFINITION = "FUNCTION" IDENTIFIER "(" [PARAMETER_LIST] ")" "{" STATEMENT_LIST "}"
PARAMETER_LIST      = IDENTIFIER { "," IDENTIFIER }
RETURN_STATEMENT    = "RETURN" EXPRESSION ";"
EXPRESSION          = TERM
                      | EXPRESSION ( "+" | "-" | "*" | "/" ) TERM
                      | "(" EXPRESSION ")"
                      | IDENTIFIER
                      | NUMBER

CONDITION           = EXPRESSION ( "==" | ">" | "<" ) EXPRESSION

EXERCISE_NAME       = "PUSH_UPS"
                      | "SQUATS"
                      | "PLANK"
                      | "CRUNCHES"
                      | "LUNGES"
MACHINE_NAME        = "EXTENSORA"
                      | "FLEXORA"
                      | "SUPINO"
                      | "PULLDOWN"
                      | "REMADA"
                      | "LEG_PRESS"
                      | "LEG_CURL"
                      | "LEG_EXTENSION"
                      | "SHOULDER_PRESS"
                      | "BICEPS_CURL"
                      | "TRICEPS_EXTENSION"
IDENTIFIER          = LETTER { LETTER | DIGIT | "_" }
NUMBER              = DIGIT { DIGIT }
LETTER              = "A" | "B" | ... | "Z" | "a" | "b" | ... | "z"
DIGIT               = "0" | "1" | ... | "9"

```

## Exemplos
```var sets = 3;
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

function custom_routine(reps) {
    repeat(reps) {
        push_ups(10);
    }
}

custom_routine(3);
```


Neste exemplo, definimos variáveis para o número de séries (sets) e o número de agachamentos por série (squats_per_set). Em seguida, usamos instruções de loop (repeat) e condicionais (if-else) para criar uma rotina de exercícios dinâmica. Também definimos uma função personalizada (custom_routine) que executa flexões (push_ups) um determinado número de vezes.

