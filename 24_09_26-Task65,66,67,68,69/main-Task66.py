# Task 66 - File Handling 04

from os import strerror


def verify_files(srcname, dstname):
    try:
        src = open(srcname, 'rb')
    except IOError as e:
        print("Error opening source file:", strerror(e.errno))
        return

    try:
        dst = open(dstname, 'rb')
    except IOError as e:
        print("Error opening destination file:", strerror(e.errno))
        src.close()
        return

    try:
        identical = True
        src_byte = src.read(1)
        dst_byte = dst.read(1)

        while src_byte != b'' and dst_byte != b'':
            if src_byte != dst_byte:
                identical = False
                break
            src_byte = src.read(1)
            dst_byte = dst.read(1)

        if src_byte != b'' or dst_byte != b'':
            identical = False

        if identical:
            print("Source and destination files are identical.")
        else:
            print("Source and destination files differ.")

    except IOError as e:
        print("Error during verification:", strerror(e.errno))
    finally:
        if src is not None:
            src.close()
        if dst is not None:
            dst.close()


if __name__ == "__main__":
    _srcname = input("Enter the source file name: ")
    _dstname = input("Enter the destination file name: ")
    verify_files(_srcname, _dstname)
