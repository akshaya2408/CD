import ast
class StrengthReducer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        self.generic_visit(node)
        if isinstance(node.op, ast.Mult):
            # x * 2^n
            if isinstance(node.right, ast.Constant):
                val = node.right.value
                if self.is_power_of_two(val):
                    shift = self.log2(val)
                    return ast.BinOp(
                        left=node.left,
                        op=ast.LShift(),
                        right=ast.Constant(value=shift))
            if isinstance(node.left, ast.Constant):
                val = node.left.value
                if self.is_power_of_two(val):
                    shift = self.log2(val)
                    return ast.BinOp(
                        left=node.right,
                        op=ast.LShift(),
                        right=ast.Constant(value=shift))
        if isinstance(node.op, ast.Div):
            if isinstance(node.right, ast.Constant):
                val = node.right.value
                if self.is_power_of_two(val):
                    shift = self.log2(val)
                    return ast.BinOp(
                        left=node.left,
                        op=ast.RShift(),
                        right=ast.Constant(value=shift))
        return node
    def is_power_of_two(self, n):
        return isinstance(n, int) and n > 0 and (n & (n - 1)) == 0
    def log2(self, n):
        count = 0
        while n > 1:
            n >>= 1
            count += 1
        return count
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
            ast.LShift: "<<",
            ast.RShift: ">>"}
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
def strength_reduction(code):
    tree = ast.parse(code)
    reducer = StrengthReducer()
    new_tree = reducer.visit(tree)
    ast.fix_missing_locations(new_tree)
    return to_source(new_tree)
if __name__ == "__main__":
    code = """
x = y * 8
a = 4 * b
c = d / 2
e = f * 3
"""
    print("Optimized Code:\n")
    print(strength_reduction(code))