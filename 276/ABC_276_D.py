n = int(input())

a = sorted(list(map(int,input().split())))

def two_divisor(n):
    i = 0
    while n%2 == 0:
        i+=1
        n = n//2
    return i, n

def three_divisor(n):
    j = 0
    while n%3 == 0:
        j+=1
        n = n//3
    return j, n

new_a = []
divised_numbers = set()
min_power_of_two = 10**9
min_power_of_three = 10**9
total_sum = 0

for i in range(len(a)):
    power_of_two, divised_two = two_divisor(a[i])
    # print(divised_two)
    # print(power_of_two)
    power_of_three, divised_three = three_divisor(divised_two)
    # print(divised_three)
    min_power_of_two = min(min_power_of_two, power_of_two)
    min_power_of_three = min(min_power_of_three, power_of_three)
    total_sum += (power_of_two + power_of_three)
    divised_numbers.add(divised_three)

if len(divised_numbers) != 1:
    print(-1)
else:
    total_sum -= (min_power_of_two + min_power_of_three) * n
    print(total_sum)