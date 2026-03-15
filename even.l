%{
#include <stdio.h>
#include <stdlib.h>
%}

%%

[0-9]+ 
{
    int num = atoi(yytext);

    if(num % 2 == 0)
        printf("Even\n");
    else
        printf("Odd\n");
}

\n      { }

%%

int main()
{
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}