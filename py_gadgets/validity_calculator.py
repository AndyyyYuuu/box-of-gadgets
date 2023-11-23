# Andy Yu
# Sept 21, 2023
# Logic Validity Calculator

AND = "^"
OR = "V"
IF = ">"
ONLY_IF = "="
NOT = "-"

def and_(p, q):
    return p and q
def or_(p, q):
    return p or q
def if_(p, q):
    return (True, q)[p]
def only_if(p, q):
    return p == q

'''
def get_func(string):
    
    # Brackets
    for i in range(len(inp)):
        if inp[i] == "(":
            bracket_f = inp[i+1:inp.rfind(")")]
    # Negation
    for i in range(len(inp)):
        if inp[i] == "
    
'''
def process_input(string):
    return string.replace("^", " and ").replace("v", " or ").replace("-", " not ")

def is_valid(atomics, expressions):
    
    table_size = 2**len(list(atomics.keys()))

    # Generate permutations
    for row in range(table_size):
        for col in range(len(list(atomics.keys()))):
            atomics[list(atomics.keys())[col]].append((row//(2**col))%2)

    # Calculate
    for row in range(table_size):
        row_bools = []
        for col in range(len(expressions)):
            test_expression = expressions[col]
            for atomic in list(atomics.keys()):
                test_expression = test_expression.replace(str(atomic), str(atomics[atomic][row]))
            row_bools.append(int(eval(process_input(test_expression))))
        if 0 in row_bools and row_bools.index(0) == len(row_bools)-1:
            return False
    return True
        
while True:
    inp = None
    total_input = ""
    atomics = {}
    expressions = []
    while inp != "":
        inp = input("> ")
        if inp != "":
            expressions.append(inp)
        
        for i in range(len(inp)):
            if inp[i].isalpha() and inp[i] not in list(atomics.keys()) and inp[i].isupper():
                atomics[inp[i]] = []

    print(is_valid(atomics, expressions))
    
