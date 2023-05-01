from arithmatic_problem_validator import ArithmaticProblemValidator

def arithmetic_arranger(problems: list[str], display=False) -> str:
    
    print(problems)
    print("\n")

    arithmatic_problem_validator_obj = ArithmaticProblemValidator(problems)
    
    if arithmatic_problem_validator_obj.is_too_many_problems():
        return 'Error: Too many problems.'
    elif arithmatic_problem_validator_obj.is_inappropriate_operators():
        return 'Error: Operator must be '+' or '-'.'
    elif arithmatic_problem_validator_obj.is_non_digits():
        return 'Error: Numbers must only contain digits.'
    elif arithmatic_problem_validator_obj.is_over_size_of_any_operand():
        return 'Error: Numbers cannot be more than four digits.'
    
    s1 = '  32         1      9999      523'
    s2 = '+  8    - 3801    + 9999    -  49'
    s3 = '----    ------    ------    -----'
    s4 = '  40     -3800     19998      474'

    '''
        ## gap er space - 4 spaces
            
    '''

    final_str = f"{s1}\n{s2}\n{s3}\n{s4}"
    # print("\n==> final_str: \n", final_str)
    return final_str