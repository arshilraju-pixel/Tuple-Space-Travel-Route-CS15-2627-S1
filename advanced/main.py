mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

# first destination
print("first destination:", mission_route[0])

# last destination
print("last destination:", mission_route[-1])

# total number of destinations
print("total destinations:", len(mission_route))

# destinations in order
print("mission Route:")
for destination in mission_route:
    print(destination)

# check whether Europa is included in the route
if "Europa" in mission_route:
    print("Europa is included in the mission route")
else:
    print("Europa is not included in the mission route")

search_destination = input("Enter a destination you want to search: ")

if search_destination in mission_route:

    print(f"{search_destination} is part of the mission route.")


    destination_index = mission_route.index(search_destination)


    stops_from_start = destination_index


    stops_from_end = len(mission_route) - 1 - destination_index

    print("Stops from start:", stops_from_start)
    print("Stops from end:", stops_from_end)

    if destination_index < len(mission_route) - 1:
        next_stop = mission_route[destination_index + 1]
        print("next stop:", next_stop)

    else:
        print("This will be the final stop of the journey.")


else:
    print(f"{search_destination} is not part of the mission route")