"""
Usage:   python -m <option> file/directory
Find the size of the given file or entire directory tree.
"""

import os, sys
import helpers.getsize_helpers as helpers


def getFileSize(filename):
    "Returns the file's size in bytes"
    helpers.checkPath(filename)

    fullpath = os.path.abspath(filename)
    
    file_size = os.path.getsize(fullpath)

    return file_size


def getDirectorySize(dirname):
    "Returns the directory's size in bytes"
    helpers.checkPath(dirname)

    fullpath = os.path.abspath(dirname)

    dir_size = 0

    for (thisDir, subsHere, filesHere) in os.walk(fullpath):
        dir_size += os.path.getsize(thisDir)
        for file in filesHere:
            try:
                dir_size += os.path.getsize(thisDir + os.path.sep + file)
            except Exception:
                print('Skipping', end=' ')
                print(thisDir + os.path.sep + file)

    return dir_size


if __name__ == '__main__':
    option = helpers.getOption()

    # Get the file or the directory
    if len(sys.argv) < 3:
        target = sys.argv[1]
    else:
        target = sys.argv[2]

    # Choose the right function to use (target can be a file or a directory)
    getSize = getFileSize if os.path.isfile(target) else getDirectorySize
    
    if not option:
        # Default: show size in Kilobytes
        size = getSize(target)
        print('Size: %.2f Kb.' % (size / 10 ** 3))
        sys.exit()

    # Get size
    size = getSize(target)

    # Show resulting size with the correct unit of mesurement
    if option == '-B' or option == '--Bytes':
        print('Size: %d Bytes.' % size)
    elif option == '-K' or option == '--Kilobytes':
        print('Size: %.2f Kb.' % (size / 10 ** 3))
    elif option == '-M' or option == '--Megabytes':
        print('Size: %.2f Mb.' % (size / 10 ** 6))
    elif option == '-G' or option == '--Gigabytes':
        print('Size: %.2f Gb.' % (size / 10 ** 9))
    elif option == '-T' or option == '--Terabytes':
        print('Size: %.2f Tb.' % (size / 10 ** 12))
    elif option == '-h' or option == '--help':
        print('Show manual page')
    else:
        print('Something strange happened on here...')