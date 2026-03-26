def is_safe(ass,variable,val):
    for v in ass:
        if ass[v]==val:
            return False
    return True
def backtrack(assignment,variables,domains):
    if len(assignment)==len(variables):
        return assignment
    var=None
    for v in variables:
        if v not in assignment:
            var=v
            break
    for value in domains[var]:
        if is_safe(assignment,var,value):
            assignment[var]=value
            result=backtrack(assignment,variables,domains)
            if result:
                return result
            del assignment[var]
    return None
variables = ['X1', 'X2', 'X3']

domains = {
'X1':[1,2,3],
'X2':[1,2,3],
'X3':[1,2,3]
}

solution = backtrack({}, variables, domains)

print("Solution:", solution)