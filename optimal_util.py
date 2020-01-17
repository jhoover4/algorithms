# Amazon | OA 2019 | Optimal Utilization

# Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the
# second integer represents a value. Your task is to find an element from a and an element form b such that the sum of
# their values is less or equal to target and as close to target as possible. Return a list of ids of selected elements.
# If no pair is possible, return an empty list.


def optimal_util(first_lis, second_lis, target):
    """
    Sorts lists then uses two pointers to find most optimal sets.

    Time complexity: Sorts take O(n log n) time and pointers take O(n). Final results is O(n log n).

    :param List first_lis:
    :param List second_lis:
    :param int target:
    :return:
    """

    if not first_lis or not second_lis:
        return []

    first_lis = sorted(first_lis, key=lambda x: x[1])
    second_lis = sorted(second_lis, key=lambda x: x[1])
    closest_diff = target
    result = list()

    i = 0
    j = len(second_lis) - 1
    while i < len(first_lis) and j >= 0:
        el_sum = first_lis[i][1] + second_lis[j][1]
        if target < el_sum:
            j -= 1
        else:
            diff = target - el_sum
            if diff == closest_diff:
                result.append([first_lis[i][0], second_lis[j][0]])
            elif diff <= closest_diff:
                result = [[first_lis[i][0], second_lis[j][0]]]
                closest_diff = diff

            i += 1

    return result



