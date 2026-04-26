from collections import defaultdict
grammar = {
    "S'": ["S"],
    "S": ["CC"],
    "C": ["cC", "d"]}
terminals = ["c", "d", "$"]
non_terminals = ["S'", "S", "C"]
def closure(items):
    items = set(items)
    changed = True
    while changed:
        changed = False
        for lhs, rhs, dot in list(items):
            if dot < len(rhs):
                sym = rhs[dot]
                if sym in non_terminals:
                    for prod in grammar[sym]:
                        item = (sym, prod, 0)
                        if item not in items:
                            items.add(item)
                            changed = True
    return frozenset(items)
def goto(items, symbol):
    moved = set()
    for lhs, rhs, dot in items:
        if dot < len(rhs) and rhs[dot] == symbol:
            moved.add((lhs, rhs, dot + 1))
    return closure(moved)
def follow_sets():
    follow = defaultdict(set)
    follow["S"].add("$")
    changed = True
    while changed:
        changed = False
        for lhs, prods in grammar.items():
            for rhs in prods:
                for i, sym in enumerate(rhs):
                    if sym in non_terminals:
                        if i + 1 < len(rhs):
                            nxt = rhs[i + 1]
                            if nxt in terminals:
                                follow[sym].add(nxt)
                            else:
                                follow[sym].add(grammar[nxt][0][0])
                        else:
                            old = len(follow[sym])
                            follow[sym] |= follow[lhs]
                            if len(follow[sym]) != old:
                                changed = True
    return follow
def make_states():
    states = [closure({("S'", "S", 0)})]
    symbols = terminals[:-1] + non_terminals
    for state in states:
        for sym in symbols:
            g = goto(state, sym)
            if g and g not in states:
                states.append(g)
    return states
states = make_states()
follow = follow_sets()
action = defaultdict(dict)
goto_table = defaultdict(dict)
symbols = terminals[:-1] + non_terminals
for i, state in enumerate(states):
    for lhs, rhs, dot in state:
        if dot < len(rhs):
            sym = rhs[dot]
            g = goto(state, sym)
            j = states.index(g)
            if sym in terminals:
                action[i][sym] = "S" + str(j)
            else:
                goto_table[i][sym] = j
        else:
            if lhs == "S'":
                action[i]["$"] = "ACC"
            else:
                for a in follow[lhs]:
                    action[i][a] = "R " + lhs + "->" + rhs
print("\nSLR Parsing Table\n")
print("State\tc\td\t$\tS\tC")
print("-" * 50)
for i in range(len(states)):
    c = action[i].get("c", "")
    d = action[i].get("d", "")
    dollar = action[i].get("$", "")
    S = goto_table[i].get("S", "")
    C = goto_table[i].get("C", "")
    print(f"{i}\t{c}\t{d}\t{dollar}\t{S}\t{C}")