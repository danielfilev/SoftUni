class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, increase):
        if self.size - self.quantity >= increase:
            self.quantity += increase

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)

print(cup.status())

cup.fill(40)

cup.fill(20)

print(cup.status())
