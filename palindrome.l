%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "y.tab.h"
%}

%%
[a-zA-Z]+   { yylval.f = strdup(yytext); return STR; }
[ \t\n]     ;
.           ;
%%

int yywrap()
{
    return 1;
}
