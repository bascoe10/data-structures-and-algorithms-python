import math


def mergeSort(arr):
    def __merge(p, q, r):
        n1 = q - p + 1
        n2 = r - q
        L = [0] * (n1 + 1)
        R = [0] * (n2 + 1)
        L[-1] = math.inf
        R[-1] = math.inf

        for i in range(n1):
            L[i] = arr[p + i]

        for j in range(n2):
            R[j] = arr[q + j + 1]

        i = j = 0
        for k in range(p, r+1):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

    def merge_sort(p, r):
        if p < r:
            q = (p + r) // 2
            merge_sort(p, q)
            merge_sort(q+1, r)
            __merge(p, q, r)
    merge_sort(0, len(arr)-1)
    return arr
