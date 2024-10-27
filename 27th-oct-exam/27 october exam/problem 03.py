
# 3) Remove Duplicates from a List (3 ქულა)
# Create a program that receives a list and removes duplicate elements while maintaining the original order.
# Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']


def remove_duplicates(first_list):
    sett = set()
    result = []
    for i in first_list:
        if i not in sett:
            sett.add(i)
            result.append(i)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5, 6, 6]))




