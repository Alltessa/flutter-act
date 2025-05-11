def addMatrix(arr1, arr2):
    n = len(arr1)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result [i][j] = arr1[i][j] + arr2[i][j]

    return result

def multiplyMatrix(arr1, arr2):
    n = len(arr1)
    result = [[0]*n for _ in range(n)]

    if n == 1:
        result[0][0] = arr1[0][0] * arr2[0][0]
        return result
    
    subMatrix = [[[0]*(n//2) for _ in range(n//2)] for _ in range(8)]

    for i in range(n//2):
        for j in range(n//2):
            subMatrix[0][i][j] = arr1[i][j]
            subMatrix[1][i][j] = arr1[i][j + n // 2]
            subMatrix[2][i][j] = arr1[i + n // 2][j]
            subMatrix[3][i][j] = arr1[i + n // 2][j + n // 2]
            subMatrix[4][i][j] = arr2[i][j]
            subMatrix[5][i][j] = arr2[i][j + n // 2]
            subMatrix[6][i][j] = arr2[i + n // 2][j]
            subMatrix[7][i][j] = arr2[i + n // 2][j + n // 2]
    
    resultMatrix = [[[0]*(n//2) for _ in range(n//2)] for _ in range(4)]

    resultMatrix[0] = addMatrix(multiplyMatrix(subMatrix[0], subMatrix[4]), multiplyMatrix(subMatrix[1], subMatrix[6]))
    resultMatrix[1] = addMatrix(multiplyMatrix(subMatrix[0], subMatrix[5]), multiplyMatrix(subMatrix[1], subMatrix[7]))
    resultMatrix[2] = addMatrix(multiplyMatrix(subMatrix[2], subMatrix[4]), multiplyMatrix(subMatrix[3], subMatrix[6]))
    resultMatrix[3] = addMatrix(multiplyMatrix(subMatrix[2], subMatrix[5]), multiplyMatrix(subMatrix[3], subMatrix[7]))

    for i in range(n//2):
        for j in range(n//2):
            result[i][j] = resultMatrix[0][i][j]
            result[i][j + n // 2] = resultMatrix[1][i][j]
            result[i + n // 2][j] = resultMatrix[2][i][j]
            result[i + n // 2][j + n // 2] = resultMatrix[3][i][j]
    
    return result

arr1 = [[1,3],[5,7]]
arr2 = [[2,4],[6,8]]
result = multiplyMatrix(arr1, arr2)
print("Array 1: ", arr1)
print("Array 2: ", arr2)
print("Result: ")
for row in result:
    print(row)

            