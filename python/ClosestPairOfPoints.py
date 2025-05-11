def distance(pair1, pair2):
    distanceX = pair1[0] - pair2[0]
    distanceY = pair1[1] - pair2[1]

    return (distanceX * distanceX + distanceY * distanceY) ** 0.5

def bruteForce(points):
    minDistance = float ('inf')
    pair = (None, None)
    n = len(points)

    for i in range(n):
        for j in range(i+1, n):
            dist = distance(points[i], points[j]) 
            if dist < minDistance:
                minDistance = dist
                pair = (points[i], points[j])

    return minDistance, pair

def closestSplitPair(pairX, pairY, delta, bestPair):
    midX = pairX[len(pairX)//2][0]
    inStrip = []
    
    for p in pairY:
        if abs(p[0] - midX) < delta:
            inStrip.append(p)

    minDistance = delta
    n = len(inStrip)

    for i in range(n):
        for j in range(i + 1, min(i + 7, n)):
            p = inStrip[i]
            q = inStrip[j]
            dist = distance(p,q)

            if dist < minDistance:
                minDistance = dist
                bestPair = (p,q)
    
    return minDistance, bestPair

def closestPairRecursive(pairX, pairY):
    n = len(pairX)
    if n <= 3:
        return bruteForce(pairX)
    
    mid = n//2
    Qx = pairX[:mid]
    Rx = pairX[mid:]
    midpoint = pairX[mid][0]

    Qy = []
    Ry = []

    for p in pairY:
        if p[0] <= midpoint:
            Qy.append(p)
        else:
            Ry.append(p)

    distLeft, pairLeft = closestPairRecursive(Qx, Qy)
    distRight, pairRight = closestPairRecursive(Rx, Ry)

    if distLeft < distRight:
        dist = distLeft
        bestPair = pairLeft
    else:
        dist = distRight
        bestPair = pairRight

    ds, splitPair  = closestSplitPair(pairX, pairY, dist, bestPair)

    if ds < dist:
        return ds, splitPair
    else:
        return dist, bestPair
    
def closestPair(points):
    pairX = sorted(points, key=lambda pair: pair[0])
    pairY = sorted(points, key=lambda pair: pair[1])

    return closestPairRecursive(pairX, pairY)

points = [(1,4), (8,5), (12,19), (30, 15), (5,1), (7,21)]
print("Points: ", points)
dist, pair = closestPair(points)
print("Closest Pair: ", pair)
print("Distance: ", dist)