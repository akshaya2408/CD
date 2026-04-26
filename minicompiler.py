import re

# -------------------------------
# Phase 1: Lexical Analysis
# -------------------------------
def lexical_analysis(statement):
    tokens = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*|\d+|[=+\-*/()]', statement)

    print("\n1. Lexical Analysis:")
    print("Tokens:", tokens)

    return tokens


# -------------------------------
# Phase 2: Syntax Analysis
# -------------------------------
def syntax_analysis(tokens):
    print("\n2. Syntax Analysis:")

    if "=" not in tokens:
        print("Syntax Error: Assignment operator missing")
        return False

    if tokens[0].isidentifier() and tokens[1] == "=":
        print("Syntax is valid")
        return True
    else:
        print("Syntax Error")
        return False


# -------------------------------
# Phase 3: Semantic Analysis
# -------------------------------
def semantic_analysis(tokens):
    print("\n3. Semantic Analysis:")

    lhs = tokens[0]

    if lhs.isdigit():
        print("Semantic Error: Cannot assign value to a number")
        return False

    print("Semantic check passed")
    return True


# -------------------------------
# Phase 4: Intermediate Code Generation
# -------------------------------
temp_count = 1

def new_temp():
    global temp_count
    temp = "t" + str(temp_count)
    temp_count += 1
    return temp


def intermediate_code_generation(tokens):
    print("\n4. Intermediate Code Generation:")

    lhs = tokens[0]
    expr = tokens[2:]

    code = []
    operators = ['*', '/', '+', '-']

    for op in operators:
        while op in expr:
            index = expr.index(op)

            left = expr[index - 1]
            right = expr[index + 1]

            temp = new_temp()
            code.append(f"{temp} = {left} {op} {right}")

            expr[index - 1:index + 2] = [temp]

    code.append(f"{lhs} = {expr[0]}")

    for line in code:
        print(line)

    return code


# -------------------------------
# Phase 5: Code Optimization
# -------------------------------
def code_optimization(code):
    print("\n5. Code Optimization:")

    optimized = []

    for line in code:
        lhs, rhs = line.split("=")
        lhs = lhs.strip()
        rhs = rhs.strip()

        try:
            value = eval(rhs)
            optimized.append(f"{lhs} = {value}")
        except:
            optimized.append(line)

    for line in optimized:
        print(line)

    return optimized


# -------------------------------
# Phase 6: Target Code Generation
# -------------------------------
def target_code_generation(code):
    print("\n6. Target Code Generation:")

    for line in code:
        lhs, rhs = line.split("=")
        lhs = lhs.strip()
        rhs = rhs.strip()

        parts = rhs.split()

        if len(parts) == 3:
            op1, op, op2 = parts

            print(f"MOV R0, {op1}")

            if op == "+":
                print(f"ADD R0, {op2}")
            elif op == "-":
                print(f"SUB R0, {op2}")
            elif op == "*":
                print(f"MUL R0, {op2}")
            elif op == "/":
                print(f"DIV R0, {op2}")

            print(f"MOV {lhs}, R0")

        else:
            print(f"MOV {lhs}, {rhs}")


# -------------------------------
# Main Program
# -------------------------------
statement = input("Enter a statement: ")

tokens = lexical_analysis(statement)

if syntax_analysis(tokens):
    if semantic_analysis(tokens):
        intermediate_code = intermediate_code_generation(tokens)
        optimized_code = code_optimization(intermediate_code)
        target_code_generation(optimized_code)