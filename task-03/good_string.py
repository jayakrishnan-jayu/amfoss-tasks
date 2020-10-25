def has_same(s):
    zeros = 0
    ones = 0
    for i in s:
        if i=="0":
            zeros+=1
        elif i=="1":
            ones+=1
    return zeros == ones

input()
s = input()



if (s=="0" or s=="1") or ("0" in s and "1" not in s) or ("1" in s and "0" not in s) or not has_same(s):
    print(1)
else :
        
    print(2)