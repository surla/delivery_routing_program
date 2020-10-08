import utils.csv_reader as  csv_reader
from models.Package import Package
from utils.hash_table import HashTable


packages = HashTable()
distances = HashTable()


def get_packages():
    data = csv_reader.get_data('./data/package.csv')

    # Loads all instances of package into global variable packages
    for item in data:
        new_package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
        packages.add(item[0], new_package) # Key is package_id


def get_distances():
    data = csv_reader.get_data('./data/distance.csv')


def start():
    print("-------- Welcome to Package Delivery System --------")

    get_packages()
    get_distances()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

start()

