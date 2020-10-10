import utils.csv_reader as csv_reader
from models.Package import Package
from models.Truck import Truck
from utils.hash_table import HashTable


packages = HashTable()  # Hash table of all packages in package.csv
distances = HashTable()  # Hash table of all packages in distance.csv
destinations = []  # List of all addresses of delivery destinations

early_deliveries = [1, 6, 13, 14, 15, 16, 20, 25, 29, 30, 31, 34, 37, 40]


def get_packages():
    data = csv_reader.get_data('data/package.csv')

    # Loads all instances of package into global variable packages
    for item in data:
        package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
        packages.add(item[0], package)  # Key is package_id


def get_distances():
    data = csv_reader.get_data('data/distance.csv')

    for item in data:
        address = item[0]  # Variable for address
        destinations.append(address)  # Used to look up distances during delivery.
        distances.add(address, item)  # Adds address as key and distances as value

    # print(distances['6351 South 900 East'][8])  # this will get distances using [current_location][index of destination]
    # print(destinations)


def delivery(group):
    location = 'HUB'  # sets current location to HUB
    truck = Truck()

    for i in group:
        truck.load_package(packages.get(i))

    # Get index of destination
    for item in truck.load:
        address = item.address
        delivery_address = destinations.index(address)
        print(distances[location][delivery_address])  # Gets distances between current location and devlivery address
        location = address  # Sets location to address afer


def start():
    print("-------- Welcome to Package Delivery System --------")

    get_packages()
    get_distances()
    delivery(early_deliveries)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

start()

