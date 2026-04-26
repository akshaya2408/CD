import ast
import operator
class ConstantFolder(ast.NodeTransformer):
    def __init__(self):
        self.constants = {}
    def visit_BinOp(self, node):
        self.generic_visit(node)

        if isinstance(node.left, ast.Constant) and isinstance(node.right, ast.Constant):
            try:
                return ast.Constant(
                    value=self.eval_binop(node.op, node.left.value, node.right.value)
                )
            except:
                pass
        return node
    def visit_UnaryOp(self, node):
        self.generic_visit(node)
        if isinstance(node.operand, ast.Constant):
            try:
                return ast.Constant(
                    value=self.eval_unaryop(node.op, node.operand.value)
                )
            except:
                pass
        return node
    def visit_Assign(self, node):
        self.generic_visit(node)
        for target in node.targets:
            if isinstance(target, ast.Name):
                if isinstance(node.value, ast.Constant):
                    self.constants[target.id] = node.value.value
                else:
                    self.constants.pop(target.id, None)
        return node
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load) and node.id in self.constants:
            return ast.Constant(value=self.constants[node.id])
        return node
    def eval_binop(self, op, l, r):
        ops = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.FloorDiv: operator.floordiv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow}
        return ops[type(op)](l, r)
    def eval_unaryop(self, op, val):
        if isinstance(op, ast.USub):
            return -val
        elif isinstance(op, ast.UAdd):
            return +val
        return val
def to_source(node):
    lines = []
    for stmt in node.body:
        if isinstance(stmt, ast.Assign):
            target = stmt.targets[0].id
            value = eval(compile(ast.Expression(stmt.value), filename="", mode="eval"))
            lines.append(f"{target} = {repr(value)}")
    return "\n".join(lines)
def fold_constants(code):
    tree = ast.parse(code)
    folder = ConstantFolder()
    new_tree = folder.visit(tree)
    ast.fix_missing_locations(new_tree)
    return to_source(new_tree)
if __name__ == "__main__":
    code = """
a = 5
b = a + 3
a = 10
c = a + 2
x = 2 + 3 * 4
y = (10 - 5) + (6 / 2)
z = -(-3)
"""
    print("Optimized Code:\n")
    print(fold_constants(code))