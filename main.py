from arithmetic_arranger import arithmetic_arranger

if __name__=='__main__':
    all_problems = [
        ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
        ,["32 + 8", "1 - 3801", "9999 + 9999", "44 - 44", "mehadi"]
        ,["32 + 8", "1 - 3801", "9999 + 9999", "523 / 49", "44 - 44"]
        ,["32 + 8", "1 - 3801", "9999 + 99991", "523 - 49"]
    ]
    for each_problem_set in all_problems:
        print(each_problem_set)
        print(arithmetic_arranger(each_problem_set, True))
        print(arithmetic_arranger(each_problem_set))
        print("======\t======\t======\t======\t======\t======\n")