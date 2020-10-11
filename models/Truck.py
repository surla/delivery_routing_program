# Truck class will create instances of trucks needed to deliver packages.
class Truck:

    def __init__(self):
        self.load = []  # Keeps track of packages loaded on a truck
        self.distance = 0.0  # Distance traveled
        self.max_capacity = 16  # Maximum load per truck is 16 packages
        self.speed_mph = 18  # Average speed per truck is 18 mph
        self.location = 'HUB'  # Trucks start at HUB
        self.time = None  # Tracks time during delivery

    # O(1)
    # Method used to load packages onto truck.
    # Arguments for this method will be in main.py
    def load_package(self, package):
        self.load.append(package)

    # O(1)
    # Method returns distance traveled based on truck speed
    def distance_time(self, distance):
        return round(distance / (self.speed_mph / 60))

