class Package:

    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes, status, time):
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.time = time

    def __str__(self):
        return f"Package ID: {self.id} | Address {self.address}, {self.city}, {self.state} {self.zip_code} | " \
               f"Deadline: {self.deadline.time().strftime('%I:%M%p')} | Weight: {self.weight}"

    def get_id(self):
        return self.id

    def get_address(self):
        return self.address

    def get_deadline(self):
        return self.deadline

    def get_weight(self):
        return self.weight

    def get_notes(self):
        return self.notes

    def get_status(self):
        return self.status

    def get_time(self):
        return self.time

    def set_status(self, status):
        self.status = status

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def set_time(self, time):
        self.time = time
