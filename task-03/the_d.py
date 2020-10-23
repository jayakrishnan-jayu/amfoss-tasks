n = int(input())
if n == 1:
    print("D")
elif n > 1:
    for i in range(1,n+1):
        for j in range(1,n+1):
            mid = (n//2)+1
            if i < mid:
                length = mid-i
                print("*" * length + "D" * (n- length*2) + "*" * length)
                break
            elif i == mid:
                print("D" * n)
                break
            else:
                
                length = i-mid
                print("*" * length + "D" * (n- length*2) + "*" * length)
                break
