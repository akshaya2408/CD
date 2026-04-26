import re
def get_variables(expr):
    return re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', expr)
def code_motion_optimization(code_lines):
    loop_line = ""
    loop_body = []
    before_loop = []
    inside_loop = []
    for line in code_lines:
        stripped = line.strip()
        if stripped.startswith("for"):
            loop_line = stripped
        elif stripped != "":
            loop_body.append(stripped)
    for stmt in loop_body:
        if "=" not in stmt:
            inside_loop.append(stmt)
            continue
        lhs, rhs = stmt.split("=", 1)
        lhs = lhs.strip()
        rhs = rhs.strip()
        variables = get_variables(rhs)
        if "i" not in variables:
            before_loop.append(stmt)
        else:
            inside_loop.append(stmt)
    print("\nOptimized Code:\n")
    for stmt in before_loop:
        print(stmt)
    if loop_line:
        print(loop_line)
    else:
        print("for i in range(n):")
    for stmt in inside_loop:
        print("    " + stmt)
n = int(input("Enter number of lines in original code: "))
print("Enter original code:")
code_lines = []
for _ in range(n):
    code_lines.append(input())
code_motion_optimization(code_lines)