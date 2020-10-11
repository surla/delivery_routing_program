from datetime import datetime

import utils.csv_reader as csv_reader
from models.Package import Package
from models.Truck import Truck
from utils.hash_table import HashTable
from utils.time import Time


all_packages = HashTable()  # Hash table to load all packages in package.csv
all_distances = HashTable()  # Hash table to load all packages in distance.csv
all_destinations = []  # List of all addresses of delivery destinations

early_deliveries = [1, 2, 4, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 40]
truck_2 = [3, 5, 6, 7, 8, 9, 10, 11, 12, 17, 18, 25, 28, 32, 36, 38]
left_over = [22, 23, 24, 26, 27, 33, 35, 39]

delivered_packages = []


# Method to get all packages in package.csv. Data saved to all_packages hash table
def get_packages():
    data = csv_reader.get_data('data/package.csv')

    # Loads all instances of package into global variable packages
    for item in data:
        package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
        all_packages.add(item[0], package)  # Key is package_id


# Method to get all distances in distance.csv. Data saved to all distances hash table
def get_distances():
    data = csv_reader.get_data('data/distance.csv')

    for item in data:
        address = item[0]  # Variable for address
        all_destinations.append(address)  # Used to look up distances during delivery.
        all_distances.add(address, item)  # Adds address as key and distances as value


# Method uses Greedy algorithm to find next pack that is the closet to the current location of the truck.
def next_package(truck_location, truck_load):
    next_nearest = 50
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
    # Loads packages into truck and sets status to 'En route'
    for i in group:
        package = all_packages.get(i)

        truck.load_package(package)
        package.status = 'En route'

    while load:
        package = next_package(truck.location, load)
        deliver_distance = float(all_distances[truck.location][all_destinations.index(package.address)])
        truck.distance += deliver_distance

        truck.time.update_time(truck.distance_time(deliver_distance))
        package.delivery_time = truck.time.get_time()

        delivered_packages.append(package)
        truck.location = package.address
        truck.load.remove(package)

    # Checks if truck load is empty and goes back to 'HUB'
    if not truck.load:
        truck.distance += float(all_distances[truck.location][1])
        truck.location = 'HUB'

# Check delivery status of package. If delivery time is before time entered, package status changes to 'Delivered'
def delivery_status(time, val2 = None):
    for item in delivered_packages:
        date_time = datetime.strptime(item.delivery_time, '%H:%M').time()

        if date_time < datetime.strptime(time, '%H:%M').time():
            item.status = 'Delivered at ' + item.delivery_time


def user_interface():
    while True:
        print('\n---------- Welcome to Package Delivery System ----------')

        print('1 - View status of all packages via time')
        print('2 - View package data via ID')
        print('3 - Exit program')
        val = input('\nEnter menu number: ')
        if val == '1':
            time = input('\nEnter time in format HH:MM to check all stauts of all packages: ')

            print('\n---------- Status of all packages at ' + time + ' ----------')
            print('{: <15} {: <45} {: <25} {: <20} {: <15} {: <15} {: <15}'.format('Package ID', 'Address', 'City', 'Zip Code', 'Weight', 'Deadline', 'Delivery Status'))
            for item in delivered_packages:
                delivery_status(time)
                print('{: <15} {: <45} {: <20} {: >10} {: >18} {: >20} {: >25}'.format(item.package_id, item.address, item.city, item.zip_code, item.weight, item.deadline, item.status))

        if val == '2':
            package_id = input('\nEnter package id to see package information: ')
            package = all_packages.get(package_id)
            package.status = 'Delivered at ' + package.delivery_time

            print('\n---------- Information for Package' + package_id + ' ----------')
            print('{: <15} {: <45} {: <25} {: <20} {: <15} {: <15} {: <15}'.format('Package ID', 'Address', 'City',
                                                                                   'Zip Code', 'Weight', 'Deadline',
                                                                                   'Delivery Status'))
            print('{: <15} {: <45} {: <20} {: >10} {: >18} {: >20} {: >25}'.format(package.package_id, package.address, package.city, package.zip_code, package.weight, package.deadline, package.status))

        if val == '3':
            print('***** Program exited ******')
            exit()

def start():
    truck1 = Truck()
    truck2 = Truck()
    get_packages()
    get_distances()

    truck1.time = Time(8, 00)  # Truck 1 start time 8:00 am
    truck2.time = Time(9, 30)  # Truck 2 start time 9:30 a

    delivery(truck1, early_deliveries)
    delivery(truck2, truck_2)
    delivery(truck1, left_over)

    print('\n********** Delivery Information **********')
    print('Truck 1 distance traveled: ' + str(truck1.distance) + ' miles.')
    print('Truck 2 distance traveled: ' + str(round(truck2.distance, 2)) + ' miles.')
    print('\n Total distance traveled to deliver packages is ' + str(round(truck1.distance + truck2.distance, 2)) + ' miles.')

    user_interface()


if __name__ == '__main__':
    start()


