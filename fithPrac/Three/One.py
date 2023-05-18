import random
import string
from collections import defaultdict
import inspect
import ast


def divide(a, b):
    return a / b if b != 0 else None


class Mutator(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, int) or isinstance(node.value, float):
            return ast.Constant(random.uniform(-1000, 1000))
        elif isinstance(node.value, str):
            return ast.Constant("".join(random.choices(string.ascii_letters + string.digits, k=len(node.value))))
        else:
            return node


def mutate_code(src):
    tree = ast.parse(src)
    Mutator().visit(tree)
    return ast.unparse(tree)


def make_mutants(func, size):
    mutant = src = ast.unparse(ast.parse(inspect.getsource(func)))
    mutants = [src]
    while len(mutants) < size + 1:
        while mutant in mutants:
            mutant = mutate_code(src)
        mutants.append(mutant)
    return mutants[1:]


def mut_test(func, test, size=20):
    survived = []
    mutants = make_mutants(func, size)
    for mutant in mutants:
        try:
            exec(mutant, globals())
            test()
            survived.append(mutant)
        except:
            pass
    return survived


def test_divide_by_nonzero():
    a = random.uniform(-1000, 1000)
    b = random.uniform(-1000, 1000)
    assert divide(a, b) == a / b


def test_divide_by_zero():
    a = random.uniform(-1000, 1000)
    assert divide(a, 0) == None


def test_divide_mutants():
    mutants = mut_test(divide, test_divide_by_nonzero)
    assert mutants == ['return a * b if b != 0 else None\n']
