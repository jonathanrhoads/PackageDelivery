import csv
from datetime import datetime
from hash_table import HashTable
from package import Package

# with open('WGUPS Distance Table.csv') as distances:

with open('WGUPS Package File.csv') as packages:
    package = csv.reader(packages, delimiter=',')
    next(package)

    for p in package:
        package_id = int(p[0])
        address = p[1]
        city = p[2]
        state = p[3]
        zip_code = p[4]
        deadline = p[5]
        weight = p[6]
        notes = p[7]
        status = 'at the hub'
        time = datetime.now().replace(hour=8, minute=0)

        if 'Delayed' in notes:
            status = 'Delayed'
            time = datetime.now().replace(hour=9, minute=5)
