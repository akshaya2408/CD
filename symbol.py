import re
class SymbolTable:
    def __init__(self):
        self.table = []
    def add(self, token, token_type):
        address = hex(id(token))
        self.table.append({
            "name": token,
            "type": token_type,
            "address": address})
    def display(self):
        print("\nSymbol Table:")
        print("Token\t\tType\t\tAddress")
        print("-" * 60)
        for entry in self.table:
            print(f"{entry['name']}\t\t{entry['type']}\t\t{entry['address']}")
patterns = [
    ('KEYWORD', r'\b(int|float|if|else|while|return)\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ('NUMBER', r'\b\d+(\.\d+)?\b'),
    ('OPERATOR', r'[+\-*/=]'),
    ('SPECIAL_SYMBOL', r'[;,\(\)\{\}]')]
def scanner(code):
    tokens = []
    while code:
        code = code.lstrip()
        matched = False
        for token_type, pattern in patterns:
            match = re.match(pattern, code)
            if match:
                token = match.group(0)
                tokens.append((token, token_type))
                code = code[len(token):]
                matched = True
                break
        if not matched:
            tokens.append((code[0], "UNKNOWN"))
            code = code[1:]
    return tokens
code = input("Enter code/expression: ")
tokens = scanner(code)
st = SymbolTable()
for token, token_type in tokens:
    st.add(token, token_type)
st.display()