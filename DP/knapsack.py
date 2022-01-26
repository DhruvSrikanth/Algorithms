# Time complexity is O(2^n) so we use dp to reduce to linear time O(n*W)
# NP Complete Problem - Problems that have no solution in polynomial time

# Problem: 0-1 Knapsack problem
# Restriction: The weights and weight limit are positive integers
# Result: Algorithm can be made to run in polynomial time instead of exponential
# Reason: Each position in our table can be an instance of the knapsack problem with different input which can be indexed by w (only possible when weights w are integers meaning W is also an integer)

def knapsack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
  
    # Build table K[][] in bottom up manner
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
  
    return K[n][W]
  
# Driver program to test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(W, wt, val, n))
