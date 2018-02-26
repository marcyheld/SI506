import unittest
import requests 
import json

# Marcy Held
# F16 - SI 506
# PS 6
# 29 Oct 2016

# This is a function we've provided for you so you can print stuff 
# in a pretty, easy-to-read way. 
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)



## [PROBLEM 1] Encoding query parameters in a URL

## Create your dictionary called url_parameters here:

url_parameters = {'format':'json'}


## [PROBLEM 2] Making a request and saving the response object

## Write the assignment statement that makes a request to the FAA API here.
## Save it in the variable airport_response.
## Here is the code we've provided for you to use.
baseurl = 'http://services.faa.gov/airport/status/'
airport = 'DTW'
# Write your line of code below:

airport_response = requests.get(baseurl + airport, params = url_parameters)


## [PROBLEM 3] Grabbing data off the web

## Put your try/except clause code here, following the directions in the assignment. You should be using the .json() method and saving a dictionary in a variable airport_data (as long as you can, that is).
try:
    airport_response = requests.get(baseurl + airport, params = url_parameters)
    airport_data = airport_response.json()
except Exception:
    print "That didn't work."

#print pretty(airport_data)

## [PROBLEM 4] Extracting relevant information from a dictionary

## Write code to extract data and save it in variables here.
airport_code = airport_data["IATA"]

status_reason = airport_data["status"]["reason"]

current_temp = airport_data["weather"]["temp"]

recent_update = airport_data["weather"]["meta"]["updated"]

# print pretty(airport_data) # uncomment this to see what the dictionary you saved in airport_data looks like
## Uncomment the following lines if you want to see the printed reps of what's in these variables.
# print airport_code
# print status_reason
# print current_temp
# print recent_update


## [PROBLEM 5] Generalizing your code

## Define your get_airport function here.
## Remember not to depend on any global variables in this file.
## (You do NOT need to put any try/except clause inside this function -- we'll get there!)
def get_airport(airport_code):
    baseurl = 'http://services.faa.gov/airport/status/'
    url_parameters = {'format':'json'}

    airport_response = requests.get(baseurl + airport_code, params = url_parameters)
    airport_data = airport_response.json()

    return airport_data


## [PROBLEM 6] More code generalization

## Define your extract_airport_data function here.

def extract_airport_data(airport_code):
    airport_data = get_airport(airport_code)

    return (airport_data["IATA"], airport_data["status"]["reason"], airport_data["weather"]["temp"], airport_data["weather"]["meta"]["updated"])


## [PROBLEM 7] Create examples of using your newly defined functions

fav_airports = ['PIT', 'BOS', 'LGA', 'DCA']
## Write your code here:
for airport in fav_airports:
    print extract_airport_data(airport)

## [PROBLEM 8] Error handling and exceptions

## Here is the request to a bogus airport.
## Write a try/except clause to handle it properly. 
## Should print "Sorry, that didn't work" if it didn't work.

try: 
    print extract_airport_data("XYZ") # You will get an error when you uncomment this line. Your goal is to make it OK!
except Exception:
    print "Sorry, that didn't work."

## The following line of code should run no matter what. Do not change this.
print "Done trying that XYZ airport."


## [PROBLEM 9] Dealing with real live data

possible_airports = ["LAX","PHX","PPT","BOS","JAC","PDX","DTW"]

## Write the rest of your code for this problem here:

for airport in possible_airports:
    try:
        print extract_airport_data(airport)
    except Exception:
        print "Failed for airport " + airport


## [PROBLEM 10] Using real live data to write a CSV file!

## Write your code to write your CSV file here.
## Remember that the file you create should be called: airport_temps.csv !

new_file_ref = open("airport_temps.csv", "w")
new_file_ref.write("airport_code, status_reason, current_temp, recent_update\n")

for airport in possible_airports:
    try:
        airport_code, status_reason, current_temp, recent_update = extract_airport_data(airport)
        new_file_ref.write(airport_code + ',' + status_reason + ',' + current_temp + ',' + recent_update + '\n')
    except Exception:
        print "Failed for airport " + airport

new_file_ref.close()


## When you're finished, upload your 506_ps6.py file to Canvas. Please don't upload your CSV -- your code should generate that when we run it!

############# BELOW THIS LINE IS CODE FOR PROBLEM SET TESTS #####################
################### DO NOT CHANGE CODE BELOW THIS LINE ##########################

class Problem1And2(unittest.TestCase):

    def test1(self):
        self.assertEqual(url_parameters,{"format":"json"},"Make sure you have the correct dictionary saved in url_parameters")
    def test2(self):
        self.assertEqual(type(airport_response),type(requests.get("http://www.google.com")),"airport_response is not a response object, check out what's being assigned to it")


class Problem4(unittest.TestCase):
    
    def test3(self):
        self.assertEqual(airport_code,airport_data["IATA"],"airport_code does not have the correct value, OR you have a problem with your airport_data variable. Check out what's going on.")
        self.assertEqual(status_reason, airport_data["status"]["reason"],"status_reason does not have the correct value, OR you have a problem with your airport_data variable. Check out what's going on.")
        self.assertEqual(current_temp,airport_data["weather"]["temp"],"current_temp does not have the correct value, OR you have a problem with your airport_data variable. Check out what's going on.")
        self.assertEqual(recent_update,airport_data["weather"]["meta"]["updated"],"recent_update does not have the correct value, OR you have a problem with your airport_data variable. Check out what's going on.")

class Problem5And6(unittest.TestCase):
    def test4(self):
        self.assertEqual(type(get_airport("DTW")),type({}),"get_airport does not return a dictionary")
    def test5(self):
        self.assertEqual(get_airport("DTW")["IATA"],u"DTW","get_airport does not return all of the right data -- check it out")
    def test6(self):
        self.assertEqual(type(extract_airport_data("DTW")),type((1,2,3,4)),"extract_airport_data does not return a tuple")
        self.assertEqual([type(extract_airport_data("DTW")[0]),type(extract_airport_data("DTW")[1]), type(extract_airport_data("DTW")[2]), type(extract_airport_data("DTW")[3])], [type(u""),type(u""),type(u""),type(u"")], "Check out the return value of extract_airport_data. Is it a tuple of strings?")
        self.assertEqual(extract_airport_data("SFO")[0],u"SFO","check what your extract_airport_data function returns!")
    def test7(self):
        print "Printing the result of your extract_airport_data function because it's live data:"
        print extract_airport_data("PHX")


class Problem7Plus(unittest.TestCase):
    print "Some of these tasks can't be tested due to it being live data."
    print "Overall, check to ensure your output is what the directions say it should be!"


if __name__ == '__main__':
    unittest.main(verbosity=2)

