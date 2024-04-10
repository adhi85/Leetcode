weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

# check if the capacity is feasible or not
# if the capacity is feasible then return True otherwise return False
def isFeasible(capacity):
    day = 1
    total = 0

    for wt in weights:
        total += wt

        if total > capacity:
            day += 1
            total = wt

            if day > days:
                return False
    return True


# left is the maximum weight of the packages, right is the sum of the weights
# because the minimum capacity is the maximum weight of the packages otherwise the packages can't be shipped
# the maximum capacity is the sum of the weights otherwise the packages can be shipped in one day
left,right = max(weights), sum(weights)

while left < right:

    mid = (left+right) >> 1

    if isFeasible(mid):
        right = mid
    else:
        left = mid + 1

print(left)
