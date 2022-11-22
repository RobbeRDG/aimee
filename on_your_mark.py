

def issatisfied(a: int, sign: str, b: int) -> bool:
    if sign == '>':
        return a > b
    else:
        return a < b

def correct_signs(int_list: list) -> str:
    solution_str = ""

    for i in range(0, len(int_list) - 1):
        if int_list[i] > int_list[i+1]:
            solution_str += '>'
        else:
            solution_str += '<'
    
    return solution_str
            

def iscorrect(int_list: list, sign_str: str) -> bool:
    sign_list = [*sign_str]

    for i in range(0, len(int_list) - 1):
        if not issatisfied(int_list[i], sign_list[i], int_list[i+1]):
            return False

    return True

def number_placement(int_list: list, sign_str: str) -> list:
    # Sort the int list
    int_list.sort()

    # Create a new list to contain  the sollution
    solution = []

    # Iterate over the signs
    for sign in [*sign_str]:
        if sign == '>':
            # Take the biggest number and place it in the solution
            solution.append(int_list[-1])

            # Remove final element from int list
            int_list = int_list[:-1]
        else:
            # Take the smallest number and place it in the solution
            solution.append(int_list[0])

            # Remove first element from int list
            int_list = int_list[1:]

    # Add final element to solution
    solution.append(int_list[0])
    
    return solution

def count_sign_occurences(sign_str: str) -> list:
    gt_count = 0
    lt_count = 0

    for sign in sign_str.split():
        if sign == '>':
            gt_count += 1
        else:
            lt_count += 1

    return gt_count, lt_count

def sign_placement(int_list: list, sign_str: str) -> str:
    # Get the correct signs 
    solution_str = correct_signs(int_list)

    # Count the sign occurences in the correct solution
    correct_gt_count, correct_lt_count = count_sign_occurences(solution_str)

    # Count the sign occurences in the given sign string
    given_gt_count, given_lt_count = count_sign_occurences(sign_str)

    if (correct_gt_count == given_gt_count) and (correct_lt_count == given_lt_count):
        return solution_str
    else:
        return 'no solution'


def assessment(int_list: list, sign_str: str) -> str:
    sign_list = [*sign_str]
    solution = ''

    for i in range(0, len(int_list) - 1):
        if not issatisfied(int_list[i], sign_list[i], int_list[i+1]):
            solution += f'{int_list[i]} !{sign_list[i]} {int_list[i+1]}'
        else:
            solution += f'{int_list[i]} {sign_list[i]} {int_list[i+1]}'

    return solution


if __name__ == '__main__':
    print(issatisfied(13,'<',42))
    print(issatisfied(13,'>',42))

    print(correct_signs([2,0,1,5]))
    print(correct_signs([0,5,1,2]))

    print(iscorrect([2,0,1,5], '<><'))
    print(iscorrect([0,5,1,2], '<><'))

    print(number_placement([2,0,1,5], '<><'))
    print(number_placement([66,95,6,7,73,97,69,68,51,21,3,93,58,42,54,19], '<>>>>>><>><<><<'))

    print(sign_placement([2,0,1,5], '<><'))
    print(sign_placement([66,95,6,7,73,97,69,68,51,21,3,93,58,42,54,19], '<>>>>>><>><<><<'))