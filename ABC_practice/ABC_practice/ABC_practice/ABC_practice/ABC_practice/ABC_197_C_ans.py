# Input integers.
N = int(input())

A = list(map(int,input().split()))

# Confirm the range, and calculate OR for elements in the range.
def calc_or(left,right):
    result = 0
    # Calculate OR in the same group.
    for i in range(left, right):
        result = result | A[i]
    return result

# Define answer.
ans = 2 ** 40

# Start the all search way.
for i in range(1<<(N+1)):
    # If the right or left side of partitions do not exist, skip to the next pattern.
    if i & 1 == 0 or i >> N & 1 == 0:
        continue
    # Confirm where partitions are.
    partitions = []
    
    for shift in range(N+1):
        # If the "shift" th digit has partitions, add the number "shift" into the list pertitions.
        if i >> shift & 1 == 1:
            partitions.append(shift)
    # Define ans_tmp as the variable to memorize the result temporary.
    ans_tmp = 0
    for j in range(len(partitions)-1):
        ans_tmp = ans_tmp ^ calc_or(partitions[j], partitions[j+1])
    ans = min(ans, ans_tmp)
    
print(ans)