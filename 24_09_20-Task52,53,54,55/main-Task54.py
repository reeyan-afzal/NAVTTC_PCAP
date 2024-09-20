# Task 54 - Check Device

class Device:
    def __init__(self, name):
        self.name = name


class PortableDevice(Device):
    def __init__(self, name):
        super().__init__(name)


class WiredDevice(Device):
    def __init__(self, name):
        super().__init__(name)


class SmartPhone(PortableDevice):
    def __init__(self, name):
        super().__init__(name)


class DesktopComputer(WiredDevice):
    def __init__(self, name):
        super().__init__(name)


device = Device('Generic Device')
portable_device = PortableDevice('Portable Device')
wired_device = WiredDevice('Wired Device')
smart_phone = SmartPhone('iPhone')
desktop_computer = DesktopComputer('iMac')

classes = [Device, PortableDevice, WiredDevice, SmartPhone, DesktopComputer]
objects = [device, portable_device, wired_device, smart_phone, desktop_computer]

print(f"{'Class/Object':<20}", end="")
for obj in objects:
    print(f"{obj.name:<20}", end="")
print("\n" + "-" * (20 * (len(objects) + 1)))

for cs1 in classes:
    print(f"{cs1.__name__:<20}", end="")
    for cs2 in objects:
        comparison = "Yes" if isinstance(cs2, cs1) else "No"
        print(f"{comparison:<20}", end="")
    print()
