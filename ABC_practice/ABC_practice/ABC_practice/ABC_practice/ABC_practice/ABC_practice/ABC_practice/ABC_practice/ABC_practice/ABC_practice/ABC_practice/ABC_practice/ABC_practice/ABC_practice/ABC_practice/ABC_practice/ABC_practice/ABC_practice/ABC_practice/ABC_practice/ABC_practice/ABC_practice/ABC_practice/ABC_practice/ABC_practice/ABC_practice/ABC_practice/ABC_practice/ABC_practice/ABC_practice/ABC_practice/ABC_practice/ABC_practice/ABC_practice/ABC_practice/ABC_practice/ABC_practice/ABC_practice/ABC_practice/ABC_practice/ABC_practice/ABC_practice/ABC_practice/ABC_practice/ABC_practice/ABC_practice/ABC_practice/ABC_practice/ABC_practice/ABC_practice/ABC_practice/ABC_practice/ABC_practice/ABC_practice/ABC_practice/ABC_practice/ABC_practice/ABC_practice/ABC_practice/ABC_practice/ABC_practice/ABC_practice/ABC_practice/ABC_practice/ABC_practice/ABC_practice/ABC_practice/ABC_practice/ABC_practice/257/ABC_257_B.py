def main():
    N,K,Q = map(int,input().split())
    A = list(map(int,input().split())) # indices of komas initially
    L = list(map(int,input().split())) # the number of komas which change the indices from left to right when the condition is content. 
    for i in range(len(L)):
        if A[L[i]-1] != N and ((A[L[i]-1] + 1) not in A):
            A[L[i]-1] += 1
    print(*A)        
            

if __name__ == "__main__":
    main()