from arithmatic_problem_validator import ArithmaticProblemValidator

def test_too_many_problems():
    arithmatic_validator_obj = ArithmaticProblemValidator(
        problems=["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "523 - 649", "523 + 49"]
    )
    assert True == arithmatic_validator_obj.is_too_many_problems()

def test_inappropriate_operators():
    arithmatic_validator_obj = ArithmaticProblemValidator(
        problems=["32 + 8", "1 - 3801", "9999 + 9999", "523 / 49", " 44 - 44"]
    )
    assert True == arithmatic_validator_obj.is_inappropriate_operators()

def test_non_digits():
    arithmatic_validator_obj = ArithmaticProblemValidator(
        problems=["32 + 8", "1 - 3801", "9999 + 9999", "44 - 44", "mehadi"]
    )
    assert True == arithmatic_validator_obj.is_non_digits()

def test_over_size_of_any_operand():
    arithmatic_validator_obj = ArithmaticProblemValidator(
        problems=["32 + 8", "1 - 3801", "9999 + 99991", "523 - 49"]
    )
    assert True == arithmatic_validator_obj.is_over_size_of_any_operand()