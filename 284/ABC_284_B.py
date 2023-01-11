t = int(input())

test = list([0]for i in range(t))
ith_test_case_length=0
count=[0 for i in range(t)]

for i in range(2*t):
    if (i+1)%2==0:
        ith_test_case = list(map(int,input().split()))
        for j in range(ith_test_case_length):
            if ith_test_case[j]%2==1:
                count[(i+1)//2-1]+=1
    else:
        ith_test_case_length = int(input())

for i in count:
    print(i)        