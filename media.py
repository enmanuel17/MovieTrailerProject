#Enmanuel Hernandez
#Creates a class for storing movie information in an organize form.


import webbrowser

#A class that has four attributes and a method to provide information about the objects.
class Movie():
	"""This class provides a way to store movie related information"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	#Method to open a web browser with the trailer of the movie
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
	
