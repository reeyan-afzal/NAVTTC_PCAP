class Appliance:
    def __init__(self, name):
        self.name = name


class KitchenAppliance(Appliance):
    def __init__(self, name):
        super().__init__(name)


class CleaningAppliance(Appliance):
    def __init__(self, name):
        super().__init__(name)


class MicroWave(KitchenAppliance):
    def __init__(self, name):
        super().__init__(name)


class VacuumCleaner(CleaningAppliance):
    def __init__(self, name):
        super().__init__(name)


classes = [Appliance, KitchenAppliance, CleaningAppliance, MicroWave, VacuumCleaner]

print(f"{'Class':<20}", end="")
for cls in classes:
    print(f"{cls.__name__:<20}", end="")
print("\n" + "-" * (20 * (len(classes) + 1)))

for cs1 in classes:
    print(f"{cs1.__name__:<20}", end="")
    for cs2 in classes:
        comparison = "Yes" if issubclass(cs1, cs2) else "No"
        print(f"{comparison:<20}", end="")
    print()
