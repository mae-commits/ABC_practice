N = int(input())

flavors_plain = [[] for i in range(N+1)]

for i in range(N):
    F, S = map(int, input().split())
    flavors_plain[F].append(S)

flavor_sum = [0 for i in range(N+1)]
flavor_max = [0 for i in range(N+1)]

flavors = [sorted(ice) for ice in flavors_plain]

for i in range(1, N+1):
    ice_i = flavors[i]
    first_i, second_i = 0, 0
    if len(ice_i) >= 2:
        first_i, second_i = ice_i[-1], ice_i[-2]
        flavor_sum[i] = first_i+second_i//2
        flavor_max[i] = first_i
    elif len(ice_i) == 1:
        first_i = ice_i[0]
        flavor_max[i] = first_i
        
flavor_max = sorted(flavor_max, reverse=True)
flavor_sum = sorted(flavor_sum, reverse=True)

print(max(flavor_sum[0], flavor_max[0] + flavor_max[1]))