def find_min_MNS(n,k):
    k = int(k)
    
    if len(n) <= k:
        return -1

    n = [int(x) for x in n]

    total_0 = None
    ninja_sums = []

    for head in range(len(n)-k+1):
        if not total_0:
            total_0 = sum(n[head: head + k])
            continue

        total_1 = total_0 - n[head-1] + n[head+k-1]
        ninja_sums.append(abs(total_0 - total_1))
        total_0 = total_1

    return min(ninja_sums)

for _ in range(int(input())):
    print(find_min_MNS(*input().split(" ")))