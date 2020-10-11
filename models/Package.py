class Package:

    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes = 'none', status = 'At hub'):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.delivery_time = None
