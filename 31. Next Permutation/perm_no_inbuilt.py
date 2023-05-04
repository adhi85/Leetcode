def permutations(lst):
    # base case
    if len(lst) == 0:
        return [[]]
    
    # recursive case
    perms = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i+1:]
        for perm in permutations(rest):
            perms.append([lst[i]] + perm)
    return perms

            

nums = [3,1,2]
print(permutations(nums))