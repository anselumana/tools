"""
Helper module for getsize.py
"""

import sys, os

def getOption():
    valid_options = ('-B', '-K', '-M', '-G', 'T', '-h', '--Bytes', '--Kilobytes', '--Megabytes', '--Gigabytes', '--Terabytes', '--help')

    if len(sys.argv) < 2:
        showCorrectUsage()
        sys.exit()

    option = sys.argv[1]

    if option not in valid_options:
        if option.startswith('-'):
            showCorrectOptionUsage()
            sys.exit()
        else:
            option = None

    return option


def checkPath(path):
    if not os.path.exists(path):
        print('%s does not exist.' % path)
        sys.exit()


def showCorrectUsage():
    "Print message about correct usage of finder.py"
    print('Bad usage.')
    print('Usage:    python getsize.py <option> file/directory')


def showCorrectOptionUsage():
    "Show help message for correct usage of options"
    print('Bad option.')
    print('Run "python finder.py -h" for help.')
