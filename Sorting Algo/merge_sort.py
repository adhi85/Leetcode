#Without space complexity With SC is down
def merge_sort(arr):
    if len(arr) <= 1:
        return 
    mid = len(arr)//2

    left  = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted_lists(left,right,arr)

def merge_sorted_lists(list1,list2,arr):
    len_1 = len(list1)
    len_2 = len(list2)
    i=j =k= 0

    while i<len_1 and j <len_2:
        if list1[i]<=list2[j]:
            arr[k] = list1[i]
            # sorted_list.append(list1[i])
            i+=1
        else:
                arr[k] = list2[j]
                # arr.append(list2[j])
                j+=1
        k+=1

    while i <len_1:
        arr[k] = list1[i]
        k+=1
        # arr.append(list1[i])
        i += 1
    while j <len_2:
        arr[k] = list2[j]
        # arr.append(list2[j])
        j += 1
        k+=1

    

a = [4,3,2]
b = [2,4,6,8]

merge_sort(a)
print(a)


# With Space complexity
# def merge_sort(arr):
#     if len(arr) <= 1:
#           return arr
#     mid = len(arr)//2

#     # left  = arr[:mid]
#     # right = arr[mid:]

#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge_sorted_lists(left,right)

# def merge_sorted_lists(list1,list2):
#     sorted_list = []
#     len_1 = len(list1)
#     len_2 = len(list2)
#     i=j = 0

#     while i<len_1 and j <len_2:
#         if list1[i]<=list2[j]:
#             sorted_list.append(list1[i])
#             i+=1
#         else:
#                 sorted_list.append(list2[j])
#                 j+=1
#     while i <len_1:
#         sorted_list.append(list1[i])
#         i += 1
#     while j <len_2:
#         sorted_list.append(list2[j])
#         j += 1

#     return sorted_list

# a = [4,3,2]
# b = [2,4,6,8]

# print(merge_sort(a))