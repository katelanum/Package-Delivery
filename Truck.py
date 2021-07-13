from Package import Package


class Truck:
    def __init__(self, id, distance_array, minutes):
        self.package_list = []
        self.package_graph = distance_array
        self.address_list = []
        self.minutes = minutes
        self.status = "at hub"
        self.distance = 0
        self.id = id

    def load_package(self, package_item):
        self.package_list.append(package_item)
        package_item.truck = self.id

    def unload_package(self, package_item):
        self.package_list.remove(package_item)

    def load_packages(self, packages):
        for package in packages:
            self.load_package(package)
            package.on_truck_time = self.minutes

    def get_time(self):
        return self.minutes

    def path(self, starting_point, address_count):
        # this function has a time complexity of O(n^3) where n is the number of packages,
        # this is due to the fact that you are iterating through the columns of distances,
        # while iterating the rows of addresses, while iterating the to visit list,
        # if every package had a different address, all three of these would be n and it is functionally nested
        # within 3 layers
        # space complexity would be O(n + m^2) where n is the number of packages and m is the number of addresses,
        # the package storage only grows linearly, but the address storage grows quadratically since there needs to be
        # an added value to all existing address distances

        # make list of unvisited addresses
        to_visit = []

        # add addresses from the packages on the truck to the unvisited list
        for package in self.package_list:
            to_visit.append(package.full_address)
        current = starting_point

        # while there are still addresses to visit
        while len(to_visit) > 0:

            # closest can be set to 50 because 50 is significantly further than any of the distances
            # between any of the addresses
            closest = float(50)
            next_address = None

            # get to row of current address
            for i in range(0, address_count):
                eval = self.package_graph[0][i]
                if eval == current:

                    # go through row and find lowest value in the address list
                    for j in range(1, address_count):
                        if self.package_graph[j][0] in to_visit:

                            # if within the row there is a value lower than the current closest, change the value of
                            # next to be the address contained in that column and change closest to be that distance
                            proposed = float(self.package_graph[j][i])
                            if proposed < closest:
                                next_address = self.package_graph[j][0]
                                closest = float(self.package_graph[j][i])

            # change current address, remove packages of next address from truck, remove next address from to_visit
            # list, and add the closest distance to the overall distance
            current = next_address
            self.distance += closest
            more_time = closest / (18 / 60)
            self.minutes += more_time
            to_visit.remove(current)
            for package in self.package_list:
                if package.full_address == current:
                    self.unload_package(package)
                    package.delivery_time = self.minutes
                    package.distance_on_truck = self.distance

        # return to hub
        for i in range(0, address_count):
            eval = self.package_graph[0][i]
            if eval == current:
                for j in range(1, address_count):
                    if self.package_graph[j][0] == "HUB":
                        closest = float(self.package_graph[j][i])
                        more_time = closest / (18 / 60)
                        self.minutes += more_time
                        self.distance += closest
                        break
