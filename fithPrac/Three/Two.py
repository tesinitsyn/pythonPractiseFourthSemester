import random
import string
from collections import defaultdict
import inspect
import ast


class Mutator(ast.NodeTransformer):
    BINARY_OPERATORS = [
        ast.Add(),
        ast.Sub(),
        ast.Mult(),
        ast.Div(),
        ast.Mod(),
        ast.Pow(),
        ast.LShift(),
        ast.RShift(),
        ast.BitOr(),
        ast.BitXor(),
        ast.BitAnd(),
        ast.FloorDiv(),
    ]

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            return ast.BinOp(self.visit(node.left), random.choice(self.BINARY_OPERATORS), self.visit(node.right))
        elif isinstance(node.op, ast.Sub):
            return ast.BinOp(self.visit(node.left), random.choice(self.BINARY_OPERATORS), self.visit(node.right))
        elif isinstance(node.op, ast.Mult):
            return ast.BinOp(self.visit(node.left), random.choice(self.BINARY_OPERATORS), self.visit(node.right))
        elif isinstance(node.op, ast.Div):
            return ast.BinOp(self.visit(node.left), random.choice(self.BINARY_OPERATORS), self.visit(node.right))
        else:
            return node

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


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def test_bubble_sort():
    lst = [random.randint(0, 100) for _ in range(10)]
    assert bubble_sort(lst) == sorted(lst)


def test_bubble_sort_mutants():
    mutants = mut_test(bubble_sort, test_bubble_sort)
    assert len(mutants) == 1
