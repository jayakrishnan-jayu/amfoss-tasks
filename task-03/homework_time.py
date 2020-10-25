def find_incredible_series(n, buffer):
    if len(buffer)>=n:
        return buffer[n-1]

    first, second, third = buffer[-3:]

    for i in range(n-len(buffer)):
        tmp_third = third
        
        third = (third + second + first) % (10**9 + 7)
        buffer.append(third)
        first = second
        second = tmp_third

    return third
    

data = []
buffer = [1,2,3]
for i in range(int(input())):

    num = find_incredible_series(int(input()) , buffer)
    reverse = 0
    
    while num > 0:
        reverse = num % 10 + reverse * 10
        num//=10

    data.append(reverse)
for i in data:
    print(i)