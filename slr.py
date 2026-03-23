ACTION = {
0: {'i':('s',5),'(':('s',4)},
1: {'+':('s',6),'$':('acc',)},
2: {'+':('r',2),'*':('s',7),')':('r',2),'$':('r',2)},
3: {'+':('r',4),'*':('r',4),')':('r',4),'$':('r',4)},
4: {'i':('s',5),'(':('s',4)},
5: {'+':('r',6),'*':('r',6),')':('r',6),'$':('r',6)},
6: {'i':('s',5),'(':('s',4)},
7: {'i':('s',5),'(':('s',4)},
8: {'+':('s',6),')':('s',11)},
9: {'+':('r',1),'*':('s',7),')':('r',1),'$':('r',1)},
10:{'+':('r',3),'*':('r',3),')':('r',3),'$':('r',3)},
11:{'+':('r',5),'*':('r',5),')':('r',5),'$':('r',5)}}
GOTO = {
0:{'E':1,'T':2,'F':3},
4:{'E':8,'T':2,'F':3},
6:{'T':9,'F':3},
7:{'F':10}}
productions = {
1:('E',['E','+','T']),
2:('E',['T']),
3:('T',['T','*','F']),
4:('T',['F']),
5:('F',['(','E',')']),
6:('F',['i'])}
def slr_parse(inp):
    stack = [0]
    inp.append('$')
    i = 0
    while True:
        state = stack[-1]
        symbol = inp[i]
        if symbol not in ACTION[state]:
            print("Invalid String")
            return
        action = ACTION[state][symbol]
        if action[0] == 's':
            stack.append(symbol)
            stack.append(action[1])
            i += 1
        elif action[0] == 'r':
            prod = productions[action[1]]
            lhs, rhs = prod
            pop_len = 2 * len(rhs)
            stack = stack[:-pop_len]
            state = stack[-1]
            stack.append(lhs)
            stack.append(GOTO[state][lhs])
        elif action[0] == 'acc':
            print("Valid String")
            return
expr = input("Enter expression: ")
tokens = []
for ch in expr:
    if ch in ['+','*','(',')']:
        tokens.append(ch)
    elif ch.isalpha() or ch.isdigit():
        tokens.append('i')
slr_parse(tokens)