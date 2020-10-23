for _ in range(int(input())):
    [infinity_stones, _ , max_boxes] = [int(x) for x in input().split(" ")]
    foo = input()
    
    max_stones_per_box = [int(x) for x in input().split(" ")]
    protectable_stones = 0
    
    for _ in range(max_boxes):
        if len(max_stones_per_box) > 0:
            temp = max(max_stones_per_box)
            protectable_stones += temp
            max_stones_per_box.remove(temp)
            
    if protectable_stones >= infinity_stones:
        print("YES")
    else:
        print("NO")
