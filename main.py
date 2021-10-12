from graph import Graph, Vertex
from import_data import package_table
from truck import Truck


class Main:

    truck1_packages = [1, 13, 14, 15, 16, 19, 20, 7, 29, 8, 30, 31, 34, 37, 39, 40]  # 16 Packages
    truck2_packages = [3, 18, 36, 38, 2, 4, 5, 10, 11, 12, 17, 21, 22, 23, 24, 26]  # 16 packages
    truck3_packages = [6, 25, 28, 32, 9, 27, 33, 35]  # 8 packages
    truck1 = Truck(truck1_packages)
    truck2 = Truck(truck2_packages)
    truck3 = Truck(truck3_packages)

    route1 = Graph()
    route2 = Graph()
    route3 = Graph()

    for p in truck1.packages:
        route1.add_vertex(Vertex(p))
    for p in truck2.packages:
        route2.add_vertex(Vertex(p))
    for p in truck3.packages:
        route3.add_vertex(Vertex(p))

    # truck_list = truck1_packages + truck2_packages + truck3_packages
    # truck_list.sort()
    #
    # for i in truck_list:
    #     print(f'{i}')

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
            print(f'hour: {hour} minute: {minute}')
            for i in range(1, 41):
                print(package_table.search(i))
            selection = input('Enter 1 to lookup another time or press any key to exit.')
            if selection != '1':
                print('Thank you and have a nice day!')
                exit()
    else:
        print('Invalid input, bye bye!')


