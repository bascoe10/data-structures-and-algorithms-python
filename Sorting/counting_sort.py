def countingSort(A):
    k = max(A) + 1
    C = [0] * k
    B = [0] * len(A)
    for j in range(len(A)):
        C[A[j]] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i-1]

    for j in reversed(range(len(A))):
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= C[A[j]]
    return B
