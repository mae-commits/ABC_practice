N, M = map(int, input().split())

lines = list(list(map(int ,input().split())) for i in range(M))

# 番号i の人間が隣に並んだ人の番号をカウント
neighbor_num = [set([i]) for i in range(N+1)]

for line in lines:
    for i in range(N):
        if i == 0:
            neighbor_num[line[i]].add(line[i+1])
        elif i == N-1:
            neighbor_num[line[i]].add(line[i-1])
        else:
            neighbor_num[line[i]].add(line[i+1])
            neighbor_num[line[i]].add(line[i-1])
            
not_good_relation_list = set()
num_list = set([i+1 for i in range(N)])

for i in range(1, N+1):
    not_good_relation_with_i = num_list - neighbor_num[i]    
    couple = set()
    not_good_relation_with_i = list(not_good_relation_with_i)
    for j in range(len(not_good_relation_with_i)):
        couple |= set([str(min(not_good_relation_with_i[j], i)) + str(max(not_good_relation_with_i[j], i))])
    not_good_relation_list |= couple

print(len(not_good_relation_list))