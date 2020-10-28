length = int(input().split(" ")[0])

owners = input().split()
orders = input().split()

owners_dict = {}
for i in range(len(owners)):
    owner = owners[i]
    if owner in owners_dict:
        owners_dict[owner].append(i)
    else:
        owners_dict[owner] = [i]

output = ""
for order in orders:
    if order in owners_dict:
        
        if(len(owners_dict[order]) > 0):
            output += str(owners_dict[order].pop(-1) + 1) + " "
            owners_dict[order]
        else:
            output += "-1 "

print(output)