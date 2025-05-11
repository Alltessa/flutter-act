def partition(arr, low, high):
    p = arr[high]
    i = low - 1

    for n in range (low, high):
        if arr[n] < p:
            i += 1
            arr[i], arr[n] = arr[n], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
    
def quickSort(arr, low, high):
    if low < high:
        pvt = partition(arr, low, high)

        quickSort(arr, low, pvt - 1)
        quickSort(arr, pvt + 1, high)

if __name__ == "__main__":
    arr = [2, 14, 4, 12, 6, 10, 8]
    print("Unsorted array: \n",arr)
    x = len(arr)

    quickSort(arr, 0, x - 1)

    print("Sorted Array: ")
    for value in arr:
        print(value, end=" ")