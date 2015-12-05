from xml.dom import minidom

def read_movie_file(path):
    """Parse the specified XML file

    Returns:
        A Document representing the xml file
    """

    return minidom.parse(path)

def get_movies(path, movieTag = "movie"):
    """Reads the XML file, and returns movieTags elements

    Arguments:
        movieTag: The tag of the elements to retrieve

    Returns:
        A list of xml elements of the specified type
    """

    movie_data = read_movie_file(path)
    return movie_data.getElementsByTagName(movieTag)

def get_movie_text_node(movie, tagName):
    """Gets the text value of the specified tag

    Arguments:
        tagName: The tag of the element to get text from

    Returns:
        The text value of the node with the specified tag
    """

    node = movie.getElementsByTagName(tagName)[0]
    return node.childNodes[0].nodeValue

def get_movie_data(movie):
    """Extracts data from the movie xml dom object

    Arguments:
        movie: A Movie object

    Returns:
        A dictionary with the details of the movie.
    """

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
