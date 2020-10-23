for _ in range(int(input())):
    
    k = int(input().split(" ")[1])
    
    bags = [int(x) for x in input().split(" ") if len(x)>0]
    
    largest_bag_index = bags.index(max(bags))
    bags[largest_bag_index] -= k
    total = 1
    for price in bags:
        total *= price
    
    print(total)
    
