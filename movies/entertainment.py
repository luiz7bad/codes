import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story','Toys get alive',
	'http://www.impawards.com/1995/posters/toy_story_ver1.jpg',
	'https://www.youtube.com/watch?v=4KPTXpQehio')


avatar = media.Movie('Avatar','qlqr coisa','blah blah', 'youtube')

movies = [toy_story, avatar]
# fresh_tomatoes.open_movies_page(movies)

#call the class variable valid_ratings
print media.Movie.VALID_RATINGS