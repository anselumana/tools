"""
################################################################################
Usage: python -m cleanpyc [root]
Removes all pyc bytecode files below root (if present must be fullpath).
Caevat: uses os.walk() to scan directories and only checks files in __pycache__ directories.
################################################################################
"""

import os, sys

def removePyc(root):
    "Removes all .pyc files in all __pycache__ directories below root."
    files_removed = 0
    memory_cleaned_in_bytes = 0
    failed = []

    for (currentDir, subsHere, filesHere) in os.walk(root):
        if currentDir.endswith('__pycache__'):
            for file in filesHere:
                try:
                    fullname = os.path.join(currentDir, file)
                    filesize = os.path.getsize(fullname)
                    os.remove(fullname)
                    files_removed += 1
                    memory_cleaned_in_bytes += filesize
                except Exception:
                    failed.append(fullname)
    return (files_removed, memory_cleaned_in_bytes, failed)
    
    

if __name__ == '__main__':    
    # Choose the root
    root = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    if not os.path.exists(root):
        print('Directory %s does not exist.' % root)
        sys.exit()

    # Ask user confirmation
    reply = input('Are you sure you want to remove all bytecode files? (y/n) ')
    if reply != 'y':
        sys.exit()

    files_removed, memory_cleaned_in_bytes, failed = removePyc(root)

    # If no file found
    if files_removed == 0:
        print('No bytecode file found.')
        sys.exit()
    # Output
    print('Successfully Removed %s bytecode files' % files_removed, end=' ')
    print('for a total of %.2fKb.' % (memory_cleaned_in_bytes / 1000))
    if failed:
        print('Failed to remove the following files:')
        for fail in failed:
            print('  ' + file)

