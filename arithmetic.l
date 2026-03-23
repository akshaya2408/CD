%{
#include "y.tab.h"
#include <stdlib.h>
%}

%%
[0-9]+      return NUMBER;
[ \t]       ;
\n          return '\n';
.           return yytext[0];
%%

int yywrap()
{
    return 1;
}

