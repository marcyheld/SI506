###################
# Marcy Held
# Problem set 8
# 13 Nov 2016

import json
import unittest
import random


#### PART 1: Class Inheritance mechanics

## [PROBLEM 1]
print "\n\n***** Problem 1 *****"
## We've provided a definition of a class Student, similar to the one you may have seen in lecture. Do not change this code:

class Student():
    def __init__(this_Student, name, years_at_umich=1):
        this_Student.name = name
        this_Student.years_UM = years_at_umich
        this_Student.bonus_points = random.randrange(1000)

    def shout(this_Student, phrase_to_shout):
        print phrase_to_shout  # print is for ppl!

    def __str__(this_Student):
        return "My name is {}, and I've been at UMich for about {} years.".format(this_Student.name,this_Student.years_UM)

    def year_at_umich(this_Student):
        return this_Student.years_UM

#### DONE WITH STUDENT CLASS DEFINITION

# Define your Programming_Student subclass of Student here:

class Programming_Student(Student):
    def __init__(self, name, years_at_umich=1, number_programs_written=0):
        Student.__init__(self, name, years_at_umich)
        self.number_programs_written = number_programs_written

    def write_programs(self, progs=1):
        self.number_programs_written += progs
        return self.number_programs_written

    def productivity(self):
        return float(self.number_programs_written) / self.years_UM

    def shout(self, phrase):
        Student.shout(self, phrase)
        print "Also, Python is pretty cool."

    def __str__(self):
        return "My name is {}, I've been at UMich for about {} years, and I have written {} programs while here.".format(self.name, self.years_UM, self.number_programs_written)

# The following code should work if you have successfully defined Programming_Student as specified! You can uncomment it to try it out, and use it to help you understand the instructions. Do not change this code, but feel free to make other print statements outside of it if that helps you!
print "==========="
pst = Programming_Student("Jess", 3)
pst.write_programs()
pst.write_programs(4)
print pst  # should print: My name is Jess, I've been at UMich for about 3 years, and I have written 5 programs while here.
pst.shout("I'm doing awesome on this problem set.")  # Should print: I'm doing awesome on this problem set.
# # Also, Python is pretty cool.
print "==========="


# Write Unit Tests here to make sure the code does what all of the instructions say.
class TestingProblem1(unittest.TestCase):
    def test_Problem1_NameTest(self):
        self.assertEqual(testStudent.name, "Marcy", "Testing to see if student.name instance variable is correct")

    def test_Problem1_ProductivityValueTest(self):
        self.assertEqual(testStudent.productivity(), .25, "Testing to see if productivity function returns num of programs written divided by num of years at UM")

    def test_Problem1_WriteProgramsMethodTest(self):
        self.assertEqual(testStudent.write_programs(2), 3, "Testing to see if write_programs method increments num of programs written")

testStudent = Programming_Student("Marcy", 4, 1) #(name, years, programs)

#### PART 2: Advanced Accumulation
## [PROBLEM 2]
print "\n\n***** Problem 2 *****"

## Provided code
names = ["Albert", "Bisi", "Cai", "Dinesh", "Euijin"]
seniority = [1, 5, 2, 4, 1]
programs_written = [10, 500, 20, 131, 46]
## End provided code

# Write your code to create a list of tuples called student_tups here:

student_tups = zip(names, seniority, programs_written)

# Write a unit test here that checks whether you have correctly solved this problem: 
class TestingProblem2(unittest.TestCase):
    def test_Problem2_tupsTest(self):
        self.assertTrue(student_tups[1] == ('Bisi', 5, 500))

## [PROBLEM 3]
print "\n\n***** Problem 3 *****"
# Use a list comprehension to create a list of Programming_Student instances out of the student_tups list you just created, and save that list in a variable called programmers:
programmers = [Programming_Student(*student) for student in student_tups]

# Write unit tests that check whether the programmers list is correct here:

class Testing_ProgrammersList(unittest.TestCase):
    def test_Problem3_nameAtIndex3(self):
        self.assertEqual(programmers[3].name, 'Dinesh')
    def test_Problem3_yearsAtUMIndex2(self):
        self.assertEqual(programmers[2].years_UM, 2)
    def test_Problem3_productivityForIndex4(self):
        self.assertTrue(programmers[4].productivity() == 46)
    def test_Problem3_typeTest(self):
         self.assertTrue(type(programmers[0]) == type(testStudent))
    def test_Problem3_listLength(self):
        self.assertEqual(len(programmers), 5)

## [PROBLEM 4]
print "\n\n***** Problem 4 *****"
# Use the Python map function with the programmers list you just created in order to create a list of numbers representing the productivity of each student:
productivities = map(lambda s: s.productivity(), programmers)

# Write a unit test that checks whether the productivities list is set correctly:
class Test_ProductivitiesList(unittest.TestCase):
    def test_Problem4_TestAtIndex3(self):
        self.assertEqual(productivities[3], 32.75)


## [PROBLEM 5]
print "\n\n***** Problem 5 *****"
# Use a list comprehension on the list programmers that you created above, in order to create a list of tuples wherein each tuple has a student's name and productivity value. Save the list of tuples in a variable called names_and_productivities:
names_and_productivities = [(student.name, student.productivity())for student in programmers]

# Write a unit test that checks whether names_and_productivities is set correctly:
class Test_NamesAndProductivitiesList(unittest.TestCase):
    def test_Problem5_TestAtIndex2(self):
        self.assertTrue(names_and_productivities[2] == ('Cai', 10.0))

## [PROBLEM 6]
print "\n\n***** Problem 6 *****"
# Use the Python filter function to select the subset of programmers who have names with 5 or more characters. Save this in a variable called long_names:
long_names = filter(lambda s: (len(s.name) > 5), programmers)

# Write a unit test that checks whether long_names is set correctly:
class Test_LongNames(unittest.TestCase):
    def test_Problem6_TestOfLength(self):
        self.assertEqual(len(long_names), 3)
    def test_Problem6_TestAtIndex1(self):
        self.assertEqual(long_names[1].name, "Dinesh")

## [PROBLEM 7]
print "\n\n***** Problem 7 *****"
# Use a list comprehension to generate a list of just the names of those programmer instances whose name is longer than their seniority (i.e., ["Albert", "Cai", "Dinesh", "Eujin"]). Assign it to a variable called names_with_not_too_much_seniority:
names_with_not_too_much_seniority = [s.name for s in programmers if (len(s.name) > s.years_UM)]

# Write a unit test that checks whether names_with_not_too_much_seniority is set correctly:
class Test_NotTooMuchSeniority(unittest.TestCase):
    def test_Problem7_TestOfLength(self):
        self.assertEqual(len(names_with_not_too_much_seniority), 4)
    def test_Problem7_TestAtIndex3(self):
        self.assertTrue(names_with_not_too_much_seniority[3] == "Euijin")

## [PROBLEM 8]
print "\n\n***** Problem 8 *****"
## The function below takes as input a list of integers, L. It returns an integer.
def good_cards(L):
    sum = 0
    c = 0
    to_return = []
    for card in L:
        sum += card
        c += 1
        if sum >= 21:
            break
    return c
## End provided code

# Write unit tests for the good_cards function here:
test = good_cards([10, 10, 1, 1])
test2 = good_cards([10, 10])
test3 = good_cards([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
test4 = good_cards([5, 5, 10, 5, 1])

class Test_BlackJack(unittest.TestCase):
    def test_Problem8_lenCardList(self):
        self.assertEqual(test, 3)
    def test_Problem8_lenCardList2(self):
        self.assertEqual(test2, 2)
    def test_Problem8_lenCardList3(self):
        self.assertEqual(test3, 21)
    def test_Problem8_lenCardList4(self):
        self.assertEqual(test4, 4)

## BELOW THIS LINE IS CODE THAT WILL RUN ANY UNIT TESTS YOU WRITE INSIDE THIS FILE. DO NOT WRITE CODE BELOW IT OR DELETE IT.
unittest.main(verbosity=2)
## END PROBLEM SET 8 FILE

