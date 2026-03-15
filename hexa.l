%{
#include <stdio.h>
%}
%%
0[xX][0-9a-fA-F]+ { printf("Hexadecimal number\n"); }
0[0-7]+ { printf("Octal number\n"); }
0[89][0-9]* { printf("Invalid input\n"); } /* invalid octal */
[ \t]+ ;
\n ;
. { printf("Invalid input\n"); }
%%
int yywrap() { return 1; }
int main() {
printf("Enter numbers (Ctrl+D to end):\n");
yylex();
return 0;
}