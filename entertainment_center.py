import media
import lib.fresh_tomatoes as ft


# Styles and scripting for the page
main_page_head = ft.read_template_file("templates/header_partial.html")

# The main page layout and title bar
main_page_content = ft.read_template_file("templates/content_partial.html")

# A single movie entry html template
movie_tile_content = ft.read_template_file("templates/movie_partial.html")


# Store movie data
# todo: update to use xml
movies = [
    media.Movie("Melancholia",
                "http://ia.media-imdb.com/images/M/MV5BMTk4NjM0MjI3MV5BMl5BanBnXkFtZTcwNjcxMDYzNg@@._V1_SX214_AL_.jpg",
                "https://www.youtube.com/watch?v=wzD0U841LRM"),

    media.Movie("The Matrix",
                "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
                "https://www.youtube.com/watch?v=m8e-FF8MsqU"),

    media.Movie("No Country for Old Men",
                "http://ia.media-imdb.com/images/M/MV5BMjA5Njk3MjM4OV5BMl5BanBnXkFtZTcwMTc5MTE1MQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                "https://www.youtube.com/watch?v=YOohAwZOSGo"),

    media.Movie("The Fountain",
                "http://ia.media-imdb.com/images/M/MV5BMTU5OTczMTcxMV5BMl5BanBnXkFtZTcwNDg3MTEzMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                "https://www.youtube.com/watch?v=dAuxryJ6pv8")
    ]

# Write movies out to a html document
# and display it in the browser.
ft.open_movies_page(movies,
                    main_page_head,
                    main_page_content,
                    movie_tile_content)
