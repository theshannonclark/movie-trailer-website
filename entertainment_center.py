import media
import lib.fresh_tomatoes as ft


# Styles and scripting for the page
main_page_head = ft.read_template_file("templates/header_partial.html")

# The main page layout and title bar
main_page_content = ft.read_template_file("templates/content_partial.html")

# A single movie entry html template
movie_tile_content = ft.read_template_file("templates/movie_partial.html")

melancholia = (
    media.MovieEssence()
    .set_title("Melancholia")
    .set_poster_image_url("http://ia.media-imdb.com/images/M/MV5BMTk4NjM0MjI3MV5BMl5BanBnXkFtZTcwNjcxMDYzNg@@._V1_SX214_AL_.jpg")
    .set_trailer_youtube_url("https://www.youtube.com/watch?v=wzD0U841LRM")
    .get_movie()
)
the_matrix = (
    media.MovieEssence()
    .set_title("The Matrix")
    .set_poster_image_url("http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg")
    .set_trailer_youtube_url("https://www.youtube.com/watch?v=m8e-FF8MsqU")
    .get_movie()
)
no_country = (
    media.MovieEssence()
    .set_title("No Country for Old Men")
    .set_poster_image_url("http://ia.media-imdb.com/images/M/MV5BMjA5Njk3MjM4OV5BMl5BanBnXkFtZTcwMTc5MTE1MQ@@._V1_SY317_CR0,0,214,317_AL_.jpg")
    .set_trailer_youtube_url("https://www.youtube.com/watch?v=YOohAwZOSGo")
    .get_movie()
)

movies = [melancholia, the_matrix, no_country]

# Write movies out to a html document
# and display it in the browser.
ft.open_movies_page(movies,
                    main_page_head,
                    main_page_content,
                    movie_tile_content)
