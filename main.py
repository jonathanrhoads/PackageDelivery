from distances import shortest_path
from graph import Graph, Vertex
from import_data import package_table, route_map
from truck import Truck


def is_during_business_hours(self, hour, minute):
    if (self <= 8 and minute <= 0) or (self > 21 and minute > 0):
        return False
    else:
        return True


def deliver_packages(truck, route, hour, minute):

    package_route = ['4001 South 700 East']
    stops = list(route.adjacency_list.keys)

    while stops not in package_route:
        package_route.append(shortest_path(stops, package_route[len(package_route - 1)]))

    for i in range(1, len(package_route)):
        truck.distance_travelled += route_map.edge_weights[(package_route[i - 1], package_route[i])]

    for pId in truck.packages:
        package = package_table[pId]

        # Finds where package is at during a specific time

        package.set_status()
        package.set_time(truck.st)


    for i in range(1, 41):
        print(package_table.search(i))

    # truck_list = truck1_packages + truck2_packages + truck3_packages
    # truck_list.sort()
    #
    # for i in truck_list:
    #     print(f'{i}')


class Main:

    truck1_packages = [1, 13, 14, 15, 16, 19, 20, 7, 29, 8, 30, 31, 34, 37, 39, 40]  # 16 Packages
    truck2_packages = [3, 18, 36, 38, 2, 4, 5, 10, 11, 12, 17, 21, 22, 23, 24, 26]  # 16 packages
    truck3_packages = [6, 25, 28, 32, 9, 27, 33, 35]  # 8 packages
    truck1 = Truck(truck1_packages, '08:00')
    truck2 = Truck(truck2_packages, '08:00')
    truck3 = Truck(truck3_packages, '10:20')

    route1 = Graph()
    route2 = Graph()
    route3 = Graph()

    for p in truck1.packages:
        route1.add_vertex(Vertex(p))
    for p in truck2.packages:
        route2.add_vertex(Vertex(p))
    for p in truck3.packages:
        route3.add_vertex(Vertex(p))

    distance = truck1.distance_travelled + truck2.distance_travelled + truck3.distance_travelled

    print(f'''
    Author: Jonathan Rhoads 
    #001891548
    --------------------------------------------------------------------------------------------------------------------
    
                                            WELCOME TO THE PACKAGE DELIVERY HUB
                                            
                                                    Total distance: {distance}
                                            
                                            Hours of Operation: 8:00 AM - 9:00 PM
                                            
                                                How can we help you today?
                                                
    --------------------------------------------------------------------------------------------------------------------
    Please enter a number from the options below:
        1. Lookup all packages at a certain time.
        2. Exit the hub.
    ''')

    selection = input()

    if selection == '2':
        print('Thank you and have a nice day!')
        exit()
    elif selection == '1':
        while selection == '1':
            time = input('\nPlease enter the time desired in the format HH:MM\n')
            (hour, minute) = time.split(':')

            if is_during_business_hours(hour, minute):
                print(f'Displaying package details at {hour}:{minute}')
                deliver_packages(truck1, route1, hour, minute)
                deliver_packages(truck2, route2, hour, minute)
                deliver_packages(truck3, route3, hour, minute)

            selection = input('Enter 1 to lookup another time or press any key to exit.')
            if selection != '1':
                print('Thank you and have a nice day!')
                exit()
    else:
        print('Invalid input, bye bye!')




