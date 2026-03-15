%{
#include <stdio.h>
%}

%%

^[0-9]+$           { printf("Integer\n"); }

^[0-9]+\.[0-9]+$   { printf("Real Number\n"); }

.|\n               { }

%%

int main()
{
    printf("Enter numbers:\n");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}