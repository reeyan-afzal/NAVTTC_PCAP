# Task 15 - Pyramid Height.

blocks = int(input("Enter the number of blocks: "))
_layers = 0
_usedBlocks = 0

while blocks >= (_layers + 1) + _usedBlocks:
    _layers += 1
    _usedBlocks += _layers

print("\nThe height of the pyramid:", _layers)
