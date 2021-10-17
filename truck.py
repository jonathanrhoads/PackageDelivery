class Truck:

    def __init__(self, packages, start_time):
        '''
        Initializes the truck to have a list of packages that it will hold and the time it will start delivering.
        The truck starts with a distance travelled of 0 then will have distances added on after each delivery.
        :param packages:
        :param start_time:
        '''
        self.speed = 18
        self.distance_travelled = 0
        self.packages = packages
        self.start_time = start_time

    def get_distance_travelled(self):
        return self.distance_travelled

    def set_packages(self, packages):
        self.packages = packages
