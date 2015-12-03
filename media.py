import lib.fresh_tomatoes as ft

class MovieEssence():

    def __init__(self):
        self.title = ""
        self.poster_image_url = ""
        self.trailer_youtube_url = ""

    def set_titles(new_title):
        self.title = new_title

    def set_poster_image_url(poster_image_url):
        self.poster_image_url = poster_image_url

    def set_trailer_youtube_url(youtube_url):
        self.trailer_youtube_url = youtube_url

class Movie():
    
    def __init__(self, movie_essence):
        self.title = movie_essence.title
        self.poster_image_url = movie_essence.poster_image_url
        self.trailer_youtube_url = movie_essence.trailer_youtube_url

