def feasible(pair):
    return True

def getOptimal(item):
    item.sort()
    result = []
    left = 0
    right = len(item) - 1

    while left < right:
        i = (item[left], item[right])

        if feasible(i):
            result = result + [i]

        left += 1
        right -= 1
    
    return result

if __name__ == "__main__":
    item = [6, 3, 2, 7, 5, 5]
    pairs = getOptimal(item)

    print("Sorted Tasks:", item)
    print("Pair Sum:")
    for pair1, pair2 in pairs:
        print(f"{pair1} + {pair2} = {pair1 + pair2}")
