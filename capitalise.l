%{
#include <stdio.h>
#include <ctype.h>
%}

%%

[a-z]+ 
{
    for(int i = 0; i < yyleng; i++)
        printf("%c", toupper(yytext[i]));
}

\n      { printf("\n"); }

.       { printf("%s", yytext); }

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