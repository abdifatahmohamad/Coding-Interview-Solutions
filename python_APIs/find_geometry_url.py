import requests
import json
import heapq

# Fetch data from the URL
response = requests.get("https://www.arcgis.com/sharing/rest/portals/self?f=json")
# Parse the JSON response
data = response.json()

# Extract the 'helperServices' object
obj = data.get("helperServices", {})
# print(obj)

# Filter the data
filtered_data = [
    {"name": key, "url": value["url"]}
    for key, value in obj.items()
    if "geocode" not in key and "defaultElevationLayers" not in key
]

# print(filtered_data)

# Use a heap to sort the data based on 'name'
heap = []
for item in filtered_data:
    heapq.heappush(heap, (item["name"], item))

sorted_data = []
while heap:
    sorted_data.append(heapq.heappop(heap)[1])

print(sorted_data)

# Use built-in function sort() to sort data by name:
# filtered_data.sort(key=lambda x: x["name"])

# Find the URL of the first entry that includes "geometry"
res = None
for entry in sorted_data:
    if "geometry" in entry["name"]:
        res = entry["url"]
        break

print(res)
