import webbrowser
import os
import re


def read_template_file(path):
    """Read the specified file

    Arguments:
        path: File path

    Returns:
        The contents of the file
    """

    result = ""
    with open(path, "r") as f:
        result = f.read()
    return result


def create_movie_tiles_content(movies, movie_tpl):
    """Creates an HTML div with the movies' details

    Arguments:
        movies: A list of Movie objects
        movie_tpl: An html template for Movies

    Returns:
        A HTML snippet with movie details inserted
    """

    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tpl.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            release_year=movie.release_year
        )
    return content


def open_movies_page(movies, head_tpl, content_tpl, movie_tpl):
    """Create the movies HTML document, and open it in the browser

    Arguments:
        movies: A list of Movie objects
        head_tpl: A template for the head of the document
        content_tpl: A template for the main content of the document
        movie_tpl: An html template for Movies

    Returns:
        None
    """

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = content_tpl.format(
        movie_tiles=create_movie_tiles_content(movies, movie_tpl))

    # Output the file
    output_file.write(head_tpl + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
