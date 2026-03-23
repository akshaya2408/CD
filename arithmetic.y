%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
%}

%token NUMBER

%%
start : E '\n' { printf("Valid Arithmetic Expression\n"); }
;

E : E '+' T
  | E '-' T
  | T
;

T : T '*' F
  | T '/' F
  | F
;

F : '(' E ')'
  | NUMBER
;
%%

int main()
{
    printf("Enter Arithmetic Expression:\n");
    yyparse();
    return 0;
}

void yyerror(const char *s)
{
    printf("Invalid Arithmetic Expression\n");
}

