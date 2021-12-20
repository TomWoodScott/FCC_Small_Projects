def arithmetic_arranger(args, Ans=False):
    combined_list = []
    first_line_list = []
    second_line_list = []
    dash_line_list = []
    answers_line_list = []

    # to many arguments error message
    arguments = len(args)
    if arguments > 5:
        return "Error: Too many problems."

    # Main Loop
    for formula in args:
        temp = formula.split()
        combined_list.append(temp)
        first_number, operation_type, second_number = temp[0], temp[1], temp[2]

        # check number length error message
        if len(first_number) >= 5 or len(second_number) >= 5:
            return "Error: Numbers cannot be more than four digits."

        # check type is numbers error message
        if not str(first_number).isnumeric() or not str(second_number).isnumeric():
            return "Error: Numbers must only contain digits."

        # ans list and check accepted operator error message
        if operation_type == "+":
            answer = float(first_number) + float(second_number)
        elif operation_type == "-":
            answer = float(first_number) - float(second_number)
        else:
            return "Error: Operator must be '+' or '-'."

        # converting lists to string, check length of each element to add appropriate padding

        if len(first_number) >= len(second_number):
            sum_extension = len(first_number)
        else:
            sum_extension = len(second_number)

        # string.rjust(*, insert), leaving space on line two to concatenate the operation

        first_line_list.append(str(first_number).rjust(sum_extension + 2))
        second_line_list.append(operation_type + str(second_number).rjust(sum_extension + 1))
        dash_line_list.append('-' * (sum_extension + 2))
        answers_line_list.append(str(int(answer)).rjust(sum_extension + 2))

    # OUT OF LOOP, list -> str

    first_line_str = '    '.join(first_line_list)
    second_line_str = '    '.join(second_line_list)
    dash_line_str = '    '.join(dash_line_list)
    answers_line_str = '    '.join(answers_line_list)

    # Ans = True or False
    if Ans:
        return first_line_str + "\n" + second_line_str + "\n" + dash_line_str + "\n" + answers_line_str
    else:
        return first_line_str + "\n" + second_line_str + "\n" + dash_line_str


print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
print(arithmetic_arranger(['3 + 855', '988 + 40'], False))

