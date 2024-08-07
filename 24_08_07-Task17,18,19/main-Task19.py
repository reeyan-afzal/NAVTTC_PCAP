# Task 19 - Beatles Fans

beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("Geroge Harrison")

print(beatles)

for i in range(len(beatles), 5):
    new_singer = input("Enter the singer name: ")
    beatles.append(new_singer)
print(beatles)

del beatles[4], beatles[3]

beatles.insert(0, "Ringo Starr")
print(beatles)
