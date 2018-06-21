'''Defining the class Movie for the file '''
import webbrowser

class Movie(): 
    '''Funcction __init__ create space in memory for the new instances.'''
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        '''Instance variables where we want to store information for our
        objects(movies) created in entertainment_center.'''
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    '''Instance method that opens the brawser to show the trailer of 
        the movie.'''

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
 
