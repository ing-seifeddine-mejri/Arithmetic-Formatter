def arithmetic_arranger(problems, results=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    r1 = ''
    r2 = ''
    r3 = ''
    r4 = ''

    for i, problem in enumerate(problems):
        no1, op, no2 = problem.split()

        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not no1.isdigit() or not no2.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(no1) > 4 or len(no2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if op == '+':
            result = int(no1) + int(no2)
        else:
            result = int(no1) - int(no2)

        spaces = max(len(no1), len(no2)) + 2

        r1 += no1.rjust(spaces)
        r2 += op + no2.rjust(spaces - 1)
        r3 += '-' * int(spaces)
        r4 += str(result).rjust(spaces)

        if i < len(problems) - 1:
            r1 += ' ' * 4
            r2 += ' ' * 4
            r3 += ' ' * 4
            r4 += ' ' * 4

    # Result conditions:
    arranged_problems = r1 + "\n" + r2 + "\n" + r3

    if results:
        arranged_problems += "\n" + r4

    return arranged_problems
