import sys
import math

lon = math.radians(float(input().replace(",",".")))
lat = math.radians(float(input().replace(",",".")))
n = int(input())

print("User: ",lat,lon,file=sys.stderr)

closest = 10000.0
defib = ""

for i in range(n):
    defibdata = input()
    fields = defibdata.split(";")
    # convert comma to period
    defiblat = math.radians(float(fields[5].replace(",",".")))
    defiblon = math.radians(float(fields[4].replace(",",".")))
    # formula presented had accuracy issues, replaced with haversine
    a = math.sin((defiblat-lat)/2)**2 + (math.cos(lat) * math.cos(defiblat) * math.sin((defiblon-lon)/2)**2)
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    distance = 6371 * c

    print("Defib: ",distance,fields[1],file=sys.stderr)
    # test for closest yet
    if closest>distance :
        closest=distance
        defib = fields[1]
    print("Closest: ",closest,defib,file=sys.stderr)
print(defib)
