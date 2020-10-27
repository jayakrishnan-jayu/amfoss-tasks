#!/bin/python3

import sys

# sum of n terms of aritmetic process is n/2(2a+(n-1)d)

t = int(input().strip())
for a0 in range(t):
    k = int(input().strip())-1
    
    total = 0
    if k>=3:
        
        for i in [3,5,15]:
            end = k - k % i
            n = end//i
            if i==15:
                total -= (n*(2*i + (n-1) * i)) >> 1
                continue
            total += (n*(2*i + (n-1) * i)) >> 1
    print(int(total))
