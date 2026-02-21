class Classroom:
    def __init__(self, name, total_desks, occupied_desks=0):
        self._name = name
        self.total_desks = total_desks
        self.occupied_desks = occupied_desks
    @property
    def name(self):
        return self._name

    @property
    def total_desks(self):
        return self._total_desks

    @total_desks.setter
    def total_desks(self, value):
        if value < 1:
            raise ValueError("Total desks must be at least 1")
        self._total_desks = value

    @property
    def occupied_desks(self):
        return self._occupied_desks
    @occupied_desks.setter
    def occupied_desks(self, value):
        if value < 0:
            raise ValueError("Occupied desks cannot be negative")
        elif value > self.total_desks:
            raise ValueError("Occupied desks cannot exceed total desks")
        self._occupied_desks = value
    
    @property
    def empty_desks(self):
        return self.total_desks - self.occupied_desks
    @property
    def fill_rate(self):
        return round((self.occupied_desks / self.total_desks) * 100, 1)
    def seat(self, students):
        if students < 0:
            raise ValueError("Number of students must be positive")
        elif self.occupied_desks + students > self.total_desks:
            raise ValueError("Not enough empty desks")
        else:
            self.occupied_desks += students
    def dismiss(self, students):
        if students < 0:    
            raise ValueError("Number of students must be positive")
        elif self.occupied_desks - students < 0:
            raise ValueError("Cannot dismiss more than seated")
        else:
            self.occupied_desks -= students
    
c = Classroom("Room 101", 35)
print(c.name, c.empty_desks, c.fill_rate)

c.seat(20)
print(c.occupied_desks, c.fill_rate)

c.dismiss(8)
print(c.empty_desks)

try:
    c.seat(25)
except ValueError as e:
    print(e)

try:
    c.name = "X"
except AttributeError:
    print("Cannot change classroom name")
