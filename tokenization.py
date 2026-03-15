KEYWORDS = ["if", "else", "while", "for", "int", "float", "return", "char", "double"]
OPERATORS = ["+", "-", "*", "/", "=", "<", ">", "<=", ">=", "=="]
SPECIAL_SYMBOLS = [";", ",", "(", ")", "{", "}", "[", "]"]
def is_identifier(word):
    return word[0].isalpha() or word[0] == "_"
def tokenize(code):
    tokens = []
    i = 0
    while i < len(code):
        ch = code[i]
        if ch.isspace():
            i += 1
            continue
        if ch == '"':
            string = ch
            i += 1
            while i < len(code) and code[i] != '"':
                string += code[i]
                i += 1
            if i < len(code):
                string += '"'
                i += 1
            tokens.append(("STRING", string))
        elif ch in "+-*/=<>":
            if i + 1 < len(code) and ch + code[i + 1] in OPERATORS:
                tokens.append(("OPERATOR", ch + code[i + 1]))
                i += 2
            else:
                tokens.append(("OPERATOR", ch))
                i += 1
        elif ch in SPECIAL_SYMBOLS:
            tokens.append(("SPECIAL SYMBOL", ch))
            i += 1
        elif ch.isdigit():
            num = ch
            i += 1
            while i < len(code) and code[i].isdigit():
                num += code[i]
                i += 1
            tokens.append(("CONSTANT", num))
        elif ch.isalpha() or ch == "_":
            word = ch
            i += 1
            while i < len(code) and (code[i].isalnum() or code[i] == "_"):
                word += code[i]
                i += 1
            if word in KEYWORDS:
                tokens.append(("KEYWORD", word))
            else:
                tokens.append(("IDENTIFIER", word))
        else:
            i += 1
    return tokens
code = input("Enter the code to tokenize: ")
for token in tokenize(code):
    print(token)