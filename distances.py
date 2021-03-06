from datetime import datetime, timedelta
from import_data import route_map, package_table



def shortest_path(package_list, start):
    '''
    Searches the remaining stops to make and returns the closest one.
    O(n)
    :param package_list:
    :param start:
    :return:
    '''
    packages = package_list[:]
    closest = packages[0]
    distances = route_map.edge_weights
    check_distance = distances[(start, closest)]

    for address in packages:
        if start == address:
            continue

        distance = distances[(start, address)]
        if distance < check_distance:
            check_distance = distance
            closest = address

    package_list.remove(closest)
    return closest



def deliver_packages(truck, route, hour, minute):
    """
    Delivers all packages while recording the distance travelled and updating the times and statuses of packages.
    O(n^2)
    :param truck:
    :param route:
    :param hour:
    :param minute:
    :return:
    """
    # Set the truck's package's status to en route
    for pId in truck.packages:
        package = package_table.search(pId)
        package.set_status('en route')

    package_route = ['4001 South 700 East']

    stops = []
    stops_vertex_list = route.adjacency_list.keys()
    for stop in stops_vertex_list:
        package = package_table.search(stop.label)
        stops.append(package.address)
    stops = list(set(stops))

    truck_start = truck.start_time.split(':')
    start_time = datetime(2021, 1, 1, int(truck_start[0]), int(truck_start[1]))
    stop_time = start_time

    while len(stops) > 0:
        closest_stop = shortest_path(stops, package_route[-1])
        package_route.append(closest_stop)
    package_route.append('4001 South 700 East')

    for i in range(1, len(package_route)):
        current_stop = package_route[i]
        truck.distance_travelled += route_map.edge_weights[(package_route[i - 1], current_stop)]
        truck.distance_travelled = round(truck.distance_travelled, 2)

        time_travelled = timedelta(minutes=(truck.distance_travelled / truck.speed) * 60)
        stop_time = start_time + time_travelled

        if stop_time > datetime(2021, 1, 1, int(hour), int(minute)):
            return

        for pId in truck.packages:
            package = package_table.search(pId)
            if package.address == current_stop:
                package.set_status('Delivered')

                package.set_time(stop_time)