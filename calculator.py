from sympy import *

def equation_solver(expr):
    expr=expr.replace('÷','/')
    ans=expand(parse_expr(expr))
    return latex(ans)
def quadratic(a, b, c):
    a=parse_expr(a)
    b=parse_expr(b)
    c=parse_expr(c)

    delta = b ** 2 - 4 * a * c

    x_1 = (-b + sqrt(delta)) / (2 * a)
    x_2 = (-b - sqrt(delta)) / (2 * a)
    return x_1, x_2


def main():
    a = float(input('please enter a number:'))
    b = float(input('please enter a number:'))
    c = float(input('please enter a number:'))
    print('Results are:', quadratic(a, b, c))


if __name__ == '__main__':
    main()
