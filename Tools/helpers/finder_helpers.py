"""
Helper module for finder.py
"""

import os, sys

def checkRoot(root):
    if not os.path.exists(root):
        print("%s does not exist." % root)
        os._exit(-1)


def getOption():
    "Return the option in sys.argv[1] if valid, else return None or exit with help message."
    if len(sys.argv) < 2:
        showCorrectUsage()
        sys.exit()

    option = sys.argv[1]

    valid_options = ('-e', '-x', '-h', '--exact', '--extension', '--help')

    if option not in valid_options:
        if option.startswith('-'):
            print('Bad option.')
            print('Run "python finder.py -h" for help.')
            sys.exit()
        else:
            option = None

    return option


def showManPage():
    "~ Change PATH_TO_HERE if you move finder.txt elsewhere ~"
    PATH_TO_HERE = r'C:\Tools'
    path_to_manual = PATH_TO_HERE + os.path.sep + 'man_pages' + os.path.sep + 'finder.txt'
    manual = open(path_to_manual)

    print(manual.read())


def showCorrectUsage():
    "Print message about correct usage of finder.py"
    print('Bad usage.')
    print('Run "python finder.py -h" for help.')
    print('Usage:    python finder.py <option> root string/filename [extenstion]')