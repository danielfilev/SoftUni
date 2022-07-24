class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([x.guests for x in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [x for x in self.rooms if room_number == x.number][0]
        return room.take_room(people)

    def free_room(self, room_number):
        room = [x for x in self.rooms if room_number == x.number][0]
        return room.free_room()

    def status(self):
        free_rooms = [str(x.number) for x in self.rooms if not x.is_taken]
        taken_rooms = [str(x.number) for x in self.rooms if x.is_taken]
        result = f"Hotel {self.name} has {self.guests} total guests\n" + \
            f'Free rooms: {", ".join(free_rooms)}\n' + \
            f'Taken rooms: {", ".join(taken_rooms)}'
        return result
