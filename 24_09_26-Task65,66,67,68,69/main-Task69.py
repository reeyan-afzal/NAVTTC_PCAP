# Task 69 - File Handling 07

class StudentsDataException(Exception):
    """Base exception class for student data errors"""
    pass


class BadLine(StudentsDataException):
    """Exception raised when a line in the file is malformed"""

    def __init__(self, line):
        self.line = line
        super().__init__(f"Bad line format: {line}")


class FileEmpty(StudentsDataException):
    """Exception raised when the file is empty"""

    def __init__(self, file_name):
        super().__init__(f"The file '{file_name}' is empty")


def process_file(file_name):
    students = {}

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

            if not lines:
                raise FileEmpty(file_name)

            for line in lines:
                parts = line.strip().split()
                if len(parts) != 3:
                    raise BadLine(line)

                first_name, last_name, points = parts[0], parts[1], parts[2]

                try:
                    points = float(points)
                except ValueError:
                    raise BadLine(line)

                full_name = f"{first_name} {last_name}"
                if full_name in students:
                    students[full_name] += points
                else:
                    students[full_name] = points

        for name, total_points in sorted(students.items()):
            print(f"{name}\t{total_points}")

    except FileEmpty as e:
        print(e)
    except BadLine as e:
        print(e)
    except IOError:
        print(f"Cannot open file: {file_name}")


if __name__ == "__main__":
    _file_name = input("Enter the file name: ")
    process_file(_file_name)
