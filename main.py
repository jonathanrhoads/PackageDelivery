from distances import deliver_packages
from graph import Graph, Vertex
from import_data import package_table, route_map
from truck import Truck


def print_packages():
    '''
    Iterates through all packages then prints them to console in the format prescribed by package class.
    '''
    for i in range(1, 41):
        print(package_table.search(i))


class Main:

    #  Manually loads all truck packages. The first two trucks out will be fully loaded and have all packages
    #  that need to be delivered by 10:30 AM. Trucks objects are instantiated with their packages and the time they
    #  depart the hub.
    truck1_packages = [1, 13, 14, 15, 16, 19, 20, 7, 29, 8, 30, 31, 34, 37, 39, 40]  # 16 Packages
    truck2_packages = [3, 18, 36, 38, 2, 4, 5, 10, 11, 12, 17, 21, 22, 23, 24, 6]  # 16 packages
    truck3_packages = [25, 28, 32, 9, 27, 33, 35, 26]  # 8 packages
    truck1 = Truck(truck1_packages, '08:00')
    truck2 = Truck(truck2_packages, '09:05')
    truck3 = Truck(truck3_packages, '10:20')

    #  Creates routes for each truck that is a graph object holding the addresses where the packages need to be
    #  delivered.
    route1 = Graph()
    route2 = Graph()
    route3 = Graph()

    for p in truck1.packages:
        route1.add_vertex(Vertex(p))
    for p in truck2.packages:
        route2.add_vertex(Vertex(p))
    for p in truck3.packages:
        route3.add_vertex(Vertex(p))

    print(f'''
    Author: Jonathan Rhoads 
    #001891548
    --------------------------------------------------------------------------------------------------------------------
    
                                            WELCOME TO THE PACKAGE DELIVERY HUB
       
                                            Hours of Operation: 8:00 AM - 9:00 PM
                                            
                                                How can we help you today?
                                                
    --------------------------------------------------------------------------------------------------------------------
    Please enter a number from the options below:
        1. Lookup all packages at a certain time.
        2. Exit the hub.    ''')

    selection = input()

    if selection == '2':
        print('Thank you and have a nice day!')
        exit()
    elif selection == '1':
        while selection == '1':
            time = input('\nPlease enter the time desired in the format HH:MM (Use military time i.e. 13:00 for 1 PM)')
            (hour, minute) = [int(i) for i in time.split(':')]

            #  Delivers the packages
            deliver_packages(truck1, route1, hour, minute)
            if hour > 9 or (hour == 9 and minute >= 5):
                deliver_packages(truck2, route2, hour, minute)
            if hour > 10 or (hour == 10 and minute >= 20):
                deliver_packages(truck3, route3, hour, minute)

            print(f'Displaying package details at {hour}:{minute}')
            print_packages()
            mileage = truck1.distance_travelled + truck2.distance_travelled + truck3.distance_travelled
            print(f'\nCurrent total mileage for all trucks is {round(mileage, 2)}')

            selection = input('\n\nEnter any key to exit.')
            print('Thank you and have a nice day!')
            exit()
    else:
        print('Invalid input, bye!')




