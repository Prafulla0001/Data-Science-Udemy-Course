def check_unique(lst):
    # Your code goes here
    for i in range(0,len(lst)):
        for j in range(i+1, len(lst)):
            if(lst[i] == lst[j]):
                return False
    return True
