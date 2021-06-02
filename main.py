# Kate/Katherine Lanum
# Student Id:

import csv


from Package import Package
from PackageHashTable import PackageHashTable

def main():
    packageTable = PackageHashTable()

    # Take in the package data and put that information in Package objects
    with open('ModifiedPackageFile.csv', 'r') as file:
        fileReader = csv.reader(file)
        for row in fileReader:
            id = row[0]
            inputAddress = row[1]
            inputCity = row[2]
            inputState = row[3]
            inputZip = row[4]
            inputDeadline = row[5]
            inputMass = row[6]
            inputNotes = row[7]
            tempPackage = Package(id, inputAddress, inputCity, inputState, inputZip, inputDeadline, inputMass, inputNotes)

            # Take package objects and populate HashTable
            packageTable.insert(row[0], tempPackage)

    # Create adjacency list of addresses
    addressCount = 27
    distanceArray = [[None]*addressCount]*addressCount
    rowCount = 0
    with open('ModifiedDistanceTable.csv', 'r') as file:
        fileReader = csv.reader(file)
        for row in fileReader:
            for i in range(addressCount):
                distanceArray[rowCount][i] = row[i]
            rowCount += 1

# Dijkstra's
# Create a set to keep track of nodes in shortest path tree

# Set of nodes not yet in tree

# Assign distances with original being huge, 0 distance for starting node

# While set of included nodes doesn't have all the nodes

# Pick unincluded node with lowest distance value

# Add that node to the list of included nodes

# Update distance value of all adjacent nodes
# Iterate through all adjacent nodes

# If the distance from the current node is lower than the current distance, update the distance value

# Populate truck package list

# Populate truck map/path

# Truck status
# Leverage time, then traverse truck graph for that time

# Package status
# Check package status field