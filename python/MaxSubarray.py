def kadane (arr):
    maxC = maxG = arr[0]
    for i in range (1, len(arr)):
        maxC = max(arr[i], maxC + arr[i])
        maxG = max(maxG, maxC)
    return maxG

def DAndC (arr, left, right):
    if left == right:
        return arr[left]
    
    mid = (left + right) // 2
    maxLeft = DAndC(arr, left, mid)
    maxRight = DAndC(arr, mid + 1, right)
    maxCrossing = maxSubarrayCrossing(arr, right, left, mid)
    return max(maxLeft, maxRight, maxCrossing)

def maxSubarrayCrossing (arr, right, left, mid):
    Lsum = float('-inf')
    total = 0
    for i in range (mid, left - 1, -1):
        total += arr[i]
        Lsum = max(Lsum, total)

    Rsum = float('-inf')
    total = 0
    for i in range (mid + 1, right + 1):
        total += arr[i]
        Rsum = max(Rsum, total)

    return Lsum + Rsum

arr = [-3, 1, -8, 12, 0, -3, 5, -9, 4]
print("Array: ", arr)
print("Kadane's: ", kadane(arr))
print("D & C: ", DAndC(arr, 0, len(arr) - 1))
