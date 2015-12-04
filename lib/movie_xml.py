from xml.dom import minidom

def read_movie_file(path):
    return minidom.parse(path)

def get_movies(path, movieTag = "movie"):
    movie_data = read_movie_file(path)
    return movie_data.getElementsByTagName(movieTag)
