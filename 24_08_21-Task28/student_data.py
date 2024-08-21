def data():
    print("This is calling the data function from std_data.py")


def package():
    print("This is calling the package function from std_data.py")


if __name__ == "__main__":
    data()
    package()
else:
    print("student_data.py imported in main!")

