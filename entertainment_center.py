import lib.media as media
import lib.fresh_tomatoes as ft
import lib.movie_xml as movie_xml


# Styles and scripting for the page
main_page_head = ft.read_template_file("templates/header_partial.html")

# The main page layout and title bar
main_page_content = ft.read_template_file("templates/content_partial.html")

# A single movie entry html template
movie_tile_content = ft.read_template_file("templates/movie_partial.html")

movies = []

# parse the movie xml document, and add each movie to a list
movie_list = movie_xml.get_movies("data/movie_data.xml")
for movie in movie_list:
    # get each movie's details as a dictionary
    movie_data = movie_xml.get_movie_data(movie)

    # create a movie instance and append it to the list
    movies.append(
        media.MovieEssence()
        .set_title(movie_data["title"])
        .set_poster_image_url(movie_data["poster_image"])
        .set_trailer_youtube_url(movie_data["youtube_trailer"])
        .set_release_year(movie_data["release_year"])
        .get_movie()
    )


# Write movies out to a html document and display it
# in the browser.
ft.open_movies_page(movies,
                    main_page_head,
                    main_page_content,
                    movie_tile_content)
