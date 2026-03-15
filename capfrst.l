%{
#include <stdio.h>
#include <ctype.h>

int newWord = 1;
%}

%%

[a-zA-Z]+
{
    for(int i = 0; i < yyleng; i++)
    {
        if(newWord && isalpha(yytext[i]))
        {
            printf("%c", toupper(yytext[i]));
            newWord = 0;
        }
        else
        {
            printf("%c", tolower(yytext[i]));
        }
    }
}

[ \t\n]+
{
    newWord = 1;
    printf("%s", yytext);
}

.
{
    printf("%s", yytext);
}

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