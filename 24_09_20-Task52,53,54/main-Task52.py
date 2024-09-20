# Task 52 - Celestial Stars

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + " in " + self.galaxy


sun = Star("Sun", "Milky Way")
print(sun)


class Planet:
    def __init__(self, name, star):
        self.name = name
        self.star = star

    def __str__(self):
        return self.name + " orbits " + self.star.__str__()


earth = Planet("Earth", sun)
print(earth)
