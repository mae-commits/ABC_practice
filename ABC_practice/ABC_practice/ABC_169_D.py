# Define the function of integer factorization.
def prime_factorize(N):
    # If the argument is equal to 1, return 1.
    if N == 1:
        return [1]
    # Otherwise, define the list of simple divisors of N.
    prime_list = []
    # Start from the first principal divisor 2.
    i = 2
    # The maximum divisors of N is no more than the square root of N.
    while i * i <= N:
        # If i can divise N,
        if N%i == 0:
            # Append i as the pricipal divisor of N.
            prime_list.append(i)
            N //= i
        # Otherwise, add 1 to i.
        else:
            i += 1
    # If the rest is not equal to 1, add it as the principal divisor.
    if N != 1:
        prime_list.append(N)
    return prime_list

# Input N from the command line.
N = int(input())

prime_list = prime_factorize(N)

prime_list.sort()

ans = 0

# Cinfirm the kind of divisors of N.
prime_N = set(prime_list)

if N == 1:
    print(0)
else:
    for p in prime_N:
        for e in range(1,10**10):
            if N%(p**e) == 0:
                ans += 1
                N //= (p**e)
            else:
                break
    print(ans)

            