# Task 32 - String Manipulation-3a

def find_file(path):
    index = path.rfind('/')

    if index != -1:
        file_name = path[index + 1:]

        if not file_name:
            return "No file name found!"
    else:
        return "Invalid path! Please provide a proper path with a file name."

    return file_name


if __name__ == "__main__":
    _path = input("Enter the file you want to find: ")
    _file_name = find_file(_path)
    print(f"File name: {_file_name}")
