def reverse_list(lst):
    # Your code goes here
    reversed = []

    for i in range(len(lst) - 1, -1, -1):
        reversed.append(lst[i])

    return reversed
