def main():
    N,Q = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    for i in range(Q):
        x = int(input())
        ok,ng = N, -1 # ok = the number of students who are taller than x, ng = that of thise who are smaller than x.
        while ok - ng > 1: # binary search
            md = (ok+ ng) // 2 
            if A[md] >= x: # if A[md] >= x, input md into ok because x is smaller than at least A[md]
                ok = md
            else:
                ng = md
        print(N-ok)


if __name__ == "__main__":
    main()