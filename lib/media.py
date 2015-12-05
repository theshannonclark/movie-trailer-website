import fresh_tomatoes as ft

class MovieEssence():
    """Essence class for constructing movies

    Attributes:
        title: the title of the movie
        release_year: the year the movie was first released
        poster_image_url: the url of the poster image
        trailer_youtube_url: the url of the trailer on youtube
    """

    def __init__(self):
        """Build a MovieEssence object"""

        self.title = u""
        self.release_year = u""
        self.poster_image_url = u""
        self.trailer_youtube_url = u""

    def set_title(self, new_title):
        """Set the movie title

        Arguments:
            new_title: the new title of the movie

        Returns:
            The object on which this method was invoked
        """

        self.title = new_title
        return self

    def set_poster_image_url(self, poster_image_url):
        """Set the url of the poster image

        Arguments:
            poster_image_url: new url for poster image

        Returns:
            The object on which this method was invoked
        """

        self.poster_image_url = poster_image_url
        return self

    def set_trailer_youtube_url(self, youtube_url):
        """Set the url of the trailer on youtube

        Arguments:
            youtube_url: url of youtube video

        Returns:
            The object on which this method was invoked
        """

        self.trailer_youtube_url = youtube_url
        return self

    def set_release_year(self, year):
        """Set the release year of the movie

        Arguments:
            year: the year the movie was first released

        Returns:
            The object on which this method was invoked
        """

        self.release_year = year
        return self

    def is_valid(self):
        """Checks if the MovieEssence instance is valid

        Returns:
            True if valid, False otherwise
        """

        result = True
        if not self.is_valid_string(self.title):
            result = False
        if not self.is_valid_string(self.poster_image_url):
            result = False
        if not self.is_valid_string(self.trailer_youtube_url):
            result = False
        if not self.is_valid_string(self.release_year):
            result = False

        return result

    def is_valid_string(self, string):
        """Checks if the string is the right type and non-empty

        Arguments
            string: the string to validate

        Returns:
            True if valid, False otherwise
        """

        return (type(string) is unicode) and (len(string) > 0)

    def get_movie(self):
        """Creates a Movie instance based on the MovieEssence

        Returns:
            A new Movie instance if is_valid, None otherwise
        """

        if self.is_valid():
            return Movie(self)

class Movie():
    """Movie class

    Attributes:
        title: the title of the movie
        release_year: the year the movie was first released
        poster_image_url: the url of the poster image
        trailer_youtube_url: the url of the trailer on youtube
    """

    
    def __init__(self, movie_essence):
        """Build a Movie object

        Arguments:
            movie_essence: A MovieEssence object
        """

        self.title = movie_essence.title
        self.poster_image_url = movie_essence.poster_image_url
        self.trailer_youtube_url = movie_essence.trailer_youtube_url
        self.release_year = movie_essence.release_year

