def binarySearch(arr, x, low, high):
    if high >= low:
        mid = low + (high-low)//2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            return binarySearch(arr, x, low, mid-1)
        
        else: 
            return binarySearch(arr, x, mid+1, high)
        
    else:
        return -1
    
if __name__ == '__main__':
    arr = list(map(int, input("Enter numbers (sorted): ").split()))
    x = int(input("Enter number to find: "))
    result = binarySearch(arr, x, 0, len(arr) - 1)
    
    if result != -1:
        print("FOUND! It's at index ", result)
    else:
        print("NOT FOUND!") 