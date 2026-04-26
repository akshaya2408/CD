import re
temp_count = 1
def new_temp():
    global temp_count
    temp = "t" + str(temp_count)
    temp_count += 1
    return temp
def tokenize(expr):
    return re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*|\d+|[+\-*/()]', expr)
def generate_intermediate_code(expr):
    operators = ['*', '/', '+', '-']
    tokens = tokenize(expr)
    code = []
    for op in operators:
        while op in tokens:
            index = tokens.index(op)
            left = tokens[index - 1]
            right = tokens[index + 1]
            temp = new_temp()
            code.append(f"{temp} = {left} {op} {right}")
            tokens[index - 1:index + 2] = [temp]
    return tokens[0], code
statement = input("Enter expression like a=b+c*d: ")
lhs, rhs = statement.split("=")
lhs = lhs.strip()
rhs = rhs.strip()
result, code = generate_intermediate_code(rhs)
print("\nIntermediate Code:")
for line in code:
    print(line)
print(f"{lhs} = {result}")