%{
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
%}

%token NUMBER

%%

input :
        expr '\n' { printf("Result = %d\n", $1); }
      ;

expr :
        expr '+' term { $$ = $1 + $3; }
      | expr '-' term { $$ = $1 - $3; }
      | term          { $$ = $1; }
      ;

term :
        term '*' factor { $$ = $1 * $3; }
      | term '/' factor
        {
            if($3 == 0)
            {
                printf("Division by 0 error\n");
                exit(0);
            }
            $$ = $1 / $3;
        }
      | factor { $$ = $1; }
      ;

factor :
        NUMBER          { $$ = $1; }
      | '(' expr ')'    { $$ = $2; }
      ;

%%


int yylex()
{
    int c;

    while ((c = getchar()) == ' ' || c == '\t');

    if (isdigit(c))
    {
        ungetc(c, stdin);
        scanf("%d", &yylval);
        return NUMBER;
    }

    if (c == '\n')
        return '\n';

    return c;   /* operators like + - * / ( ) */
}


void yyerror(const char *s)
{
    printf("Syntax Error\n");
}


int main()
{
    printf("Enter expression: ");
    yyparse();
    return 0;
}