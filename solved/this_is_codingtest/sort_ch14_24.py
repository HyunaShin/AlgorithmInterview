n = int(input())
house_list = list(map(int ,input().split(" ")))

total_mile = sum(house_list)
mile_by_house = []
for house in house_list:
    distance = 0
    for neighbor in house_list:
        if  house == neighbor:
            continue
        else:
            distance += abs(house - neighbor)
    mile_by_house.append((house, distance))

mile_by_house.sort(key = lambda x: (int(x[1]), int(x[0])))
print(mile_by_house[0][0])