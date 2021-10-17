import csv
from datetime import datetime
from graph import Graph, Vertex
from hash_table import HashTable
from package import Package

with open('WGUPS Distance Table.csv') as distances:
    line = csv.reader(distances, delimiter=',')
    address_list = next(line)  # Creates a list of the addresses to be used as the end points of edges
    route_map = Graph()

    for address in line:
        # Uses the address column to add a vertex
        route_map.add_vertex(Vertex(address[0]))
        # Adds the addresses in left column as a key with an empty list as the value.
        route_map.add_vertex(address[0])

        for distance in range(len(address))[1:]:
            # Adds the address in the first row as a key with an empty list as the value.
            route_map.add_vertex(address_list[distance])
            # Pulls point A from the line of CSV, point B from first row, and weight from where the two addresses meet
            route_map.add_undirected_edge(address[0], address_list[distance], float(address[distance]))

with open('WGUPS Package File.csv') as packages:
    package = csv.reader(packages, delimiter=',')
    next(package)

    package_table = HashTable(40)

    for p in package:
        pId = int(p[0])
        pAddress = p[1]
        pCity = p[2]
        pState = p[3]
        pZip = p[4]

        if 'EOD' in p[5]:
            pDeadline = datetime.now().replace(hour=21, minute=0)
        else:
            time = p[5].replace(' ', ':').split(':')
            pDeadline = datetime.now().replace(hour=int(time[0]), minute=int(time[1])) if 'AM' in time \
                else datetime.now().replace(hour=int(time[0]) + 12, minute=int(time[1]))

        pWeight = p[6]
        pNotes = p[7]
        pStatus = 'at the hub'
        pTime = datetime.now().replace(hour=8, minute=0)

        if 'Delayed' in pNotes:
            status = 'Delayed'
            time = datetime.now().replace(hour=9, minute=5)

        if pId == 9:
            pAddress = '410 S State St'
            pCity = 'Salt Lake City'
            pState = 'UT'
            pZip = '84111'

        new_package = Package(pId, pAddress, pCity, pState, pZip,
                              pDeadline, pWeight, pNotes, pStatus, pTime)
        package_table.insert(pId, new_package)
