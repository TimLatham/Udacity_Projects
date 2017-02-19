import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Behavior:   Constructor for Movie class
        Inputs:     self: ability to reference self
                    movie_title: title of the movie_title
                    movie_storyline: in this case, a tagline of sorts for the movie_title
                    poster_image: a url link to an image of the movie poster
                    trailer_youtube: a url link to a youtube trailer for the movie
        Outputs:    None, but initializes the title, storyline, poster image and trailer for the movie object
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Behavior:   opens a web browser tab/window and plays the referenced trailer
        Inputs:     self
        Outputs:    None, takes the action in behavior
        """
        webbrowser.open(self.trailer_youtube_url)
