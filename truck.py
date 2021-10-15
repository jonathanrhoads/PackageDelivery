class Truck:

    def __init__(self, packages, start_time):
        self.speed = 18
        self.capacity = 16
        self.distance_travelled = 0
        self.packages = packages
        self.start_time = start_time

    def get_distance_travelled(self):
        return self.distance_travelled

    def set_packages(self, packages):
        self.packages = packages
