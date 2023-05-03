import re
from arithmatic_problem_validator import ArithmaticProblemValidator

FOUR_WHITE_SPACES = '    ' ## 4 spaces

def arithmetic_arranger(problems: list[str], display=False) -> str:
    
    arithmatic_problem_validator_obj = ArithmaticProblemValidator(problems)
    
    if arithmatic_problem_validator_obj.is_too_many_problems():
        return 'Error: Too many problems.'
    elif arithmatic_problem_validator_obj.is_inappropriate_operators():
        return "Error: Operator must be '+' or '-'."
    elif arithmatic_problem_validator_obj.is_non_digits():
        return 'Error: Numbers must only contain digits.'
    elif arithmatic_problem_validator_obj.is_over_size_of_any_operand():
        return 'Error: Numbers cannot be more than four digits.'
    
    """
        s1 = '  32         1      9999      523'
        s2 = '+  8    - 3801    + 9999    -  49'
        s3 = '----    ------    ------    -----'
        s4 = '  40     -3800     19998      474'
    """

    s1 = ''
    s2 = ''
    s3 = ''
    s4 = ''

    flag = False

    for each_problem in problems:
        temp = re.sub(r'\s', '', each_problem)
        splitted_list = temp.split('+') if '+' in temp else temp.split('-')
        
        if display:
            arithmatic_result = str(int(splitted_list[0]) + int(splitted_list[1])) if '+' in temp \
                            else str(int(splitted_list[0]) - int(splitted_list[1]))
        big_operand_len = len(splitted_list[0]) if len(splitted_list[0]) >= len(splitted_list[1]) \
                        else len(splitted_list[1])
        
        mx_len = big_operand_len+2

        if not flag:
            s1 = ' '*(mx_len - len(splitted_list[0])) + splitted_list[0]
            s2 = ('+' if '+' in temp else '-') + ' '*(mx_len - len(splitted_list[1]) - 1) + splitted_list[1]
            s3 = '-'*mx_len
            if display:
                s4 = ' '*(mx_len - len(arithmatic_result)) + arithmatic_result
            flag = True
        else:
            s1 = s1 + FOUR_WHITE_SPACES + ' '*(mx_len - len(splitted_list[0])) + splitted_list[0]
            s2 = s2 + FOUR_WHITE_SPACES + ('+' if '+' in temp else '-') + \
                ' '*(mx_len - len(splitted_list[1]) - 1) + splitted_list[1]
            s3 = s3 + FOUR_WHITE_SPACES + '-'*mx_len
            if display:
                s4 = s4 + FOUR_WHITE_SPACES + ' '*(mx_len - len(arithmatic_result)) + arithmatic_result

        # print(f"{s1}\n{s2}\n{s3}\n{s4}")
        # print(arithmatic_result)
        # print(big_operand_len)
        # print("############")

    if display:
        return f"{s1}\n{s2}\n{s3}\n{s4}"
    else:
        return f"{s1}\n{s2}\n{s3}"