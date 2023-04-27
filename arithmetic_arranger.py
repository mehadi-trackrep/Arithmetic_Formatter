from arithmatic_problem_validator import ArithmaticProblemValidator

def arithmetic_arranger(problems: list[str], display=False):
    print(problems)
    arithmatic_problem_validator_obj = ArithmaticProblemValidator(problems)
    if arithmatic_problem_validator_obj.is_too_many_problems():
        return 'Error: Too many problems.'
    elif arithmatic_problem_validator_obj.is_inappropriate_operators():
        return 'Error: Operator must be '+' or '-'.'
    elif arithmatic_problem_validator_obj.is_non_digits():
        return 'Error: Numbers must only contain digits.'
    # elif arithmatic_problem_validator_obj. :
    #     ...