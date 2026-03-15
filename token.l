%{
#include <stdio.h>
%}

/* Definitions */
KEYWORD     int|float|char|double|if|else|while|for|return
ID          [a-zA-Z_][a-zA-Z0-9_]*
NUMBER      [0-9]+
OPERATOR    [+\-*/=<>]
SEPARATOR   [(),;{}]

%%

{KEYWORD}      { printf("KEYWORD : %s\n", yytext); }

{ID}           { printf("IDENTIFIER : %s\n", yytext); }

{NUMBER}       { printf("NUMBER : %s\n", yytext); }

{OPERATOR}     { printf("OPERATOR : %s\n", yytext); }

{SEPARATOR}    { printf("SEPARATOR : %s\n", yytext); }

[ \t\n]+       ;   /* ignore whitespace */

.              { printf("UNKNOWN : %s\n", yytext); }

%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter the input:\n");
    yylex();
    return 0;
}