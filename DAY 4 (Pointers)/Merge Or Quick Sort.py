import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [i for i in arr if i < pivot]
    middle = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return quick_sort(left) + middle + quick_sort(right)

array = list(map(int, input().split()))

start_time = time.time()
sorted_array = quick_sort(array)
end_time = time.time()

print("Sorted array:", sorted_array)
print("Time taken:", end_time - start_time, "seconds")