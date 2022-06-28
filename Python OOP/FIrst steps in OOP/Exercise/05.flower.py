class Flower:

    def __init__(self, name, water_reqs):
        self.name = name
        self.water_reqs = water_reqs
        self.is_Happy = False

    def water(self, quantity):
        if quantity >= self.water_reqs:
            self.is_Happy = True

    def status(self):
        if self.is_Happy:
            return f"{self.name} is happy"
        return f"{self.name} is not happy"


flower = Flower("Lilly", 100)

flower.water(50)

print(flower.status())

flower.water(60)

print(flower.status())

flower.water(100)

print(flower.status())
