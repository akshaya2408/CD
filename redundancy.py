import ast
class RedundancyEliminator(ast.NodeTransformer):
    def __init__(self):
        self.expr_table = {}
    def expr_key(self, node):
        return ast.dump(node)
    def visit_Assign(self, node):
        self.generic_visit(node)
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            return node
        target = node.targets[0].id
        expr = node.value
        if isinstance(expr, (ast.BinOp, ast.UnaryOp, ast.BoolOp, ast.Compare)):
            key = self.expr_key(expr)
            if key in self.expr_table:
                prev_var = self.expr_table[key]
                return ast.Assign(
                    targets=[ast.Name(id=target, ctx=ast.Store())],
                    value=ast.Name(id=prev_var, ctx=ast.Load()))
            else:
                self.expr_table[key] = target
        return node
def expr_to_str(node):
    if isinstance(node, ast.Constant):
        return repr(node.value)
    elif isinstance(node, ast.Name):
        return node.id
    elif isinstance(node, ast.BinOp):
        left = expr_to_str(node.left)
        right = expr_to_str(node.right)
        op_map = {
            ast.Add: "+",
            ast.Sub: "-",
            ast.Mult: "*",
            ast.Div: "/",
            ast.Mod: "%",
            ast.Pow: "**"}
        op = op_map.get(type(node.op), "?")
        return f"({left} {op} {right})"
    elif isinstance(node, ast.UnaryOp):
        operand = expr_to_str(node.operand)
        if isinstance(node.op, ast.USub):
            return f"-{operand}"
        return operand
    elif isinstance(node, ast.Compare):
        left = expr_to_str(node.left)
        right = expr_to_str(node.comparators[0])
        op_map = {
            ast.Gt: ">",
            ast.Lt: "<",
            ast.Eq: "=="}
        op = op_map.get(type(node.ops[0]), "?")
        return f"({left} {op} {right})"
    return "UNKNOWN"
def to_source(node):
    lines = []
    for stmt in node.body:
        if isinstance(stmt, ast.Assign):
            target = stmt.targets[0].id
            value = expr_to_str(stmt.value)
            lines.append(f"{target} = {value}")
    return "\n".join(lines)
def eliminate_redundancy(code):
    tree = ast.parse(code)
    optimizer = RedundancyEliminator()
    new_tree = optimizer.visit(tree)
    ast.fix_missing_locations(new_tree)
    return to_source(new_tree)
if __name__ == "__main__":
    code = """
a = b + c
d = b + c
e = a + d
f = a + d
"""
    print("Optimized Code:\n")
    print(eliminate_redundancy(code))