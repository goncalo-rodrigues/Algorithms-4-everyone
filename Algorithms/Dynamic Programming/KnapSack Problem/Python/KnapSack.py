# This solves the knapsack 0-1 problem
def knapsack(v, w, W):
    n = len(v)
    # m[i, w] represents the max value you can get with the first i items using a max of w capacity
    m = []
    # initalize matrix m
    for i in range(n+1):
        m.append([[]] * (W+1))
    # start with 0 when using 0 items
    for j in range(W+1):
        m[0][j] = 0

    for i in range(1,n+1):
        for j in range(W+1):
            # if can't fit new object, just use the optimal solution without that object
            if w[i-1] > j:
                 m[i][j] = m[i-1][j]
            # else, choose the max between not using the object or 
            # optimal solution for all items but new one such that new object fits + the new object's value
            else:
                 m[i][j] = max(m[i-1][j], m[i-1][j-w[i-1]] + v[i-1])
    return m[n][W]

print(knapsack([1, 2, 3, 4], [2, 3, 5, 1], 6))
