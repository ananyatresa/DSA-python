class Bird:
    def fly(self):
        print("Some birds can fly")

class Ostrich(Bird):
    def fly(self):
        print("Ostritch cannot fly")

class Pigeon(Bird):
    def fly(self):
        print("Pigeon can fly")

obj_bird = Bird()
obj_ostrich = Ostrich()
obj_pigeon = Pigeon()
obj_bird.fly()
obj_pigeon.fly()
obj_ostrich.fly()