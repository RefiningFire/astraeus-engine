
# For storing 'global' stats to use in composited classes.
class EnvironmentalVariables():
    def __init__(self, resistance):
        self.resistance = resistance

# Allows for distinguishing between powered movement and unpowered movement, i.e. a working spaceship vs a drifting spaceship.
class Movement():
    def __init__(self):
        self.env_var = EnvironmentalVariables(0)
        print(f'Resistance is {self.env_var.resistance}')

    def move_right(self):
        print('move_right')

    def rotate_right(self):
        print('rotate_right')

# If an object is capable of moving itself, it has this component.
class Propulsion():
    def __init__(self):
        self.movement = Movement()

    def power_move_right(self):
        self.movement.move_right()

    def power_rotate_right(self):
        self.movement.rotate_right()

class Stats():
    def __init__(self, mass=0, size=0):
        self.mass = mass
        self.size = size

class Engines():
    def __init__(self, mass, size):
        self.stats = Stats(mass, size)
        self.propulsion = Propulsion()

# Represents the framework upon which ship components can be placed.
class Chassis():
    def __init__(self, mass, size):
        self.stats = Stats(mass, size)

class Ship():
    def __init__(self, mass, size):
        self.stats = Stats()
        self.chassis = Chassis(mass, size)
        self.engines = Engines(mass, size)
        self.stats.mass += self.chassis.stats.mass
        self.stats.mass += self.engines.stats.mass
