import ast


def get_input_from_file():
    with open('input') as f:
        lines = []
        for line in f.readlines():
            data = line.strip('\n')
            lines.append(data)

        return lines


def prepare(node, eval_function):
    if isinstance(node, ast.Module):
        for op in node.body:
            prepare(op, eval_function)
    elif isinstance(node, ast.Expr):
        prepare(node.value, eval_function)
    elif isinstance(node, ast.BinOp):
        eval_function(node)
        prepare(node.left, eval_function)
        prepare(node.right, eval_function)


def eval_function_1(node):
    if isinstance(node.op, ast.Sub):
        node.op = ast.Mult()


def eval_function_2(node):
    if isinstance(node.op, ast.Add):
        node.op = ast.Mult()
    elif isinstance(node.op, ast.Mult):
        node.op = ast.Add()


def translate_function_1(s):
    # To save operation order (+ and * same operation order)
    return s.replace('*', '-')


def translate_function_2(s):
    # To reverse operation order (+ before *)
    return s.translate(str.maketrans({'+': '*', '*': '+'}))


def solve(translate_function, eval_function):
    lines = get_input_from_file()

    total = 0

    for line in lines:
        line = translate_function(line)
        tree = ast.parse(line)
        prepare(tree, eval_function)
        for expr in tree.body:
            total += eval(compile(ast.Expression(expr.value), '', 'eval'))

    return total


def solve_1():
    return solve(translate_function_1, eval_function_1)


def solve_2():
    return solve(translate_function_2, eval_function_2)


if __name__ == '__main__':
    print(solve_1())
    print(solve_2())
