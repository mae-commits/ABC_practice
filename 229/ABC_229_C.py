n,w = map(int,input().split())

pizza = list(list(map(int,input().split())) for i in range(n))

#Sort the deliciousness of cheese in upper order
pizza.sort(reverse=True)

#Total weight of cheese
weight = 0

kind = 0

totalDeliciousness = 0

while weight < w and kind < n:
    totalDeliciousness += pizza[kind][0] * min(w-weight,pizza[kind][1])
    weight += min(w-weight,pizza[kind][1])
    kind += 1

print(totalDeliciousness)    