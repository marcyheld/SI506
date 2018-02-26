# If you set this to 'True', you will use your actual filesystem information
USE_REAL_FILESTYSTEM = True

# Used for operating system functions (the types of functions you would run on the command line)
import os
import json

NO_PERMISSION = {}

# Utility methods to determine if a given object is a dictionary or an integer
(isDict,isInt) = [lambda x,o=s: type(x)==type(o) for s in [{},0]]

# Get the root of the filesystem (OS-dependent)
def getRoot():
    return os.path.normpath(os.sep)

# Get the home directory of the current user
def getHome():
    if USE_REAL_FILESTYSTEM:
        return os.path.expanduser('~')
    else:
        return join(getRoot(), 'Users', 'steve')

# Is this the root of the filesystem
def __isRoot(path):
    # http://stackoverflow.com/questions/12041525/a-system-independent-way-using-python-to-get-the-root-directory-drive-on-which-p
    # but we want something that return "\" for windows, not "c:\", so we use os.path.normpath instead of os.path.abspath
    return path == getRoot()

# Is it a hidden file (something that wouldn't show up in finder)
def __isHidden(path):
    head, tail = os.path.split(os.path.normpath(path))
    return tail.startswith('.')

# The current working directory:
def getCwd():
    if USE_REAL_FILESTYSTEM:
        return os.getcwd()
    else:
        return join(getRoot(), 'Users', 'steve')

fake_filestructure = {
    'Applications': {
        'Atom.app': NO_PERMISSION,
        'Sublime.app': NO_PERMISSION
    },
    '106_solutions': NO_PERMISSION,
    '506_solutions': NO_PERMISSION,
    'ps10_solution.py': 500,
    'Users': {
        'steve': {
            'Desktop': {
                '106': {
                    'ps10.py': 100
                },
                '506': {
                    'ps10.py': 110
                }
            },
            'Images': {
                'michigan_stadium.jpeg': 1000,
                'detroit.jpg': 800
            },
            'Movies': {
                'graduation.mov': 80000,
                'convocation.mov': 60000
            }
        },
        'jackie': {
            'Documents': {
                'finalexam1.docx': 600
            },
        },
        'paul': {
            'Papers': {
                'paper1.pdf': 120,
                'paper3.pdf': 130,
                'paper6.pdf': 140
            },
            'code': {
                'runestone': {
                    'runestone_client.js': 599
                }
            },
            'Images': {
                'heinz_field.jpg': 900
            }
        }
    }
}

# For when USE_REAL_FILESTYSTEM == False, navigate key/value pairs of a dictionary
# as if they are directories and files
def __fake_nav(path, recurse_level = 0):
    # gets rid of any oddities in the path, like if it includes .. or .
    # to resolve to a normal path
    normpath = os.path.normpath(path)

    # base case:
    #     if we are in the root, return the root of the fake file structure
    if __isRoot(normpath):
        return fake_filestructure
    else:
        # recursive case:
        #     split the path into a filename and a
        head, tail = os.path.split(normpath)
        obj = __fake_nav(head, recurse_level+1)
        if isDict(obj) and tail in obj:
            return obj[tail]
        else:
            raise OSError('Could not find {} in {}'.format(tail, head))

# takes two parts of a path and joins them according to OS conventions
# example: join('/users/soney', 'myProg.py') -> '/users/soney/myProg.py'
def join(*args):
    return os.path.join(*args)

def splitext(path):
    return os.path.splitext(path)

# list all of the filenames in a directory
def listdir(path,includeHidden=False):
    contents = []

    if USE_REAL_FILESTYSTEM:
        contents = os.listdir(path)
    else:
        obj = __fake_nav(path)
        if isDict(obj):
            if obj is NO_PERMISSION:
                raise OSError('Permission denied: {}'.format(path))
            else:
                contents = obj.keys()
        else:
            raise OSError('Not a directory: {}'.format(path))

    if includeHidden:
        return contents
    else:
        return [c for c in contents if not __isHidden(c)]

# True if a given path points to a file
def isfile(path):
    if USE_REAL_FILESTYSTEM:
        return os.path.isfile(path)
    else:
        obj = __fake_nav(path)
        return isInt(obj)

# True if a given path points to a directory
def isdir(path):
    if USE_REAL_FILESTYSTEM:
        return os.path.isdir(path)
    else:
        obj = __fake_nav(path)
        return isDict(obj)


# Give the size (in bytes) of a file
def getsize(path):
    if USE_REAL_FILESTYSTEM:
        return os.path.getsize(path)
    else:
        obj = __fake_nav(path)
        if isInt(obj):
            return obj
        else:
            raise OSError('Not a file: {}'.format(path))


# Provided for your reference: code to recursively navigate through a directory
def listRecursive(path=getCwd(),recursionLevel=0,indentChar='    '):
    try:
        contents = listdir(path)
    except OSError as e:
        contents = []

    if len(contents) == 0:
        print('{indent}(empty)'.format(indent=indentChar*recursionLevel))
    else:
        for relativePath in contents:
            absolutePath = join(path, relativePath)

            if isdir(absolutePath):
                print('{indent}{dname}{sep}:'.format(indent=indentChar*recursionLevel, dname=relativePath, sep=os.sep))
                listRecursive(absolutePath, recursionLevel=recursionLevel+1)
            elif isfile(absolutePath):
                print('{indent}{fname}: {size}'.format(indent=indentChar*recursionLevel, fname=relativePath, size=getsize(absolutePath)))

if __name__ == '__main__':
    print('You should run ps10.py, not this file.')

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMM             MMMMMMMMMMMMMMMMM             MMMMMMMMM
#MMMMMMM              MMMMMMMMMMMMMMM              MMMMMMMMM
#MMMMMMM                MMMMMMMMMMM                MMMMMMMMM
#MMMMMMM                 MMMMMMMMM                 MMMMMMMMM
#MMMMMMM                  MMMMMMM                  MMMMMMMMM
#MMMMMMMMMMM               MMMMM                MMMMMMMMMMMM
#MMMMMMMMMMM                MMM                 MMMMMMMMMMMM
#MMMMMMMMMMM                 V                  MMMMMMMMMMMM
#MMMMMMMMMMM                                    MMMMMMMMMMMM
#MMMMMMMMMMM         ^               ^          MMMMMMMMMMMM
#MMMMMMMMMMM         MM             MM          MMMMMMMMMMMM
#MMMMMMMMMMM         MMMM         MMMM          MMMMMMMMMMMM
#MMMMMMMMMMM         MMMMM       MMMMM          MMMMMMMMMMMM
#MMMMMMMMMMM         MMMMMM     MMMMMM          MMMMMMMMMMMM
#MMMMMMM                MMMM   MMMM                MMMMMMMMM
#MMMMMMM                MMMMMVMMMMM                MMMMMMMMM
#MMMMMMM                MMMMMMMMMMM                MMMMMMMMM
#MMMMMMM                MMMMMMMMMMM                MMMMMMMMM
#MMMMMMM                MMMMMMMMMMM                MMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMM/-------------------------/MMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMM/- SCHOOL OF INFORMATION -/MMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMM/-------------------------/MMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
