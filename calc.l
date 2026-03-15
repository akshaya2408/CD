%{
#include "y.tab.h"
#include <stdlib.h>
#include <stdio.h>
%}

%%

[0-9]+      { yylval = atoi(yytext); return NUMBER; }

"+"         { return PLUS; }

"-"         { return MINUS; }

"*"         { return MUL; }

"/"         { return DIV; }

"("         { return LPAREN; }

")"         { return RPAREN; }

\n          { return '\n'; }

[ \t]+      { }

.           { printf("Invalid character\n"); }

%%

int yywrap()
{
    return 1;
}