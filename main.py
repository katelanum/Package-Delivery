# Kate/Katherine Lanum
# Student Id:

import csv
from math import floor

from Package import Package
from PackageHashTable import PackageHashTable
from Truck import Truck


def populate_packages():
    # This function has a time complexity of O(n) where n is the number of rows/packages. This is due to the fact
    # that while iterating, the only actions are constant, so time grows linearly.
    # Space complexity of this function is O(n) where n is the number of rows/packages because for every package,
    # one package item is being created
    # Take in the package data and put that information in Package objects
    with open('ModifiedPackageFile.csv', 'r', encoding='utf-8-sig') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            package_id = row[0].strip()
            input_address = row[1]
            input_city = row[2]
            input_state = row[3]
            input_zip = row[4]
            input_deadline = row[5]
            input_mass = row[6]
            input_notes = row[7]
            temp_package = Package(package_id, input_address, input_city, input_state, input_zip, input_deadline,
                                   input_mass, input_notes)
            # Take package objects and populate HashTable
            package_table.insert(row[0], temp_package)


def package_check(id, minutes):
    # get package information from the hashtable and format the information for printing to console
    item = package_table.get(id)
    if item.delivery_time < minutes:
        status_hours = floor(item.delivery_time / 60)
        status_minutes = floor(item.delivery_time % 60)
        print("Package " + str(item.id) + " Delivery address: " + str(item.full_address) +
              " Delivery deadline: " + str(item.deadline) + " Package weight: " + str(item.mass) +
              " Status: Delivered at " + str(status_hours) + ":" + '{:0>2}'.format(status_minutes))
    elif item.on_truck_time < minutes:
        status_hours = floor(item.on_truck_time / 60)
        status_minutes = floor(item.on_truck_time % 60)
        print("Package " + str(item.id) + " Delivery address: " + str(item.full_address) +
              " Delivery deadline: " + str(item.deadline) + " Package weight: " + str(item.mass) +
              " Status: Loaded on truck at " + str(status_hours) + ":" +
              '{:0>2}'.format(status_minutes))
    else:
        print("Package " + str(item.id) + " Delivery address: " + str(item.full_address) +
              " Delivery deadline: " + str(item.deadline) + " Package weight: " + str(item.mass) +
              " Status: At hub")


# start running code
# The overall time complexity is O(n^3) where n is the number of packages. The largest time complexity is in the
# traversal of the truck's path. The creation and population of the package hash table is O(n). The creation of the
# distance matrix is also O(n). Loading the trucks are also O(n). The truck path traversal is O(n^3).
# Each portion of the output is also O(n). While there are many pieces, those are simply added to the time and since
# O(n^3) dwarfs the others, it's functionally determining time complexity itself.
# The overall space complexity is O(n^2) where n is the number of packages. Almost all components are O(n), but the
# distance matrix is O(n^2) due to needing to add to all existing rows and columns for each addition. None of the
# other components take up enough space to change the complexity from O(n^2)

# create and load package hashtable
package_table = PackageHashTable()
populate_packages()
package_count = 40

# Create adjacency list of addresses
address_count = 28
distance_array = [[""] * address_count] * address_count
row_count = 0
with open('ModifiedDistanceTable.csv', 'r') as file:
    file_reader = csv.reader(file)
    i = 0
    for row in file_reader:
        distance_array[i] = row
        i += 1

# input time that drivers start driving (8am)
driver_one_time = 8 * 60
driver_two_time = 8 * 60

# load truck 1 for trip 1
truck1 = Truck(1, distance_array, driver_one_time)
truck1.load_packages([package_table.get(14), package_table.get(15), package_table.get(16),
                      package_table.get(34), package_table.get(20), package_table.get(21), package_table.get(19),
                      package_table.get(13), package_table.get(39)])

# drive truck 1 for trip 1
truck1.path('HUB', address_count)
driver_one_time = truck1.get_time()

# load truck 2 for trip 1
truck2 = Truck(2, distance_array, driver_two_time)
truck2.load_packages([package_table.get(1), package_table.get(40), package_table.get(4), package_table.get(5),
                      package_table.get(37), package_table.get(38), package_table.get(3), package_table.get(36),
                      package_table.get(18)])

# drive truck 2 for trip 1
truck2.path('HUB', address_count)
driver_two_time = truck2.get_time()

# load truck 3 for trip 1
truck3 = Truck(3, distance_array, driver_two_time)
truck3.load_packages([package_table.get(25), package_table.get(26), package_table.get(31), package_table.get(32),
                      package_table.get(6)])

# drive truck 3 for trip 1
truck3.path('HUB', address_count)
driver_two_time = truck3.get_time()

# load truck 1 for trip 2
truck1 = Truck(1, distance_array, driver_one_time)
truck1.load_packages([package_table.get(7), package_table.get(29), package_table.get(8), package_table.get(9),
                      package_table.get(30)])

# drive truck 1 for trip 2
truck1.path('HUB', address_count)
driver_one_time = truck1.get_time()

# load truck 2 for trip 2
truck2 = Truck(2, distance_array, driver_two_time)
truck2.load_packages([package_table.get(24), package_table.get(22), package_table.get(2), package_table.get(33),
                      package_table.get(28), package_table.get(17), package_table.get(27), package_table.get(35),
                      package_table.get(10), package_table.get(12), package_table.get(23), package_table.get(11)])

# drive truck 2 for trip 2
truck2.path('HUB', address_count)
driver_two_time = truck2.get_time()

# get user input for time
time = int(input("Please type in time in military time format (i.e. 1300 for 1pm) and press enter "))
hours = time / 100
minutes = (hours * 60) + (time % 60)
confirmation_options = ["yes", "Y", "y", "Yes", "YES"]
rejection_options = ["no", "No", "NO", "n", "N"]

# handle summary information
summary_verification = str(input("Would you like a summary of all trucks and packages? "
                                 "Type yes or no and press enter "))
if summary_verification in confirmation_options:
    total_distance = truck1.distance + truck2.distance + truck3.distance
    print("Total distance traveled at end: " + str(int(total_distance)) + " miles")
    for i in range(1, 41):
        package_check(i, minutes)
elif summary_verification in rejection_options:

    # handle package information
    package_verification = str(input("Would you like the status of a package? "
                                         "Type yes or no and press enter "))
    if package_verification in confirmation_options:
        package_identification = str(input("Please put in a package id and press enter "))
        package_check(package_identification, minutes)
    elif package_table in rejection_options:
        print("No valid options selected")
    else:
        print("Input does not match with yes or no")
else:
    print("Input does not match with yes or no")




