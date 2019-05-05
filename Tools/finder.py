#/usr/bin/python3
"""
Tools for scanning trees and printing files and directories matching the given criteria.
Usage:    python  finder.py  <option>  root  string/filename [extension]
"""

import sys, os
import helpers.finder_helpers as helpers

def findFilesAndDirectories(string, root):
    "Print files and directories containing string in their filename (extension excluded)."
    helpers.checkRoot(root)
    for (thisDir, subsHere, filesHere) in os.walk(root):
        for sub in subsHere:
            if string in sub:
                print(thisDir + os.path.sep + sub, end=' ')
                print('(directory)')
        for file in filesHere:
            basename, file_ext = os.path.splitext(file)
            if string.casefold() in basename.casefold():
                print(thisDir + os.path.sep + file)


def findExactFiles(filename, root):
    "Print files matching filename."
    helpers.checkRoot(root)
    for (thisDir, subsHere, filesHere) in os.walk(root):
        for file in filesHere:
            if file.casefold() == filename.casefold():
                print(thisDir + os.path.sep + file)


def findExactDirectories(dirname, root):
    "Print directories matching dirname."
    helpers.checkRoot(root)
    for (thisDir, subsHere, filesHere) in os.walk(root):
        for sub in subsHere:
            if sub.casefold() == dirname.casefold():
                print(thisDir + os.path.sep + sub, end=' ')
                print('(directory)')


def findFilesWithKnownExtension(string, root, extension):
    "Print files that contain string in their filename (extension excluded) and that match the given extension."
    helpers.checkRoot(root)
    for (thisDir, subsHere, filesHere) in os.walk(root):
        for file in [f for f in filesHere if os.path.splitext(f)[1] == extension]:
            basename, file_ext = os.path.splitext(file)
            if string.casefold() in basename.casefold():
                print(thisDir + os.path.sep + file)




if __name__ == '__main__':
    # Get the option (None if not present)
    option = helpers.getOption()

    if not option:
        # Call findFilesAndDirectories()
        try:
            findFilesAndDirectories(sys.argv[1], sys.argv[2])
        except IndexError:
            helpers.showCorrectUsage()
            sys.exit()
        
    
    if option == '-e' or option == '--exact':
        # Call findExactFiles() and findExactDirectories()
        try:
            findExactFiles(sys.argv[2], sys.argv[3])
            findExactDirectories(sys.argv[2], sys.argv[3])
        except IndexError:
            helpers.showCorrectUsage()
            sys.exit()
    elif option == '-x' or option == '--extension':
        # Call findFilesWithKnownExtension
        try:
            findFilesWithKnownExtension(sys.argv[2], sys.argv[3], sys.argv[4])
        except IndexError:
            helpers.showCorrectUsage()
            sys.exit()
    elif option == '-h' or option == '--help':
        # Call helpers.showManPage
        helpers.showManPage()
