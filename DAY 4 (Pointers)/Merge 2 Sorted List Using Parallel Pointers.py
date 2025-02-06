arra1 = list(map(int, input().split()))
arra2 = list(map(int, input().split()))

len1 = len(arra1)
len2 = len(arra2)
def parallel_po(arr1, arr2):
    p1, p2 = 0, 0
    sorted_arr = []
    while p1 < len1 and p2 < len2:
        if arr1[p1] < arr2[p2]:
            sorted_arr.append(arr1[p1])
            p1 += 1
        else:
            sorted_arr.append(arr2[p2])
            p2 += 1
    while p1 < len1:
        sorted_arr.append(arr1[p1])
        p1 += 1
    while p2 < len2:
        sorted_arr.append(arr2[p2])
        p2 += 1
    return sorted_arr

print(parallel_po(arra1, arra2))