def find_cycle(graph, start):
    stack = [start]
    visited = [False] * (len(graph) + 1)
    while stack:
        current = stack[-1]
        if visited[current]:
            return stack[stack.index(current):]
        visited[current] = True
        next_node = graph[current]
        stack.append(next_node)
    return None

def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))  # 0番目の要素は無視するため0を追加

    cycle = find_cycle(A, 1)  # 頂点1をスタートとして有向閉路を探索

    if cycle:
        M = len(cycle)
        print(M-1)
        print(*cycle[0:-1])
    else:
        print("No cycle found.")

if __name__ == "__main__":
    main()
