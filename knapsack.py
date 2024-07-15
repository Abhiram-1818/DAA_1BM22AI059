def unboundedKnapsack(k, arr):
    n = len(arr)
    dp = [0] * (k + 1)
    
    for x in arr:
        for j in range(x, k + 1):
            dp[j] = max(dp[j], dp[j - x] + x)
    
    return dp[k]

# Reading input and processing each test case
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        arr = list(map(int, data[index + 2:index + 2 + n]))
        index += 2 + n
        
        # Calculate the result for this test case
        result = unboundedKnapsack(k, arr)
        results.append(result)
    
    # Print all results
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
