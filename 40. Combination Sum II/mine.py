candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

ans = []
candidates.sort()


def backtrack(index, curr, total):

    if total == target:
        ans.append(curr[::])
        return

    if index >= len(candidates) or total > target:
        return

    # Calling backtrack for left branch including the element
    curr.append(candidates[index])
    backtrack(index+1, curr, total+candidates[index])
    curr.pop()

    # Calling the right branch as not including the candidates[index]
    # We have to skip the duplicate values to avoid same answer

    while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
        index += 1

    backtrack(index+1, curr, total)


backtrack(0, [], 0)

print(ans)
