



#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a): 
    n = len(a) 
    i = 1 
    pri = 0 
    sec = 0 
    x = 0 
    y = 0 
    z = len(a)-1 
    while i <= n: 
        pri = pri + a[x][y] 
        sec = sec + a[x][z] 
        x += 1 
        y += 1 
        i += 1 
        z -= 1 
    diff = pri - sec
    return abs(diff) 
