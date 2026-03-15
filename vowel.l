%{
#include <stdio.h>
#include <ctype.h>
%}

%%

[a-zA-Z]
{
    char ch = tolower(yytext[0]);

    if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')
        printf("Vowel\n");
    else
        printf("Consonant\n");
}

\n      { }

.       { }

%%

int main()
{
    printf("Enter characters:\n");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
