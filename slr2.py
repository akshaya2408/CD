action = {
    0: {'c': 'S3', 'd': 'S4'},
    1: {'$': 'ACC'},
    2: {'c': 'S3', 'd': 'S4'},
    3: {'c': 'S3', 'd': 'S4'},
    4: {'c': 'R3', 'd': 'R3', '$': 'R3'},
    5: {'$': 'R1'},
    6: {'c': 'R2', 'd': 'R2', '$': 'R2'}}
goto = {
    0: {'S': 1, 'C': 2},
    2: {'C': 5},
    3: {'C': 6}}
productions = {
    1: ('S', 2),   # S -> CC
    2: ('C', 2),   # C -> cC
    3: ('C', 1)}
def check_slr(s):
    s += '$'
    stack = [0]
    i = 0
    while True:
        state = stack[-1]
        symbol = s[i]
        if state not in action or symbol not in action[state]:
            return False
        act = action[state][symbol]
        if act == 'ACC':
            return True
        elif act[0] == 'S':
            stack.append(symbol)
            stack.append(int(act[1:]))
            i += 1
        elif act[0] == 'R':
            lhs, length = productions[int(act[1:])]
            for _ in range(2 * length):
                stack.pop()
            state = stack[-1]
            if state not in goto or lhs not in goto[state]:
                return False
            stack.append(lhs)
            stack.append(goto[state][lhs])
string = input("Enter string: ")
if check_slr(string):
    print("Valid")
else:
    print("Invalid")