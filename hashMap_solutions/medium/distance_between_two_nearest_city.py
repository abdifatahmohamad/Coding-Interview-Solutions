import sys
import heapq

data = []
# O(n)
for line in sys.stdin:
    data = [x.strip() for x in line.split(';')]

cities = {}
# O(n)
for d in data: 
    if d != '':
        city, distance = d.split(',')[0], d.split(',')[1]
        cities[city] = int(distance)

heap = []
# O(NlogN)
for city in cities: 
    heapq.heappush(heap, cities.get(city))

prev_distance = heapq.heappop(heap)
result = [prev_distance]
while heap:
    curr_distance = heapq.heappop(heap)
    total_distance = curr_distance - prev_distance
    result.append(total_distance)
    prev_distance = curr_distance

print(result)
    
'''
# line = 'Vgdfz,70; Mgknxpi,3958; Nsptghk,2626; Wuzp,2559; Jcdwi,3761;'
# Output: 70,2489,67,1135,197

line = 'Rkbs,5453; Wdqiz,1245; Rwds,3890; Ujma,5589; Tbzmo,1303;'
# Output: 1245,58,2587,1563,136


['seattle,5453; louisville,1245; fargo,3890; portland,5589; miami,1303;']
1245,58,2587,1563,136

- starting point to the nearest city [done] 
louisville1245

- distance between two nearest cities [done]
miami1303 - louis1245 = abs(58)
miami1303 - fargo3890 = abs(2587)
fargo3890 - seattle5453 = abs(1563)
seaatle5453 - portland5589 = abs(136)



[1,5,7,1,8,9,5]
'''