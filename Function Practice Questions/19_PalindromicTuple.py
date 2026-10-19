def is_palindromic_tuple(tup):
    left = 0
    right = len(tup) - 1

    while left < right:
        if tup[left] != tup[right]:
            return False

        left += 1
        right -= 1

    return True