#hash is package id, value is Pakage object

class PackageHashTable:
    #initial capacity of 40 due to that being the original number of packages
    def __init__(self, capacity=40):
        self.array = [None] * capacity

    # hashing function not completely needed, but getting put in for the sake of completeness
    def hash(packageId):
        return packageId % len(PackageHashTable)

    # insert is going to get the hash of the packageId, then it will either replace the value/packageObject
    # if already there or it will create an entry at that key, before insertion handles any necessary size management
    def insert(self, packageId, packageObject):
        key = hash(packageId)
        self.sizeManage()
        if self.array[key] is not None:
            for pair in self.array[key]:
                if pair[0] == key:
                    pair[1] = packageObject
                    break
            else:
                self.array[key].append([key,packageObject])
        else:
            self.array[key]= []
            self.array[key].append([key,packageObject])

    # get will search for the key/hashed packageId and then will return the value/packageObject,
    # if the package does not exist, it will throw an exception
    def get(self,packageId):
        key = self.hash(packageId)
        if self.array[key] is None:
            raise Exception("The package you are searching for does not exist")
        else:
            for pair in self.array[key]:
                if pair[0] == key:
                    return pair[1]
            raise Exception("The package you are searching for does not exist")

    # need to check if the table is full, resizes if needed by doubling the size on a new table and then transferring
    # over the data from the prior table
    def sizeManage(self):
        values = 0
        for value in self.array:
            if value is not None:
                values += 1
        if values == len(self.array):
            newTable = PackageHashTable(capacity=len(self.array)*2)
            for value in range(len(self.array)):
                if self.array[value] is None:
                    continue
                for pair in self.array[value]:
                    newTable.insert(pair[0], pair[1])
            self.array = newTable.array





