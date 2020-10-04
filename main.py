# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import utils.csv_reader as  csv_reader
from models.Package import Package

packages = []
distances = []


def load_data():
    data = csv_reader.get_data('./data/package.csv')

    # Loads all instances of package into global variable packages
    for item in data:
        new_package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
        packages.append(new_package)








def start():
    print("-------- Welcome to Package Delivery System --------")

    load_data()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
