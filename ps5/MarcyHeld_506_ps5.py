# Problem Set 5
# SI 106

# Marcy Held 
# October 14, 2016

# These import statements are necessary for the tests to run in your code. Do not change them!
import unittest

##########

## [PROBLEM 1] 

fall_list = ["leaves","apples","autumn","bicycles","pumpkin","squash","excellent"]

sorted_fall_list = sorted(fall_list, reverse = True)


## [PROBLEM 2]

food_amounts = [{"sugar_grams":245,"carbohydrate":83,"fiber":67},{"carbohydrate":74,"sugar_grams":52,"fiber":26},{"fiber":47,"carbohydrate":93,"sugar_grams":6}]

sorted_sugar = sorted(food_amounts, key = lambda d: d["sugar_grams"])

raw_carb_sort = sorted (food_amounts, key = lambda d: (d["carbohydrate"] - d["fiber"]))

## [PROBLEM 3]
# Worked with Meg Green on this problem: 10/13/16
# Write code here.
fname = 'words.txt'
f = open(fname, 'r')
words = f.read()

short_z_words = []

for word in words.split():
  if len(word) == 3:
    if 'z' in word:
      short_z_words.append(word)

short_z_words = sorted(short_z_words, reverse = True)

f.close()


## [PROBLEM 4]
fname = 'words.txt'
f = open(fname, 'r')
words = f.read()

all_words_with_z = []

for word in words.split():
  if 'z' in word:
    all_words_with_z.append(word)

letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}

# make a list of tuples!
# each item in z_scores list is a tuple
# tuple[0] is the word, tuple[1]
z_scores = []

for word in all_words_with_z:
  word_score = 0
  for letter in word:
    word_score += letter_values[letter]
  z_scores.append((word, word_score))


ordered_z_scores = sorted(z_scores, key = lambda item: item[1], reverse = True)

top_ten = ordered_z_scores[:10]

best_z_words = []

for item in top_ten:
  best_z_words.append(item[0])


## [PROBLEM 5]

nl = [["nested","data","is"],["really","fun"],[11,["hooray","hooray"],"yay"]]

second_elems = []

for item in nl:
  second_elems.append(item[1])

## [PROBLEM 6]

# Define your function here. 
## NOTE: It should be called convert_nums, NOT convert_times. Instructions are being updated in the textbook to reflect this.

def convert_nums(hrs):
  return (hrs * 60, hrs * 3600)


## [PROBLEM 7]

# First, we suggest you look through the data structure saved in the variable fb_data to get a sense for it. Below, write code to solve the problems.

fb_data = {
 "data": [
  {
    "id": "2253324325325123432madeup", 
    "from": {
      "id": "23243152523425madeup", 
      "name": "Jane Smith"
    }, 
    "to": {
      "data": [
        {
          "name": "Your Facebook Group", 
          "id": "432542543635453245madeup"
        }
      ]
    }, 
    "message": "This problem might use the accumulation pattern, like many problems do", 
    "type": "status", 
    "created_time": "2014-10-03T02:07:19+0000", 
    "updated_time": "2014-10-03T02:07:19+0000"
  }, 
 
  {
    "id": "2359739457974250975madeup", 
    "from": {
      "id": "4363684063madeup", 
      "name": "John Smythe"
    }, 
    "to": {
      "data": [
        {
          "name": "Your Facebook Group", 
          "id": "432542543635453245madeup"
        }
      ]
    }, 
    "message": "Here is a fun link about programming", 
    "type": "status", 
    "created_time": "2014-10-02T20:12:28+0000", 
    "updated_time": "2014-10-02T20:12:28+0000"
  }]
}

## Write your code for problem 7 here.

first_message = fb_data["data"][0]["message"]

second_name = fb_data["data"][1]["from"]["name"]


## [PROBLEM 8]

## Define your function sort_nested_lists here.

def sumfunc (numlist):
  total = 0
  for num in numlist:
    total += num

  return total

def sort_nested_lists (list_input):

  return sorted(list_input, key = sumfunc)


############# BELOW THIS LINE IS CODE FOR PROBLEM SET TESTS #####################
################### DO NOT CHANGE CODE BELOW THIS LINE ##########################
class Problem1(unittest.TestCase):

    def test1(self):
        self.assertEqual(sorted_fall_list, ['squash', 'pumpkin', 'leaves', 'excellent', 'bicycles', 'autumn', 'apples'], "sorted_fall_list is not accurately sorted")

class Problem2(unittest.TestCase):
    
    def test2(self):
        self.assertEqual(sorted_sugar,[{'carbohydrate': 93, 'fiber': 47, 'sugar_grams': 6}, {'carbohydrate': 74, 'fiber': 26, 'sugar_grams': 52}, {'carbohydrate': 83, 'fiber': 67, 'sugar_grams': 245}])
    def test3(self):
        self.assertEqual(raw_carb_sort,[{'carbohydrate': 83, 'fiber': 67, 'sugar_grams': 245}, {'carbohydrate': 93, 'fiber': 47, 'sugar_grams': 6}, {'carbohydrate': 74, 'fiber': 26, 'sugar_grams': 52}])

class Problem3(unittest.TestCase):

    def test4(self):
        self.assertEqual(short_z_words,['zoo', 'zoa', 'zit', 'zip', 'zig', 'zek', 'zee', 'zed', 'zax', 'zap', 'zag', 'wiz', 'lez', 'fiz', 'fez', 'coz', 'biz', 'azo', 'adz'], "short_z_words does not have the correct value")


class Problem4(unittest.TestCase):
    
    def test5(self):
        self.assertEqual(sorted(best_z_words)[:9],sorted(['zyzzyvas', 'zyzzyva', 'pizazzy', 'bezazzes', 'jazzlike', 'pazazzes', 'pizazzes', 'quizzing', 'zizzling', 'bezazz'])[:9],"best_z_words does not have the correct value")

class Problem5(unittest.TestCase):
    
    def test6(self):
        self.assertEqual(second_elems, ['data', 'fun', ['hooray', 'hooray']], "second_elems does not have the correct value")

class Problem6(unittest.TestCase):
    
    def test7(self):
       self.assertEqual(convert_nums(1),(60,3600),"incorrect output of function with input 1")
       self.assertEqual(convert_nums(50),(60*50,3600*50), "incorrect output of function with input 50")
       self.assertEqual(convert_nums(0), (0,0), "incorrect output of function with input 0")

class Problem7(unittest.TestCase):
    
    def test8(self):
        self.assertEqual(first_message, "This problem might use the accumulation pattern, like many problems do")
    def test9(self):
        self.assertEqual(second_name,"John Smythe")

class Problem8(unittest.TestCase):

    def test10(self):
        self.assertEqual(sort_nested_lists([[2,3],[45,100,2],[536],[103,2,8]]),[[2,3],[103,2,8],[45,100,2],[536]],"testing a case of a sorted nested list -- check out your function output")
        self.assertEqual(sort_nested_lists([[1],[50],[6]]),[[1],[6],[50]],"testing a case of a sorted nested list -- check out your function output")
        self.assertEqual(sort_nested_lists([[],[1]]),[[],[1]],"testing a case of a sorted nested list -- check out your function output")
        self.assertEqual(sort_nested_lists([[0],[-4,-5,-7],[-56,4]]),[[-56,4],[-4,-5,-7],[0]],"testing a case of a sorted nested list -- check out your function output")

if __name__ == '__main__':
    unittest.main(verbosity=2)
