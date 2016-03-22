__author__ = 'Matej Zrimsek'

import types
import random

def dataInput(file):
    lines = open(file).read().splitlines()
    exp = []
    for line in lines:
        if line[0] == 'c':
            continue
        elif line[0] == 'p':
            nrOfVars = int(line.split()[2])
        else:
            exp.append(map(int, line.split()[:-1]))
    return nrOfVars, exp

def solveSAT(exp):
    solution = set()
    vars = range(-nrOfVars, 0) + range(1, nrOfVars+1)
    while True:
        satisfiable = processIdentities(exp)
        if satisfiable is not None:
            break

        newExp = processReduction(exp, solution)
        if newExp is not None:
            exp = newExp
            continue

        element = vars[random.randint(0, len(vars)-1)]
        exp = insertValue(element, exp, solution)

    return (satisfiable, sorted(solution))

def processIdentities(exp):
    if len(exp) == 0:
        return True
    for clause in exp:
        if len(clause) == 0:
            return False
    return None

def processReduction(exp, solution):
    tautologyClauseVars = set()
    newExp = []
    for clause in exp:
        if len(clause) == 1 and type(clause[0]) == types.IntType:
            tautologyClauseVars.add(clause[0])

    if len(tautologyClauseVars) == 0:
        return None
    for i in tautologyClauseVars:
        if i not in solution and -i not in solution:
            solution.add(i)

    for clause in exp:
        newClause = []
        for literal in clause:
            if literal in tautologyClauseVars:
                newClause = []
                break
            if -literal not in tautologyClauseVars:
                newClause.append(literal)
        if len(newClause) != 0:
            newExp.append(newClause)

    return newExp

def insertValue(lit ,exp, solution):
    newExp = []
    for clause in exp:
        newClause = []
        for l in clause:
            if l == lit:
                l = True
            elif l == -lit:
                l = False
            anyTrue = l == True and type(l) == types.BooleanType
            if anyTrue:
                break
            newClause.append(l)

        if not anyTrue:
            newClause = [x for x in newClause if type(x) == types.IntType]
            newExp.append(newClause)

    if lit in solution or -lit in solution:
        return exp
    solution.add(lit)
    return newExp




nrOfVars, exp = dataInput("test_file.txt")
# nrOfVars, exp = dataInput("dimacs/sudoku1.txt")
# nrOfVars, exp = dataInput("dimacs/sudoku2.txt")

(satisfiable, solution) =  solveSAT(exp)

if(satisfiable):
    print "Satisfiable", solution
else :
    print "Not satisfiable", solution