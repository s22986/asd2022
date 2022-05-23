import timeit
from random import random


def partition(A, p, r):
    j = p - 1
    i = p

    while len(A) > i:
        if A[i] <= A[r]:
            j = j + 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            i = i + 1
        else:
            i = i + 1
    return j


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


def max_heapify(A, n, i):
    l = (2 * i) + 1
    r = (2 * i) + 2
    if l <= (n - 1) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= (n - 1) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def heap_sort(A):
    n = len(A)
    for i in range((n - 1) // 2, -1, -1):
        max_heapify(A, n, i)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        max_heapify(A, i, 0)


def bubble_sort(A):
    n = len(A) - 1
    for i in range(0, n - 1):
        for j in range(0, n - i):
            if A[j] <= A[j + 1]:
                continue
            A[j], A[j + 1] = A[j + 1], A[j]


if __name__ == '__main__':
    random_arr = [int(random() * 100000 + 1) for _ in range(300000)]
    sorted_arr = [i for i in range(1, 300000)]
    unsorted_arr = [i for i in range(300000, 1, -1)]

    # Algorytm się nie wykona ponieważ python ma określony limit rekursji który jest zbyt mały dla tylu liczb
    # quick_time_random = timeit.Timer(lambda: quick_sort(random_arr, 0, len(random_arr) - 1))
    # quick_time_sorted = timeit.Timer(lambda: quick_sort(sorted_arr, 0, len(sorted_arr) - 1))
    # quick_time_unsorted = timeit.Timer(lambda: quick_sort(unsorted_arr, 0, len(unsorted_arr) - 1))

    # print("Time for quick sort random array: " + str(quick_time_random.timeit(1)))
    # print("Time for quick sort sorted array: " + str(quick_time_sorted.timeit(1)))
    # print("Time for quick sort unsorted array: " + str(quick_time_unsorted.timeit(1)))

    merge_time_random = timeit.Timer(lambda: merge_sort(random_arr))
    merge_time_sorted = timeit.Timer(lambda: merge_sort(sorted_arr))
    merge_time_unsorted = timeit.Timer(lambda: merge_sort(unsorted_arr))

    print("Time for merge sort random array: " + str(merge_time_random.timeit(1)))
    print("Time for merge sort sorted array: " + str(merge_time_sorted.timeit(1)))
    print("Time for merge sort unsorted array: " + str(merge_time_unsorted.timeit(1)))

    heap_time_random = timeit.Timer(lambda: heap_sort(random_arr))
    heap_time_sorted = timeit.Timer(lambda: heap_sort(sorted_arr))
    heap_time_unsorted = timeit.Timer(lambda: heap_sort(unsorted_arr))

    print("Time for heap sort random array: " + str(heap_time_random.timeit(1)))
    print("Time for heap sort sorted array: " + str(heap_time_sorted.timeit(1)))
    print("Time for heap sort unsorted array: " + str(heap_time_unsorted.timeit(1)))

    bubble_time_random = timeit.Timer(lambda: bubble_sort(random_arr))
    bubble_time_sorted = timeit.Timer(lambda: bubble_sort(sorted_arr))
    bubble_time_unsorted = timeit.Timer(lambda: bubble_sort(unsorted_arr))

    print("Time for bubble sort random array: " + str(bubble_time_random.timeit(1)))
    print("Time for bubble sort sorted array: " + str(bubble_time_sorted.timeit(1)))
    print("Time for bubble sort unsorted array: " + str(bubble_time_unsorted.timeit(1)))
