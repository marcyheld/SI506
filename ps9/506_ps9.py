## 506 PS 9 draft

# Marcy Held
# 19 Nov 2016
# PS 9

# import statements
import unittest
import requests
import json
from pprint import pprint

### The following code makes lists of positive words and negative words, saving them in the variables pos_ws and neg_ws. DO NOT CHANGE THIS CODE. You'll need it later!
pos_ws = []
f = open('positive-words.txt', 'r')

for l in f.readlines()[35:]:
    pos_ws.append(unicode(l.strip()))
f.close()

neg_ws = []
f = open('negative-words.txt', 'r')
for l in f.readlines()[35:]:
    neg_ws.append(unicode(l.strip()))

### END PROVIDED CODE

# [PROBLEM 1]
print "\n\n***** Problem 1 *****"

## Fill in the missing parts of class Post per the instructions in the textbook. 

class Post():
    """object representing status update"""
    def __init__(self, post_dict={}):
        if 'message' in post_dict:
            self.message = post_dict['message']
        else:
            self.message = ""

        if 'comments' in post_dict:
            self.comments = post_dict['comments']['data']
        else:
            self.comments = []

        if 'likes' in post_dict:
            self.likes = post_dict['likes']['data']
        else:
            self.likes = []
        
    def positive(self):
        posNum = 0
        for word in self.message.split(): # creates list where each item is one word in the message, if we didn't do this we would iterate through each character in the string...
            if word in pos_ws:
                posNum += 1

        return posNum
                   
    def negative(self):
        negNum = 0
        for word in self.message.split(): # creates list where each item is one word in the message
            if word in neg_ws:
                negNum += 1

        return negNum

    def emo_score(self):

        return self.positive() - self.negative()

## [PROBLEM 2]
print "\n\n***** Problem 2 *****"
## This code is provided so you can use it in the problem set. Do not change it!
## You should answer the question about it on the textbook assignment, too.
sample = open('samplepost.txt').read()
sample_post_dict = json.loads(sample)
p = Post(sample_post_dict)
## End provided code

## Now, if you want, uncomment and run the next lines of code if you're having trouble getting the tests for the above problem to pass. The output from this code may help you understand what a post_dict contains, and what your code has actually extracted from it and assigned to the comments and likes instance variables.

# print "sample_post_dict\n", pprint(sample_post_dict)
# print "the comments in one Post instance\n", pprint(p.comments)
# print "the likes in one Post instance\n", pprint(p.likes)

## [PROBLEM 3]
print "\n\n***** Problem 3 *****"

## Fill in your access token (in quotes, because it's a string) in the code if you don't want to have to paste it every time you run the program (but you'll have to replace it every couple hours).

access_token = "-- V2.5 ACCESS TOKEN HERE --"

####The following code allows us to grade your code with graders' tokens. (It also helps you run the code if your access token has expired.) Please do not change it! 
r = requests.get("https://graph.facebook.com/v2.5/me/feed",params={"limit":2, "access_token":access_token})
# print r.status_code
if r.status_code != 200:
    access_token = raw_input("Get a Facebook access token v2.5 from https://developers.facebook.com/tools/explorer, making sure to check all items in 'Select Permissions' window and enter it here if the one saved in the file doesn't work anymore.  :\n")

## This global variable holds the group id for our class Facebook group.
#GROUP_ID = "2201523684" #SOCHI group id
GROUP_ID = "323187111349524" #506 group id

#### End provided code

## Baseurl for the Facebook API
## Remember to replace "me" with the GROUP ID value if you want data from the class FB group 
# baseurl = "https://graph.facebook.com/v2.5/" + GROUP_ID + "/feed"  # changed version from 2.3 to 2.5 on 02/25/2018
baseurl = "https://graph.facebook.com/v2.5/me/feed" # changed version from 2.3 to 2.5 on 02/25/2018

# Building the Facebook parameters dictionary
url_params = {}
url_params["access_token"] = access_token
url_params["fields"] = "comments{comments{like_count,from,message,created_time},like_count,from,message,created_time},likes,message,created_time,from" # Parameter key-value so you can get post message, comments, likes, etc. as described in assignment instructions.

# Write code to make a request to the Facebook API using paging and save data in fb_data here.

fb_response = requests.get(baseurl, params=url_params)
fb_data = fb_response.json()

# print type(fb_data['data'])
# print len(fb_data['data'])

next_url = fb_data['paging']['next']

for i in range(7):
    #print "entering for loop"
    new_fb_response = requests.get(next_url)
    new_fb_data = new_fb_response.json()

    #print new_fb_data

    fb_data['data'] = fb_data['data'] + new_fb_data['data']
    #print new_fb_data.keys()
    if len(new_fb_data.keys()) == 2:
        next_url = new_fb_data['paging']['next']
        #print next_url
    #print "at end of for loop"

## [PROBLEM 4]
print "\n\n***** Problem 4 *****"
    
# Write your list comprehension here:

post_insts = [Post(item) for item in fb_data['data']]
# print type(post_insts)
# print type(post_insts[0])

#print post_insts[0].comments[0]['created_time']

## [PROBLEM 5]
print "\n\n***** Problem 5 *****"

# Write code to collect top commenters and top likers here.
# Top likers
likes_count = {}

for obj in post_insts:
    for like in obj.likes:
        if like['name'] not in likes_count:
            likes_count[like['name']] = 0
        likes_count[like['name']] += 1

#print likes_count

sorted_likes = sorted(likes_count.keys(), key = lambda k: likes_count[k], reverse = True)
#print sorted_likes

top_likers = sorted_likes[:3]
#print top_likers

#Top commenters
comments_count = {}

for obj in post_insts:
    for comment in obj.comments:
         if comment['from']['name'] not in comments_count:
             comments_count[comment['from']['name']] = 0
         comments_count[comment['from']['name']] += 1

#print comments_count

sorted_comments = sorted(comments_count.keys(), key = lambda k: comments_count[k], reverse = True)

top_commenters = sorted_comments[:3]
#print top_commenters


## [PROBLEM 6]
print "\n\n***** Problem 6 *****"

# Define your function here.
def unique_facebookers(postList):
    #make a list of unique commenters, use length of that list
    unique_commenters_list = []
    unique_likers_list = []
    for item in postList:
        for comment in item.comments:
            if comment['from']['name'] not in unique_commenters_list:
                unique_commenters_list.append(comment['from']['name'])

    for item in postList:
        for like in item.likes:
            if like['name'] not in unique_likers_list:
                unique_likers_list.append(like['name'])

    if len(unique_commenters_list) > len(unique_likers_list):
        return "commenters"
    elif len(unique_likers_list) > len(unique_commenters_list):
        return "likers"
    else:
        return "equal"

#print unique_facebookers(post_insts)
  
## [PROBLEM 7]
print "\n\n***** Problem 7 *****"
# Write code to create your emo_scores.csv file here!
outfile = open("emo_scores.csv", "w")
outfile.write("emo score, comment counts, like counts\n")
for post in post_insts:
    outfile.write(("{}, {}, {}\n").format(post.emo_score(), len(post.comments), len(post.likes)))

outfile.close()

##### TESTS BELOW, DO NOT CHANGE #########
class Problem1(unittest.TestCase):
    def test_instvar_1(self):
        self.assertEqual(type(p.comments), type([]), "testing type of p.comments")
    def test_instvar_2(self):
        self.assertEqual(len(p.comments), 4, "testing length of p.comments")
    def test_instvar_3(self):
        self.assertEqual(type(p.comments[0]), type({}), "testing type of p.comments[0]")
    def test_instvar_4(self):
        self.assertEqual(type(p.likes), type([]), "testing type of p.likes") 
    def test_instvar_5(self):       
        self.assertEqual(len(p.likes), 4, "testing length of p.likes")
    def test_instvar_6(self):
        self.assertEqual(type(p.likes[0]), type({}), "testing type of p.likes[0]")
    def test_method_1(self):
        p.message = "adaptive acumen abuses acerbic aches for everyone"
        self.assertEqual(p.positive(), 2, "testing return value of .positive()")
    def test_method_2(self):
        p.message = "adaptive acumen abuses acerbic aches for everyone"
        self.assertEqual(p.negative(), 3, "testing return value of .negative()")
    def test_method_3(self):
        p.message = "adaptive acumen abuses acerbic aches for everyone"
        self.assertEqual(p.emo_score(), -1, "testing return value of .emo_score()")

class Problem3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(type(fb_data),type({}),"testing type of fb_data")
    def test_1(self):
        self.assertEqual(type(fb_data["data"]),type([]), "testing type of the data key in fb_data, and that fb_data has a key data")

class Problem4(unittest.TestCase):
    def test_1(self):
        self.assertEqual(type(post_insts), type([]), "testing that post_insts is a list")
    def test_2(self):
        self.assertTrue(len(post_insts) > 0)
    def test_3(self):
        self.assertIsInstance(post_insts[1], Post, "Testing that elements of post_insts are  Post instances")

class Problem5(unittest.TestCase):
    def test_1(self):
        self.assertEqual(len(top_commenters),3,"Testing that there are 3 elements in top_commenters")
    def test_2(self):
        self.assertEqual(type(top_commenters[1]),type(u""), "Testing that elements of top_commenters are Unicode strings (should be strings of the commenters' names -- note that you'll have to judge whether they're the correct names)")
    def test_3(self):
        self.assertEqual(len(top_likers),3,"Testing that there are 3 elements in top_likers")
    def test_2(self):
        self.assertEqual(type(top_likers[1]),type(u""), "Testing that elements of top_likers are Unicode strings (should be strings of the likers' names -- note that you'll have to judge whether they're the correct names)")

class Problem6(unittest.TestCase):
    def test_1(self):
        pi = [p] # list of one post
        self.assertEqual(unique_facebookers(pi),"likers", "Testing that the unique_facebookers function returns 'likers' in an appropriate scenario")

unittest.main(verbosity=2)