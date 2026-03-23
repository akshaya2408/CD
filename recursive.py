input_str = input()
i = 0
def match(expected):
   global i
   if input_str[i:i+len(expected)] == expected:
       print(f"Matched {expected}")
       i += len(expected)
   else:
       error()
def error():
   print("Parsing Error!")
   exit()
def E():
   print("Enter E")
   T()
   E_dash()
   print("Exit E")
def E_dash():
   print("Enter E'")
   global i
   if input_str[i] == '+':
       match('+')
       T()
       E_dash()
   print("Exit E'")
def T():
   print("Enter T")
   F()
   T_dash()
   print("Exit T")
def T_dash():
   print("Enter T'")
   global i
   if input_str[i] == '*':
       match('*')
       F()
       T_dash()
   print("Exit T'")
def F():
   print("Enter F")
   global i
   if input_str[i] == '(':
       match('(')
       E()
       match(')')
   elif input_str[i:i+2] == "id":
       match("id")
   else:
       error()
   print("Exit F")
E()
if input_str[i] == '$':
   print("String Accepted!")
else:
   print("String Rejected!")