length = int(input())
requirement = list(map(lambda x: int(x), input().split(" ")))
data = list(map(lambda x: int(x), input().split(" ")))

least_pages = data[0] // requirement[0] 
for index in range(1, length):
    num_pages = data[index] // requirement[index]
    if least_pages > num_pages:
        least_pages = num_pages
print(least_pages)
