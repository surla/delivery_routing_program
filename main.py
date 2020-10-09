import utils.csv_reader as  csv_reader
from models.Package import Package
from models.Truck import Truck
from utils.hash_table import HashTable


packages = HashTable()  # Hash table of all packages in package.csv
distances = HashTable()  # Hash table of all packages in distance.csv
destinations = []  # List of all addresses of delivery destinations


def get_packages():
    data = csv_reader.get_data('./data/package.csv')

    # Loads all instances of package into global variable packages
    for item in data:
        package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
        packages.add(item[0], package)  # Key is package_id


def get_distances():
    data = csv_reader.get_data('./data/distance.csv')

    for item in data:
        address = item[0]  # Variable for address
        destinations.append(address)  # Used to look up distances during delivery.
        distances.add(address, item)  # Adds address as key and distances as value

    print(distances['6351 South 900 East'][8])  # this will get distances using [current_location][index of destination]
    print(destinations)

#  def set_destinations():
# def delivery_package():
#     location = 1  # sets current location to HUB
#     address = packages.get(1).address
#     print("Address: " + address)
#
#     for distance in distances:
#         destinations.append(distance[0])
#
#     print(destinations)


def start():
    print("-------- Welcome to Package Delivery System --------")

    get_packages()
    get_distances()

    truck = Truck()

    deliver = [2, 3, 4, 5]

    for i in deliver:
        truck.load_truck(packages.get(i))

    truck_load = truck.load

    # for load in truck_load:
    #     print(load.address)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

start()

