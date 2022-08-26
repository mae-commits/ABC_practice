from typing import Sequence

import itertools

N, M = map(int,input().split())

Seq = list(i for i in range(1,M+1))

Seq_re = list(itertools.combinations(Seq,N))

for i in range(len(Seq_re)):
    print(*Seq_re[i])
    
