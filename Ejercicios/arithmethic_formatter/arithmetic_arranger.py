
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_line = ""
    middle_line = ""
    bottom_line = ""
    results_line = ""

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_length = max(len(num1), len(num2))

        top_line += num1.rjust(max_length + 2)
        middle_line += operator + num2.rjust(max_length + 1)
        bottom_line += "-" * (max_length + 2)

        if problem != problems[-1]:
            top_line += "    "
            middle_line += "    "
            bottom_line += "    "

        if show_answers:
            if operator == '+':
                result = int(num1) + int(num2)
            else:
                result = int(num1) - int(num2)

            results_line += str(result).rjust(max_length + 2) + ("    ")

    arranged_problems = top_line + "\n" + middle_line + "\n" + bottom_line

    if show_answers:
        arranged_problems += "\n" + results_line.rstrip()
    return(arranged_problems)
  