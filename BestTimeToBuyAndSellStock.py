def bestTimeToBuyAndSellStock(arr):
    minVal, maxVal = float('inf'), 0
    for i in range(len(arr)):
        minVal = min(minVal,arr[i])
        maxVal = max(maxVal,arr[i]-minVal)
    return maxVal

if __name__ == '__main__':
    arr = [7, 1, 5, 3, 6, 4]
    print(bestTimeToBuyAndSellStock(arr))
