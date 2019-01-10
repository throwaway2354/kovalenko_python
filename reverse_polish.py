from math import sin, cos, sqrt

stack = []
variables = {}
expression = input().split()
while True:
    try:
        name, value = input().split('=')
        variables[name] = float(value)
    except Exception:
        break

try:
    for token in expression:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            b, a = stack.pop(), stack.pop()
            stack.append(a / b)

        elif token == 'abs':
            stack.append(abs(stack.pop()))
        elif token == 'sin':
            stack.append(sin(stack.pop()))
        elif token == 'cos':
            stack.append(cos(stack.pop()))
        elif token == 'sqrt':
            stack.append(sqrt(stack.pop()))

        else:
            try:
                stack.append(variables[token])
            except KeyError:
                stack.append(float(token))

    assert len(stack) == 1

    print(f'{stack.pop():.3f}')
except Exception:
    print('ERROR')
