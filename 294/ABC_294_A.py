N = int(input())

sequence_A = list(map(int,input().split()))

even_squences = []

for num in sequence_A:
    if num%2 == 0:
        even_squences.append(num)
        
print(*even_squences)