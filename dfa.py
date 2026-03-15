KEYWORDS = {"if", "else", "while"}
OPERATORS = {"+", "-", "*", "/", "="}
SEPARATORS = {"(", ")", ";"}
def tokenize_with_dfa(source_code):
    i = 0
    n = len(source_code)
    while i < n:
        ch = source_code[i]
        if ch.isalpha():
            state = "q0"
            print(f"\nStart DFA for IDENTIFIER at state {state}")
            lexeme = ch
            print(f"{state} --{ch}--> q1")
            state = "q1"
            i += 1
            while i < n and source_code[i].isalnum():
                ch = source_code[i]
                print(f"{state} --{ch}--> q1")
                lexeme += ch
                i += 1
            if lexeme in KEYWORDS:
                print(f"Accepting State: KEYWORD ({lexeme})")
            else:
                print(f"Accepting State: IDENTIFIER ({lexeme})")
        elif ch.isdigit():
            state = "q0"
            print(f"\nStart DFA for NUMBER at state {state}")
            lexeme = ch
            print(f"{state} --{ch}--> q2")
            state = "q2"
            i += 1
            while i < n and source_code[i].isdigit():
                ch = source_code[i]
                print(f"{state} --{ch}--> q2")
                lexeme += ch
                i += 1
            print(f"Accepting State: NUMBER ({lexeme})")
        elif ch in OPERATORS:
            print(f"\nq0 --{ch}--> q_op")
            print(f"Accepting State: OPERATOR ({ch})")
            i += 1
        elif ch in SEPARATORS:
            print(f"\nq0 --{ch}--> q_sep")
            print(f"Accepting State: SEPARATOR ({ch})")
            i += 1
        elif ch.isspace():
            i += 1
        else:
            print(f"\nq0 --{ch}--> q_err")
            print(f"Accepting State: UNKNOWN ({ch})")
            i += 1
source_code = input("Enter source code: ")
tokenize_with_dfa(source_code)