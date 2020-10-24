m = int(input().split(" ")[1])
arr = list(dict.fromkeys([int(x) for x in input().split(" ")]))
arr.sort()

has_pair = False
head_index = 0
tail_index = len(arr)-1

while head_index != tail_index:
    sum_of_pair = arr[head_index] + arr[tail_index]
    if sum_of_pair == m:
        has_pair = True
        break
    elif sum_of_pair < m:
        head_index += 1
    else:
        tail_index-=1

print(str(has_pair))