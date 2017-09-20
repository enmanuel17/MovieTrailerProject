#Enmanuel Hernandez
#Movie trailer project.


# These are the links to the githubs of the APIs I am using:
# For tmdbsimple:
# https://github.com/celiao/tmdbsimple.git
# For tmdb3:
# https://github.com/celiao/tmdbsimple.git

# libraries:
# Udacity
# https://github.com/udacity/ud036_StarterCode.git

#Imports the two APIs I need to query the movie IDs and create image urls and trailers.
#####################################################
import tmdbsimple as tmdb
tmdb.API_KEY = '6178322d2a44fe7cbef43f2bad94bd6e'
import tmdb3
from tmdb3 import set_key
set_key('6178322d2a44fe7cbef43f2bad94bd6e')
from tmdb3 import searchMovie, Movie
#Makes the API work on windows
tmdb3.set_cache('null')
######################################################
#imports the local libraries
import media
import fresh_tomatoes

#Gets the ID from all the movies I want
#######################################################################################
#Stores all the movies I want to display
movies = ['300', 'The avengers ultron', 'iron man', 'skyfall', 'dark knight rises', 'logan', 'the pursuit of happy', 'Dirty Grandpa', 'alien covenant', 'A dogs purpose', 'stand and deliver', 'thor']
#movies = ['iron man 3','thor 2']
#Initializes the tmbd search method
search = tmdb.Search()
#Counter to determine the amount of times the while loop has to run.
numMovie = len(movies)
#Array to store the ID of each movie
mID = []
#counter to stop the loop
counter = len(mID)

while (counter < numMovie):
	for m in movies:
		movie = search.movie(query= m)
		result = search.results[0]
		#print result['id']
		movieID = result['id']
		mID.insert(counter,movieID)
		counter = counter + 1

################################################################################################

#Finds each movie by using the ID and creates an Movie Object for each movie then
#inserts each movie object into an array
################################################################################################
#Arrat that hols each movie object
movieArray = []
#Counting the number of movies for the while loop
numMovie = len(mID)
#counter
counter = len(movieArray)
#loop that insert each movie object into an array
while (counter < numMovie):
	#For each id inside the ID array, create a Movie object with the class from the API tmdb3
	for s in mID:
		res = Movie(s)
		#array of movie objects
		movieArray.insert(counter,res) 
		counter = counter + 1

##################################################################################################

#By using each movie object from the array MovieArray, we are able to extract only the data for the four attributes we need.
#These attributes are title, overview, poster url, trailer url. 
#We then pass these attributes to create instance of the Media.Movie class.
#We then insert each Media.Movie instance into an array for future use.
###################################################################################################################
#array that hold the media.py objects
mediaArray = []
counter = 0
#loops that creates an media object with four attributes extracted and passed onto the media.Movie class to create instances
while (counter < numMovie):
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