'''Creating 6 instances or objects of the class Movie that is defined in
media file'''

import fresh_tomatos
import media

'''Giving argunments to the instances so the funcction can be initialize'''  
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie('Avatar',
                     'A marine on an alien palent',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

the_conjuring = media.Movie("The Conjuring",
                            "A family living in a hounted house story",
                            "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg",
                            "https://www.youtube.com/watch?v=k10ETZ41q5o")

avengers = media.Movie('The Avengers',
                       'Superheros fighting Loki',
                       'https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg',
                       'https://www.youtube.com/watch?v=eOrNdBpGMv8')

maze_runner = media.Movie('The Maze Runner',
                          'Kids traped in maze trying to fine an exit',
                          'https://upload.wikimedia.org/wikipedia/en/b/be/The_Maze_Runner_poster.jpg',
                          'https://www.youtube.com/watch?v=AwwbhhjQ9Xk')

black_panther = media.Movie('Black Panther',
                            'Superhero balck panther',
                            'https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg',
                            'https://www.youtube.com/watch?v=xjDjIWPwcPU')

'''List of movies to be able to open_movies_page'''
movies = [toy_story, avatar, the_conjuring, avengers, maze_runner, black_panther]

'''Fresh_tomatos file to open a movie website wiht the list of movies'''
fresh_tomatos.open_movies_page(movies)
