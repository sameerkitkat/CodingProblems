def subarraysWithGivenSum(arr,k):
    arrSum = count = 0
    myDict = {0 : 1}
    for i in range(0, len(arr)):
        arrSum += arr[i]
        count += myDict.get(arrSum - k, 0)
        myDict[arrSum] = myDict.get(arrSum, 0) + 1
    return count

if __name__ == '__main__':
    arr = [1, 2, 3]
    k = 3
    print(subarraysWithGivenSum(arr,k))
