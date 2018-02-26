# Marcy Held
# SI 506 - PS 10
# 3 Dec 2016

# import statements
import os_506
# this is a file module we have written to provide tools for this problem set -- you'll need os_506.py in your directory for the import to work!
import unittest

#####

#os_506.listRecursive() # this invokes a function that recursively navigates through a directory and pretty-prints the contents of that directory. It is for your reference -- you can see the implementation in the os_506 file!

## [PROBLEM 1]

# Fill in the sum function here:

def sum(lst):
    returnSum = 0
    for item in lst:
        returnSum += item
    return returnSum

## [PROBLEM 2]

## Provided for your use in Problem 2. DO NOT CHANGE THIS CODE.
extensionTypes = {
    'movie': ['.mp4','.mov'],
    'image': ['.jpg','.jpeg','.png','.bmp','.svg'],
    'document': ['.docx','.pdf','.txt'],
    'code': ['.py','.python','.java','.js']
}
## End provided code.

# Finish the definition of the getFileType function here, making reference to the extensionTypes dictionary:
def getFileType(path):
    # os.path.splitext separates an extension with a filename.
    # for example: os.path.splitext('/usr/soney/file.txt')
    # returns: ('/usr/soney/file', '.txt')
    filename,extension = os_506.splitext(path)

    if extension in extensionTypes['movie']:
        return 'movie'
    elif extension in extensionTypes['image']:
        return 'image'
    elif extension in extensionTypes['document']:
        return 'document'
    elif extension in extensionTypes['code']:
        return 'code'
    else:
        return 'unknown'

#print getFileType('/usr/soney/file.txt')

## [PROBLEM 3]

## Add code to what we've provided below in order to finish defining the getSize function.
## getSize INPUT: a path string (a full path to a file OR directory)
## getSize RETURN VAL: the numeric size of that file or directory, including any subdirectories

def getSize(path=os_506.getCwd()):
    total = 0
    if os_506.isfile(path): # base case, already taken care of
        return os_506.getsize(path)
    elif os_506.isdir(path): # recursive case
        # TODO: Fill the rest of the code for the recursive case in here. You may choose to use the list comprehension below, or not. There is more than one way to complete this.
        try:
            absoluteChildPaths = [os_506.join(path,relChildPath) for relChildPath in os_506.listdir(path)]
            total = 0
            for path in absoluteChildPaths:
                total += getSize(path)
            return total
        except OSError as e: # in the case where you have an operating system error looking for the paths
            return 0 # return 0 because you couldn't calculate the size
        
## [PROBLEM 4]
## Finish defining the getCategorySizes function here.
## Function INPUT: path, a full path string to a file or directory
## RETURN VAL: a dictionary whose keys are file types that appear (as a result of calling `getFileType`) and values are the total size of all the files of that file type

def getCategorySizes(path=os_506.getCwd(),bins=None): # Default values: the path is default to the urrent working directory, default bins are None (no file types that appear)
    # print " " * recursion_level + " level " + str(recursion_level)
    #print path
    if bins==None:
        bins = {}
    ## In here: translate English into code bit by bit!
    # If the path is a file (base case)
    if os_506.isfile(path):
        # Get the file type and save it in a variable
        type_of_file = getFileType(path)
        # Get the file size and save it in a variable
        size_of_file = getSize(path)
        # Check to see if the file type is in the bins dictionary
        if type_of_file in bins:
        # If it is, add the file size to its value
            bins[type_of_file] = bins[type_of_file] + size_of_file
            #return bins[type_of_file]
        # If it's not, set the file size to be its value
        else:
            bins[type_of_file] = size_of_file
            #return bins[type_of_file]

    # But if the path is a directory
    elif os_506.isdir(path):
        # Then for each file or directory in the directory
        # (Code for a list of all files/dirs in the directory: os_506.listdir(path))
        # Pass the bins directory (with the appropriate path as the first param) to the getCategorySizes function
        try:
            for item in os_506.listdir(path):
                getCategorySizes(os_506.join(path,item), bins)
        except OSError as e:
            pass 
    # print bins
    return bins


## [PROBLEM 5] (OPTIONAL, not graded)
# All our tests use a "fake" filesystem. Now that you have your code working, have some fun running it on your actual filesystem.

## To do so, uncomment this line:
#os_506.USE_REAL_FILESTYSTEM = True

## And invoke the getCategorySizes function and/or the getSize function on some of your directory paths, and print out the results!
## NOTE: don't call getSize('/') -- on your base path -- unless you are prepared to wait a very long time for your program to finish running...

########## Tests below this line; DO NOT EDIT/CHANGE THIS CODE ##########

class RecursionUnitTest(unittest.TestCase):
    def test_problem1(self):
        self.assertEqual(sum([-10]), -10)
        self.assertEqual(sum([3,2]), 5)
        self.assertEqual(sum([1,2,3,4,5,6]), 21)
        self.assertEqual(sum([]), 0)

    def test_problem2(self):
        self.assertEqual(extensionTypes, {
            'movie': ['.mp4','.mov'],
            'image': ['.jpg','.jpeg','.png','.bmp','.svg'],
            'document': ['.docx','.pdf','.txt'],
            'code': ['.py','.python','.java','.js']
        }, 'Do not change the default extension types from the original problem set source.')
        self.assertEqual(getFileType(os_506.join(os_506.getRoot(),'i', 'just.dunno')), 'unknown')
        self.assertEqual(getFileType(os_506.join(os_506.getRoot(),'home','movie.mp4')), 'movie')
        self.assertEqual(getFileType(os_506.join(os_506.getRoot(),'usr','soney','img.jpg')), 'image')
        self.assertEqual(getFileType(os_506.join(os_506.getRoot(),'Users','soney','Images','michigan.jpeg')), 'image')
        self.assertEqual(getFileType(os_506.join(os_506.getRoot(),'Documents','textual.txt')), 'document')
        self.assertEqual(getFileType(os_506.join(os_506.getRoot(),'development','ps10.py')), 'code')
        self.assertEqual(getFileType(os_506.join(os_506.getRoot(),'development','constraint.js')), 'code')

    def test_problem3(self):
        self.assertEqual(getSize(os_506.join(os_506.getRoot(),'ps10_solution.py')), 500)
        self.assertEqual(getSize(os_506.join(os_506.getRoot(),'Users','steve')), 142010)
        self.assertEqual(getSize(os_506.join(os_506.getRoot(),'Users','steve','Images')), 1800)
        self.assertEqual(getSize(os_506.getRoot()), 144999)

    def test_problem4(self):
        self.assertEqual(getCategorySizes(os_506.join(os_506.getRoot(),'ps10_solution.py')), {'code': 500})
        self.assertEqual(getCategorySizes(os_506.join(os_506.getRoot(),'Users','steve')), {'movie': 140000, 'image': 1800, 'code': 210})
        self.assertEqual(getCategorySizes(os_506.join(os_506.getRoot(),'Users','steve','Images')), {'image': 1800})
        self.assertEqual(getCategorySizes(os_506.getRoot()), {'movie': 140000, 'image': 2700, 'code': 1309, 'document': 990})

## This following code controls to make sure you don't run the tests on your real file system, but on our fake-filesystem code. Don't change it!!
if __name__ == '__main__':
    was_use_fs = os_506.USE_REAL_FILESTYSTEM
    os_506.USE_REAL_FILESTYSTEM = False

    unittest.main(verbosity=2)

    os_506.USE_REAL_FILESTYSTEM = was_use_fs