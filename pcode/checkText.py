import urllib
def read_text():
	#open opens the document to be read
	quotes = open("/Users/Luiz/desktop/python/movie_quotes.txt")
	#function reads, read the document
	content = quotes.read()
	#close the opened document
	quotes.close()
	check_profanity(content)
def check_profanity(texto):
	#function to open a url, in this case passing the argument to be checked
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+texto)
	#returns the output 
	output = connection.read()
	print output
	connection.close()
read_text()