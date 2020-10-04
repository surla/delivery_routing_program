class Truck:

    def __init__(self):
        self.load = []  # Keeps track of packages loaded on a truck
        self.distance = 0
        self.max_capacity = 16  # Maximum load per truck is 16 packages
        self.speed_mph = 18  # Average speed per truck is 18 mph
