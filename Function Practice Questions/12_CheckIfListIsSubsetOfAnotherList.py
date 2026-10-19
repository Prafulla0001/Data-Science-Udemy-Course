def is_subset(lst1, lst2):
    for i in lst1:
        found = False

        for j in lst2:
            if i == j:
                found = True
                break

        if not found:
            return False

    return True