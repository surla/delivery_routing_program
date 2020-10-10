import utils.csv_reader as csv_reader
from models.Package import Package
from models.Truck import Truck
from utils.hash_table import HashTable


all_packages = HashTable()  # Hash table of all packages in package.csv
all_distances = HashTable()  # Hash table of all packages in distance.csv
all_destinations = []  # List of all addresses of delivery destinations

early_deliveries = [1, 2, 4, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 40]
truck_2 = [3, 5, 6, 7, 8, 9, 10, 11, 12, 17, 18, 25, 28, 32, 36, 38]
left_over = [22, 23, 24, 26, 27, 33, 35, 39]


def get_packages():
    data = csv_reader.get_data('data/package.csv')

    # Loads all instances of package into global variable packages
    for item in data:
        package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
        all_packages.add(item[0], package)  # Key is package_id


def get_distances():
    data = csv_reader.get_data('data/distance.csv')

    for item in data:
        address = item[0]  # Variable for address
        all_destinations.append(address)  # Used to look up distances during delivery.
        all_distances.add(address, item)  # Adds address as key and distances as value


#  Bubble Sort as greedy algorithm to get packages in order from closest to farthest
# def sort_packages(arr):
#     n = len(arr)
#
#     for i in range(n):
#         for j in range(0, n-1):
#             if float(all_distances[all_packages.get(arr[j]).address][1]) > float(all_distances[all_packages.get(arr[j+1]).address][1]):
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#     return arr

# Method uses Greedy algorithm to find next pack that is the closet to the current location of the truck.
def next_package(truck_location, truck_load):
    next_nearest = 100
    new_package = None

    # Last package will be returned
    if len(truck_load) == 1:
        return truck_load[0]

    for item in truck_load:
        address = item.address
        delivery_address = all_destinations.index(address)

        if float(all_distances[truck_location][delivery_address]) < next_nearest:
            next_nearest = float(all_distances[truck_location][delivery_address])
            new_package = item

    return new_package


# Method will load packages and get delivery distances
def delivery(truck, group):
    load = truck.load

    for i in group:
        truck.load_package(all_packages.get(i))

    while load:
        package = next_package(truck.location, load)

        truck.distance += float(all_distances[truck.location][all_destinations.index(package.address)])
        package.status = 'Delivered'
        truck.location = package.address
        truck.load.remove(package)

    # Checks if truck load is empty and goes back to 'HUB'
    if not truck.load:
        truck.distance += float(all_distances[truck.location][1])
        truck.location = 'HUB'


def start():
    print("-------- Welcome to Package Delivery System --------")

    truck1 = Truck()
    truck2 = Truck()

    get_packages()
    get_distances()
    delivery(truck1, early_deliveries)
    delivery(truck2, truck_2)
    delivery(truck1, left_over)

    print("Truck 1 distance: " + str(truck1.distance))
    print("Truck 2 distance: " + str(truck2.distance))
    print(truck1.distance + truck2.distance)




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

start()

