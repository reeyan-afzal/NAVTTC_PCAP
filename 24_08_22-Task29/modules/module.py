counter = 0

if __name__ == "__main__":
    print("I am module.py")
else:
    print("module.py imported in main!")
    print("initial value of counter from module.py:", counter)
    counter += 1
