import time
import webbrowser


for i in range(3):
# function to get the current time
	print time.ctime()
#function to make a program or function wait a given time in seconds
#to start afterit have being executed.
	time.sleep(15)
#Native python function to open a webbrowser in a pre-set page.
	webbrowser.open("https://www.youtube.com/watch?v=1CvC-3smmts&t=304s")