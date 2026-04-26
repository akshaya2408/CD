import re

# -------------------------------
# Phase 1: Lexical Analysis
# -------------------------------
def lexical_analysis(source_code):
    tokens = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*|\d+|[=+\-*/();:]', source_code)

    print("\n1. Lexical Analysis:")
    print(tokens)

    return tokens


# -------------------------------
# Phase 2: Syntax Analysis
# -------------------------------
def syntax_analysis(source_code):
    print("\n2. Syntax Analysis:")
    ast = []
    lines = source_code.strip().split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line == "":
            i += 1
            continue
        if line.startswith("for"):
            loop_node = {
                "type": "for",
                "condition": line,
                "body": []
            }
            i += 1
            while i < len(lines) and lines[i].startswith("    "):
                body_line = lines[i].strip().replace(";", "")
                if "=" in body_line:
                    lhs, rhs = body_line.split("=")
                    loop_node["body"].append({
                        "type": "assign",
                        "var": lhs.strip(),
                        "value": rhs.strip()
                    })
                i += 1
            ast.append(loop_node)
        else:
            line = line.replace(";", "")
            if "=" in line:
                lhs, rhs = line.split("=")
                ast.append({
                    "type": "assign",
                    "var": lhs.strip(),
                    "value": rhs.strip()
                })
            i += 1
    print("Syntax is valid")
    return ast


# -------------------------------
# Phase 3: Semantic Analysis
# -------------------------------
def semantic_analysis(ast):
    print("\n3. Semantic Analysis:")

    defined_vars = set()

    for node in ast:
        if node["type"] == "assign":
            defined_vars.add(node["var"])

        elif node["type"] == "for":
            for stmt in node["body"]:
                defined_vars.add(stmt["var"])

    print("Semantic check passed")
    print("Defined Variables:", defined_vars)

    return defined_vars


# -------------------------------
# Phase 4: Intermediate Code Generation
# -------------------------------
temp_count = 1

def new_temp():
    global temp_count
    temp = "t" + str(temp_count)
    temp_count += 1
    return temp


def generate_expression_code(lhs, rhs):
    tokens = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*|\d+|[+\-*/]', rhs)

    code = []
    operators = ['*', '/', '+', '-']

    for op in operators:
        while op in tokens:
            index = tokens.index(op)

            left = tokens[index - 1]
            right = tokens[index + 1]

            temp = new_temp()
            code.append(f"{temp} = {left} {op} {right}")

            tokens[index - 1:index + 2] = [temp]

    code.append(f"{lhs} = {tokens[0]}")
    return code


def intermediate_code_generation(ast):
    print("\n4. Intermediate Code Generation:")

    code = []

    for node in ast:
        if node["type"] == "assign":
            code.extend(generate_expression_code(node["var"], node["value"]))

        elif node["type"] == "for":
            code.append(node["condition"])

            for stmt in node["body"]:
                code.extend(generate_expression_code(stmt["var"], stmt["value"]))

            code.append("end for")

    for line in code:
        print(line)

    return code


# -------------------------------
# Phase 5: Code Optimization
# -------------------------------
def code_optimization(code):
    print("\n5. Code Optimization:")

    optimized = []
    constants = {}

    for line in code:
        if line.startswith("for") or line == "end for":
            optimized.append(line)
            continue

        if "=" in line:
            lhs, rhs = line.split("=")
            lhs = lhs.strip()
            rhs = rhs.strip()

            for var, val in constants.items():
                rhs = re.sub(r'\b' + var + r'\b', str(val), rhs)

            try:
                value = eval(rhs)
                optimized.append(f"{lhs} = {value}")
                constants[lhs] = value
            except:
                optimized.append(f"{lhs} = {rhs}")
                constants.pop(lhs, None)

    for line in optimized:
        print(line)

    return optimized


# -------------------------------
# Phase 6: Target Code Generation
# -------------------------------
def target_code_generation(code):
    print("\n6. Target Code Generation:")

    for line in code:
        if line.startswith("for"):
            print("; " + line)
            continue

        if line == "end for":
            print("; end for")
            continue

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
if __name__ == "__main__":

    source_code = """
a=5;
b=10;
for i in range(3):
    c=a;
    d=b;
    e=5;
"""

    print("=== SOURCE PROGRAM ===")
    print(source_code)

    tokens = lexical_analysis(source_code)

    ast_tree = syntax_analysis(source_code)

    print("\nSYNTAX ANALYSIS AST:")
    print(ast_tree)

    defined_vars = semantic_analysis(ast_tree)

    intermediate_code = intermediate_code_generation(ast_tree)

    optimized_code = code_optimization(intermediate_code)

    target_code_generation(optimized_code)