def arrayProductExceptSelf(arr):
    n = len(arr)
    L, R, ans = [0] * n, [0] * n, [0] * n
    L[0] = 1
    for i in range(1, n):
        L[i] = arr[i - 1] * L[i - 1]
    R[n - 1] = 1
    for i in reversed(range(n - 1)):
        R[i] = arr[i + 1] * R[i + 1]
    for i in range(n):
        ans[i] = L[i] * R[i]
    return ans


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(arrayProductExceptSelf(arr))
