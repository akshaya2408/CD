import ast
class AlgebraicSimplifier(ast.NodeTransformer):
    def visit_BinOp(self, node):
        self.generic_visit(node)
        if isinstance(node.op, ast.Add):
            if self.is_zero(node.right):
                return node.left
            if self.is_zero(node.left):
                return node.right
        if isinstance(node.op, ast.Sub):
            if self.is_zero(node.right):
                return node.left
        if isinstance(node.op, ast.Mult):
            if self.is_one(node.right):
                return node.left
            if self.is_one(node.left):
                return node.right
            if self.is_zero(node.right) or self.is_zero(node.left):
                return ast.Constant(value=0)
        if isinstance(node.op, ast.Div):
            if self.is_one(node.right):
                return node.left
            if self.is_zero(node.left):
                return ast.Constant(value=0)
        return node
    def is_zero(self, node):
        return isinstance(node, ast.Constant) and node.value == 0
    def is_one(self, node):
        return isinstance(node, ast.Constant) and node.value == 1
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
            ast.Div: "/"}
        op = op_map.get(type(node.op), "?")
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
def simplify_algebra(code):
    tree = ast.parse(code)
    simplifier = AlgebraicSimplifier()
    new_tree = simplifier.visit(tree)
    ast.fix_missing_locations(new_tree)
    return to_source(new_tree)
if __name__ == "__main__":
    code = """
a = b + 0
c = 0 + d
e = f * 1
g = 1 * h
i = j * 0
k = 0 * l
m = n - 0
o = p / 1
q = 0 / r
"""
    print("Simplified Code:\n")
    print(simplify_algebra(code))