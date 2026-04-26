import re
def tokenize(rhs):
    return re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*|\d+|[+\-*/]', rhs)
def generate_target_code(tac):
    print("\nTarget Code:")
    for line in tac:
        lhs, rhs = line.split("=")
        lhs = lhs.strip()
        rhs = rhs.strip()
        parts = tokenize(rhs)
        if len(parts) == 3:
            op1, operator, op2 = parts
            print(f"MOV R0, {op1}")
            if operator == '+':
                print(f"ADD R0, {op2}")
            elif operator == '-':
                print(f"SUB R0, {op2}")
            elif operator == '*':
                print(f"MUL R0, {op2}")
            elif operator == '/':
                print(f"DIV R0, {op2}")
            print(f"MOV {lhs}, R0")
        else:
            print(f"MOV {lhs}, {rhs}")
n = int(input("Enter number of intermediate code statements: "))
tac = []
print("Enter Three Address Code statements:")
for i in range(n):
    tac.append(input())
generate_target_code(tac)