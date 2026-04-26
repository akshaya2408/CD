from collections import defaultdict

# -------- INPUT --------
n = int(input("No. of productions: "))

P = []
NT = set()

print("Enter productions (format: E -> E + T):")
for _ in range(n):
    l, r = input().split("->")
    l = l.strip()
    r = r.strip().split()
    P.append((l, r))
    NT.add(l)

# Augmented grammar
start = P[0][0]
P.insert(0, (start+"'", [start]))
NT.add(start+"'")

# Terminals
T = set()
for _, rhs in P:
    for x in rhs:
        if x not in NT:
            T.add(x)
T.add("$")
T = list(T)

FIRST, FOLLOW = defaultdict(set), defaultdict(set)

# -------- FIRST --------
def first():
    for t in T:
        FIRST[t].add(t)
    changed = True
    while changed:
        changed = False
        for A, B in P:
            for x in B:
                before = len(FIRST[A])
                FIRST[A] |= FIRST[x]
                if before != len(FIRST[A]):
                    changed = True
                if "ε" not in FIRST[x]:
                    break

# -------- FOLLOW --------
def follow():
    FOLLOW[start+"'"].add("$")
    changed = True
    while changed:
        changed = False
        for A, B in P:
            trailer = FOLLOW[A].copy()
            for x in reversed(B):
                if x in NT:
                    before = len(FOLLOW[x])
                    FOLLOW[x] |= trailer
                    if before != len(FOLLOW[x]):
                        changed = True
                    trailer = FIRST[x]
                else:
                    trailer = FIRST[x]

# -------- CLOSURE --------
def closure(I):
    I = set(I)
    while True:
        new = set(I)
        for A, B, d in I:
            if d < len(B) and B[d] in NT:
                for p in P:
                    if p[0] == B[d]:
                        new.add((p[0], tuple(p[1]), 0))
        if new == I:
            return I
        I = new

# -------- GOTO --------
def goto(I, X):
    return closure({(A, B, d+1) for A, B, d in I if d < len(B) and B[d] == X})

# -------- ITEMS --------
def items():
    C = [closure({(P[0][0], tuple(P[0][1]), 0)})]
    while True:
        new = []
        for I in C:
            for X in T + list(NT):
                g = goto(I, X)
                if g and g not in C and g not in new:
                    new.append(g)
        if not new:
            return C
        C += new

# -------- TABLE --------
def table(C):
    A, G = defaultdict(dict), defaultdict(dict)
    for i, I in enumerate(C):
        for A1, B, d in I:
            if d < len(B):
                X = B[d]
                j = goto(I, X)
                if j in C:
                    if X in T:
                        A[i][X] = "s" + str(C.index(j))
                    else:
                        G[i][X] = str(C.index(j))
            else:
                if A1 == P[0][0]:
                    A[i]["$"] = "acc"
                else:
                    for a in FOLLOW[A1]:
                        A[i][a] = "r" + str(P.index((A1, list(B))))
    return A, G

# -------- PRINT --------
def print_states(C):
    print("\nCanonical Collection:\n")
    for i, I in enumerate(C):
        print(f"I{i}:")
        for A, B, d in I:
            B = list(B)
            B.insert(d, "•")
            print(" ", A, "->", " ".join(B))
        print()

def print_table(A, G, C):
    headers = T + list(NT)

    print("\nSLR PARSING TABLE:\n")

    print(f"{'State':<6}", end="")
    for h in headers:
        print(f"{h:<8}", end="")
    print()

    print("-" * 100)

    for i in range(len(C)):
        print(f"{i:<6}", end="")
        for t in T:
            print(f"{A[i].get(t, ''):<8}", end="")
        for nt in NT:
            print(f"{G[i].get(nt, ''):<8}", end="")
        print()

# -------- RUN --------
first()
follow()
C = items()
A, G = table(C)

print_states(C)
print_table(A, G, C)