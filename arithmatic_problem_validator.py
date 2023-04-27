import re


class ArithmaticProblemValidator:
    def __init__(self, problems: list[str]):
        self.problems = problems
    def is_too_many_problems(self) -> bool:
        return True if len(self.problems) > 5 else False
    def is_inappropriate_operators(self) -> bool:
        return True if (
            "#".join(self.problems).find('*') != -1 or "#".join(self.problems).find('/') != -1
        ) else False
    def is_non_digits(self) -> bool:
        joined_str = "".join(self.problems)
        sub_str = re.sub(r'\d*|\-*|\+*', '', joined_str).strip()
        return True if sub_str else False
    def is_over_size_of_any_operand(self) -> bool:
        for each_problem in self.problems:
            ...
    