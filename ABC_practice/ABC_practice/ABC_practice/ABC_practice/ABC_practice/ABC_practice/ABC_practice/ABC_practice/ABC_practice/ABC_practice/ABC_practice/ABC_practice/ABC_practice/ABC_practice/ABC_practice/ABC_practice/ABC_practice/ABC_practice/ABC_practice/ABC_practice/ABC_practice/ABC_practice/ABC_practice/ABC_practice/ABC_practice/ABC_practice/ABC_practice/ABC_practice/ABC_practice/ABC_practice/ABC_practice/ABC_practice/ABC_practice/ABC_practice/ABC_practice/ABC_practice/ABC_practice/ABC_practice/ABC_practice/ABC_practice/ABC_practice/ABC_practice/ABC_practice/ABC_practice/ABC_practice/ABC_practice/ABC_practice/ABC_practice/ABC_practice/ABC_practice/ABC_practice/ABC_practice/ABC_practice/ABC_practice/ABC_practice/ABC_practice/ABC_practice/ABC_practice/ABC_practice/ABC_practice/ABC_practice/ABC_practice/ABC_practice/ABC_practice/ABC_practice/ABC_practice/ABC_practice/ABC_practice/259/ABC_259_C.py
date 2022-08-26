from itertools import groupby
import sys

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def rungLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k,v in grouped:
        res.append((k,int(len(list(v)))))
    return res

def rungLengthDecode(L: "list[tuple]"):
    res = ""
    for c,n in L:
        res += c * int(n)
    return res

def rungLengthEncodeToString(S: str):
    grouped = groupby(S)
    res = ""
    for k,v in grouped:
        res += k + str(len(list(v)))
    return res

def main():
    S = str(input())

    T = str(input())

    rung_S = rungLengthEncode(S)

    rung_T = rungLengthEncode(T)

    if len(rung_T) != len(rung_S):
        print("No")
        sys.exit()
        
    for i in range(len(rung_T)):
        if rung_S[i][0] != rung_T[i][0]:
            print("No")
            sys.exit()
        elif rung_S[i][1] == 1 and rung_T[i][1] >= 2:
            print("No")
            sys.exit()
        elif rung_S[i][1] > rung_T[i][1]:
            print("No")
            sys.exit()
    print("Yes")
            

if __name__ == "__main__":
    main()