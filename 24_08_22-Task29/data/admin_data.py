def data():
    print("This is calling the data function from admin_data.py")


def package():
    print("This is calling the package function from admin_data.py")


if __name__ == "__main__":
    data()
    package()
else:
    print("admin_data.py imported in main!")
