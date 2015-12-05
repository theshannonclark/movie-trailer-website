import fresh_tomatoes as ft

class MovieEssence():

    def __init__(self):
        self.title = u""
        self.release_year = u""
        self.poster_image_url = u""
        self.trailer_youtube_url = u""

    def set_title(self, new_title):
        self.title = new_title
        return self

    def set_poster_image_url(self, poster_image_url):
        self.poster_image_url = poster_image_url
        return self

    def set_trailer_youtube_url(self, youtube_url):
        self.trailer_youtube_url = youtube_url
        return self

    def set_release_year(self, year):
        self.release_year = year
        return self

    def is_valid(self):
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
        return (type(string) is unicode) and (len(string) > 0)

    def get_movie(self):
        if self.is_valid():
            return Movie(self)

class Movie():
    
    def __init__(self, movie_essence):
        self.title = movie_essence.title
        self.poster_image_url = movie_essence.poster_image_url
        self.trailer_youtube_url = movie_essence.trailer_youtube_url
        self.release_year = movie_essence.release_year

