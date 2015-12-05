from xml.dom import minidom

def read_movie_file(path):
    return minidom.parse(path)

def get_movies(path, movieTag = "movie"):
    movie_data = read_movie_file(path)
    return movie_data.getElementsByTagName(movieTag)

def get_movie_text_node(movie, tagName):
    node = movie.getElementsByTagName(tagName)[0]
    return node.childNodes[0].nodeValue

def get_movie_data(movie):
    title = get_movie_text_node(movie, "title")
    poster_image = get_movie_text_node(movie, "poster-image-url")
    youtube_trailer = get_movie_text_node(movie, "youtube-trailer-url")
    release_year = get_movie_text_node(movie, "release-year")

    return {
        "title": title,
        "poster_image": poster_image,
        "youtube_trailer": youtube_trailer,
        "release_year": release_year
    }
