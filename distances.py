from import_data import route_map, package_table


def shortest_path(package_list, start):
    packages = []

    for p in package_list:
        package = package_table.search(p)
        if package[1] not in packages:
            packages.append(package)

    current = start
    closest = packages[0]
    distances = route_map.edge_weights
    check_distance = distances[(current, closest)]

    while len(packages) > 1:
        for address in packages:
            distance = distances[(current, address)]

            if current == address:
                packages.clear()
                return current

            if check_distance <= distance:
                packages.remove(address)

            if check_distance > distance:
                check_distance = distance
                closest = address
                packages.remove(closest)
    return closest

# Dijkstra's
# def shortest_path(truck_list, start):
#     unvisited_stops = []
#
#     for address in route_map.adjacency_list:
#         unvisited_stops.append(address)
#
#     start.distance = 0
#
#     while len(unvisited_stops) > 0:
#
#         closest_idx = 0
#         for i in range(1, len(unvisited_stops)):
#
#             if unvisited_stops[i].distance < unvisited_stops[closest_idx].distance:
#                 closest_idx = i
#
#         current_location = unvisited_stops.pop(closest_idx)
#
#         for adj_stop in route_map.adjacency_list[current_location]:
#             edge_weight = route_map.edge_weights[(current_location, adj_stop)]
#             alternative_path_distance = current_location.distance + edge_weight
#
#             if alternative_path_distance < adj_stop.distance:
#                 adj_stop.distance = alternative_path_distance
#                 adj_stop.pred_vertex = current_location
#
#
# def get_shortest_route(package_list, start_vertex, end_vertex):
#     path = []
#     current_stop = end_vertex
#     while current_stop is not start_vertex:
#         package_list.adjacency_list
