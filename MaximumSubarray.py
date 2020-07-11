def maximumSubarray(arr):
    maxSum = currentSum = arr[0]
    for i in range(1,len(arr)):
        currentSum = max(arr[i],currentSum+arr[i])
        maxSum = max(maxSum,currentSum)
    return maxSum

if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maximumSubarray(arr))
