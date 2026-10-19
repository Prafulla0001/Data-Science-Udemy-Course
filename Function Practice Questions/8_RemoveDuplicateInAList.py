def remove_duplicates(lst):
    # Your code goes here
    list1 = set(lst)
    return list(list1)


### Without using set 
def remove_duplicates(lst):
    result = []

    for i in range(len(lst)):
        duplicate = False

        for j in range(len(result)):
            if lst[i] == result[j]:
                duplicate = True
                break

        if not duplicate:
            result.append(lst[i])

    return result