class Package:
    def __init__(self, input_id, input_address, input_city, input_state, input_zip, input_deadline, input_mass,
                 input_notes):
        self.id = input_id
        self.address = input_address
        self.city = input_city
        self.state = input_state
        self.zip = input_zip
        self.full_address = self.address + ', ' + self.city + ', ' + self.state + ' ' + self.zip
        self.deadline = input_deadline
        self.mass = input_mass
        self.notes = input_notes
        self.on_truck_time = 9000000
        self.delivery_time = 9000000
        self.truck = ""
        self.distance_on_truck = 0
