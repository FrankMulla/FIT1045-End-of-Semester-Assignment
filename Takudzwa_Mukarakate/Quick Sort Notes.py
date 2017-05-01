List = []

def quick_sort(array):
    start = 0
    end = len(array) - 1
    quick_sort_aux(array, start, end)

def partition(array, start, end):
    pivot = array[start]
    boundary = start
    for k in range(start+1,end+1):
        if array[k] < pivot:
            boundary += 1
            array[k],array[boundary] = array[boundary], array[k]
    array[boundary],array[start] = array[start], array[boundary]
    return boundary

def quick_sort_aux(array, start, end):
    print(start)
    if start < end:
        boundary = partition(array, start, end)
        quick_sort_aux(array, start, boundary - 1)
        quick_sort_aux(array, boundary + 1, end)
import random
for i in range(8):
    List.append(random.randint(0,20))
print(List)
quick_sort(List)
print(List)

