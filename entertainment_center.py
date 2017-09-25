# Enmanuel Hernandez
# Movie trailer project.

#  These are the links to the githubs of the APIs I am using:
#  For tmdbsimple:
#  https://github.com/celiao/tmdbsimple.git
#  For tmdb3:
#  https://github.com/celiao/tmdbsimple.git

#  Libraries:
#  Udacity
#  https://github.com/udacity/ud036_StarterCode.git

#Imports the local libraries
import media
import fresh_tomatoes

#Stores the key for query the themoviedb.org API with the wrappers.
API_Key = "6178322d2a44fe7cbef43f2bad94bd6e"

#Imports the two API wrappers I need to query the movie IDs and create image urls and trailers.
#Imports the API that has a search function and uses a key get allow my query it.
#The tmdbsimple API has facilitates using keywords for searching movies and returns a movie ID.
import tmdbsimple as tmdb
tmdb.API_KEY = API_Key

#Imports the API that allow me to get all the attributes of a movie by using the Movie ID.
import tmdb3
from tmdb3 import set_key
set_key(API_Key)
from tmdb3 import searchMovie, Movie
#Makes the API work on windows. For some reason windows has a permission issue with caching.
tmdb3.set_cache('null') 

#Creates an array that stores a keyword for each movie we are trying to find.
movies = ['300', 'The avengers ultron', 'iron man', 'skyfall', 'dark knight rises', 'logan', 'the pursuit of happy', 'Dirty Grandpa', 'alien covenant', 'A dogs purpose', 'stand and deliver', 'thor']

#Initializes the tmbd search method
search = tmdb.Search()
#Counter to determine the amount of times the while loop has to run.
numMovie = len(movies)
#Array to store the ID of each movie
mID = []
#Counter to stop the while loop
counter = len(mID)
#This loops runs till the counter variable is greater than the number of movies in the array Movies "numMovie".
while (counter < numMovie):
	#For each keyword (m) in the array of movies "movie", search for a movie that matches the keyword.
	#Store the first match from all the results [0]. We only want the first match because that is the one thats most likely to be accurate. 
	#From the first result, extract the ID of the movie 'id'
	#Store the ID of the movie into the array mID.
	for m in movies:
		movie = search.movie(query= m)
		result = search.results[0]
		#print result['id']
		movieID = result['id']
		mID.insert(counter,movieID)
		#Increments the counter to eventually make the while loop exit.
		counter = counter + 1

#Array that will hold each movie object
movieArray = []
#Counter to determine the amount of times the while loop has to run.
numMovie = len(mID)
#Counter top stop the while loop.
counter = len(movieArray)
#This loops till the counter variable is greater than the number of movies in the array of movies "numMovie".
while (counter < numMovie):
	#For each movie ID inside the mID array, create a Movie object with the class from the API tmdb3 "Movie(s)"
	#Store the object in the variable res.
	#The insert each object into the array movieArray.
	for s in mID:
		res = Movie(s)
		#array of movie objects
		movieArray.insert(counter,res) 
		#Increments the counter to eventually make the while loop exit.
		counter = counter + 1


#By using each movie object from the array MovieArray, we are able to extract only the data for the four attributes we need.
#These attributes are title, overview, poster url, trailer url. 
#We then pass these attributes to create instance of the Media.Movie class.
#We then insert each Media.Movie instance into an array for future use.
###################################################################################################################

#Array that will hold the objects created with the media.py class.
mediaArray = []
#Counter top stop the while loop.
counter = 0
#loops that creates an media object with four attributes extracted and passed onto the media.Movie class to create instances
while (counter < numMovie):
	#
	mediaObject = media.Movie(
		movieArray[counter].title,
		movieArray[counter].overview,
		movieArray[counter].poster.geturl(),
		movieArray[counter].youtube_trailers[0].geturl()
		)
	mediaArray.insert(counter,mediaObject)
	counter = counter + 1
####################################################################################################################

#Class the funtion that creaets the html website and it give it an array of media Objects.
fresh_tomatoes.open_movies_page(mediaArray)