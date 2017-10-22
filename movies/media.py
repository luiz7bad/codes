import webbrowser
#create a class
class Movie():
	#class variable, belongs to the classe not the instance
	#defined before the init method
	#the instances dont have access to it.
	VALID_RATINGS = ['G', 'PG']
	#defines the initial constructor to reserve memory space
	#for the new instance using the keyword __init__ 
	#init needs the arguments, necessary the first is self
	#self refers always to the instance, without self the variable is just accessible
	#in the upper class
	def __init__(self, movie_title, movie_storyline, poster_image, trailer):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)