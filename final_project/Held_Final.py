# Marcy Held
# SI 506 - Final Project
# 13 Dec 2016

import requests
import json
import unittest

class Director():
	def __init__(self, movie_d):
		self.titleList = []
		for item in movie_d['results']:
			self.titleList.append(item['trackName'])

		self.genreList = []
		for item in movie_d['results']:
			self.genreList.append(item['primaryGenreName'])

		self.directorName = movie_d['results'][0]['artistName']

	def getGenreTypes(self):
		genre_dictionary = {}
		for item in self.genreList:
			if item not in genre_dictionary:
				genre_dictionary[item] = 1
			else:
				genre_dictionary[item] += 1
		return genre_dictionary

	def getMostCommonGenre(self):
		genre_d = Director.getGenreTypes(self)
		genre_keys = genre_d.keys()
		sorted_genres = sorted(genre_keys, key = lambda k:genre_d[k], reverse = True)
		return sorted_genres[0]

	def getDrinkKeyWord(self):
		genre_keyword = Director.getMostCommonGenre(self)

		if genre_keyword == 'Kids & Family':
			return 'Non-Alcoholic'
		elif genre_keyword == 'Comedy' or genre_keyword == 'Sports':
			return 'Lager'
		elif genre_keyword == 'Action & Adventure':
			return 'Whiskey'
		elif genre_keyword == 'Classics':
			return 'Gin'
		elif genre_keyword == 'Documentary' or genre_keyword == 'Independent':
			return 'Cider'
		elif genre_keyword == 'Drama':
			return 'Vodka'
		elif genre_keyword == 'Essentials':
			return 'Sparkling Wine'
		elif genre_keyword == 'Foreign':
			return 'Liqueur'
		elif genre_keyword == 'Horror':
			return 'Absinthe'
		elif genre_keyword == 'Music' or genre_keyword == 'Thriller':
			return 'Rum'
		elif genre_keyword == 'Romance':
			return 'Red Wine'
		elif genre_keyword == 'Sci-Fi & Fantasy' or genre_keyword == 'Western':
			return 'Stout'
		elif genre_keyword == 'Short Films':
			return 'Tequila'
		else:
			return 'Any'

	def __str__(self):
		s = 'The movies associated with ' + str(self.directorName) + ' are: ' + str(self.titleList) + '.\n\n'
		s = s + 'The genres associated with these movies are: ' + str(self.genreList) + '.\n\n'
		s = s + 'The genre that is most commonly associated with ' + self.directorName + ' is ' + str(Director.getMostCommonGenre(self)) + '.' + "\n"
		return s

class DrinkRecs():
	def __init__(self, drink_d):
		self.drinkNamesAndPrices = []
		for item in drink_d['result']:
			self.drinkNamesAndPrices.append((item['name'], item['price_in_cents']))

		self.primaryCategoryList = []
		for item in drink_d['result']:
			self.primaryCategoryList.append(item['primary_category'])

		self.secondaryCategoryList = []
		for item in drink_d['result']:
			self.secondaryCategoryList.append(item['secondary_category'])

	# return all drinks whose cost is over 5000 cents
	def getMostExpensiveDrinks(self):
		returnList = [d for d in self.drinkNamesAndPrices if d[1] > 5000]
		return returnList

	# return all drinks whose cost is below 2000 cents
	def getLeastExpensiveDrinks(self):
		returnList = [d for d in self.drinkNamesAndPrices if d[1] < 2000]
		return returnList

	def __str__(self):
		s = "The drink recommendations are as follows:\n\n"
		s = s + "The primary drink category is " + str(self.primaryCategoryList[0]) + ", and the secondary drink category is " + str(self.secondaryCategoryList[0]) + "\n"
		s = s + "Most expensive results (over $50): " + str(DrinkRecs.getMostExpensiveDrinks(self)) + "\n\n"
		s = s + "Least expensive results (under $20): " + str(DrinkRecs.getLeastExpensiveDrinks(self))
		return s

CACHE_FNAME = 'Held_cached_data.txt'

try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION = {}

def getiTunesWithCaching(directorName):
    BASE_URL = 'https://itunes.apple.com/search'
    full_url = requestURL(BASE_URL, params={'term': directorName, 'media': 'movie'})

    if full_url in CACHE_DICTION:
        print 'using cache'
        # use stored response
        response_text = CACHE_DICTION[full_url]
    else:
        print 'fetching'
        # do the work of calling the API
        response = requests.get(full_url)
        # store the response
        CACHE_DICTION[full_url] = response.text
        response_text = response.text 

        cache_file = open(CACHE_FNAME, 'w')
        cache_file.write(json.dumps(CACHE_DICTION))
        cache_file.close()

    response_dictionary = json.loads(response_text)
    return response_dictionary

def getLCBOWithCaching(drinkStr):
    BASE_URL = 'https://lcboapi.com/products'
    full_url = requestURL(BASE_URL, params={'access_key': '--LCBO KEY GOES HERE--', 'q': drinkStr}) #LCBO api access key goes here

    if full_url in CACHE_DICTION:
        print 'using cache'
        # use stored response
        response_text = CACHE_DICTION[full_url]
    else:
        print 'fetching'
        # do the work of calling the API
        response = requests.get(full_url)
        # store the response
        CACHE_DICTION[full_url] = response.text
        response_text = response.text

        cache_file = open(CACHE_FNAME, 'w')
        cache_file.write(json.dumps(CACHE_DICTION))
        cache_file.close()

    response_dictionary = json.loads(response_text)
    return response_dictionary

def canonical_order(d):
    alphabetized_keys = sorted(d.keys())
    res = []
    for k in alphabetized_keys:
        res.append((k, d[k]))
    return res

def requestURL(baseurl, params = {}):
    req = requests.Request(method = 'GET', url = baseurl, params = canonical_order(params))
    prepped = req.prepare()
    return prepped.url

wes_dictionary = getiTunesWithCaching('Wes Anderson')
tar_dictionary = getiTunesWithCaching('Quentin Tarantino')
pta_dictionary = getiTunesWithCaching('Paul Thomas Anderson')
hitch_dictionary = getiTunesWithCaching('Alfred Hitchcock')

wes_movies = Director(wes_dictionary)
tar_movies = Director(tar_dictionary)
pta_movies = Director(pta_dictionary)
hitch_movies = Director(hitch_dictionary)

print "********** printing info for Wes Anderson **********"
print wes_movies
print "The drink keyword associated with Wes Anderson is: " + str(wes_movies.getDrinkKeyWord())
wes_drinks = DrinkRecs(getLCBOWithCaching(wes_movies.getDrinkKeyWord()))
print wes_drinks
print "\nEnjoy these drinks while watching a movie by " + wes_movies.directorName + "!\n"

print "********** printing info for Quentin Tarantino **********"
print tar_movies
print "The drink keyword assoicated with Quentin Tarantino is: " + str(tar_movies.getDrinkKeyWord())
tar_drinks = DrinkRecs(getLCBOWithCaching(tar_movies.getDrinkKeyWord()))
print tar_drinks
print "\nEnjoy these drinks while watching a movie by " + tar_movies.directorName + "!\n"

print "********** printing info for Paul Thomas Anderson **********"
print pta_movies
print "The drink keyword associated with Paul Thomas Anderson is: " + str(pta_movies.getDrinkKeyWord())
pta_drinks = DrinkRecs(getLCBOWithCaching(pta_movies.getDrinkKeyWord()))
print pta_drinks
print "\nEnjoy these drinks while watching a movie by " + pta_movies.directorName + "!\n"

print "********** printing info for Alfred Hitchcock **********"
print hitch_movies
print "The drink keyword associated with Alfred Hitchcock is: " + str(hitch_movies.getDrinkKeyWord())
hitch_drinks = DrinkRecs(getLCBOWithCaching(hitch_movies.getDrinkKeyWord()))
print hitch_drinks
print "\nEnjoy these drinks while watching a movie by " + hitch_movies.directorName + "!"

print "\n\n********** Begin Unit Tests **********"
class TestingiTunesCaching(unittest.TestCase):
	def test_Director_typeTitleList(self):
		self.assertEqual(type(tar_movies.titleList), type([]))
	def test_Director_typeGetGenreType(self):
		self.assertEqual(type(wes_movies.getGenreTypes()),type({}))
	def test_Director_typeGetDrinkKeyword(self):
		self.assertEqual(type(hitch_movies.getDrinkKeyWord()),type(""))
	def test_Director_drinkKeyword(self):
		self.assertEqual(pta_movies.getDrinkKeyWord(), 'Vodka')
	def test_Director_drinkKeyword2(self):
		self.assertEqual(wes_movies.getDrinkKeyWord(), 'Lager')
	def test_Director_mostCommonGenre(self):
		self.assertEqual(wes_movies.getMostCommonGenre(), 'Comedy')
class TestingLCBOCaching(unittest.TestCase):
	def test_typeLeastExpensiveDrinksList(self):
		self.assertEqual(type(wes_drinks.getLeastExpensiveDrinks()), type([]))
	def test_priceOfMostExpensiveDrinks(self):
		self.assertTrue(tar_drinks.getMostExpensiveDrinks()[0][1] > 5000)


unittest.main(verbosity=2)