mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

print("First destination:", mission_route[0])

print("Last destination:", mission_route[-1])

print("Total destinations:", len(mission_route))

print("Mission Route:")
for destination in mission_route:
    print(destination)

if "Europa" in mission_route:
    print("Europa is included in the mission route")
else:
    print("Europa is not included in the mission route")
