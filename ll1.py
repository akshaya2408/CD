from collections import defaultdict
grammar = {
    'E': [['T', "E'"]],
    "E'": [['*', 'T', "E'"], ['ε']],
    'T': [['+', 'T'], ['F']],
    'F': [['(', 'E', ')'], ['id']]}
non_terminals = list(grammar.keys())
terminals = ['+', '*', '(', ')', 'id', '$']
FIRST = defaultdict(set)
FOLLOW = defaultdict(set)
parsing_table = defaultdict(dict)
def compute_first():
    changed = True
    while changed:
        changed = False
        for nt in grammar:
            for production in grammar[nt]:
                for symbol in production:
                    if symbol not in grammar:
                        if symbol not in FIRST[nt]:
                            FIRST[nt].add(symbol)
                            changed = True
                        break
                    else:
                        before = len(FIRST[nt])
                        FIRST[nt] |= (FIRST[symbol] - {'ε'})
                        if 'ε' not in FIRST[symbol]:
                            break
                        if before != len(FIRST[nt]):
                            changed = True
                else:
                    FIRST[nt].add('ε')

def compute_follow():
    FOLLOW['E'].add('$')  # start symbol
    changed = True
    while changed:
        changed = False
        for nt in grammar:
            for production in grammar[nt]:
                for i, symbol in enumerate(production):
                    if symbol in grammar:
                        before = len(FOLLOW[symbol])
                        if i + 1 < len(production):
                            next_symbol = production[i + 1]
                            if next_symbol in grammar:
                                FOLLOW[symbol] |= (FIRST[next_symbol] - {'ε'})
                            else:
                                FOLLOW[symbol].add(next_symbol)
                        else:
                            FOLLOW[symbol] |= FOLLOW[nt]
                        if before != len(FOLLOW[symbol]):
                            changed = True
def construct_table():
    for nt in grammar:
        for production in grammar[nt]:
            first_set = set()
            if production[0] not in grammar:
                first_set.add(production[0])
            else:
                first_set |= FIRST[production[0]]
            for terminal in first_set - {'ε'}:
                parsing_table[nt][terminal] = production
            if 'ε' in first_set:
                for terminal in FOLLOW[nt]:
                    parsing_table[nt][terminal] = production
def print_table():
    print("\nLL(1) Parsing Table:\n")
    print(f"{'':10}", end="")
    for t in terminals:
        print(f"{t:10}", end="")
    print()
    for nt in non_terminals:
        print(f"{nt:10}", end="")
        for t in terminals:
            if t in parsing_table[nt]:
                prod = " ".join(parsing_table[nt][t])
                print(f"{prod:10}", end="")
            else:
                print(f"{'-':10}", end="")
        print()
compute_first()
compute_follow()
construct_table()
print_table()