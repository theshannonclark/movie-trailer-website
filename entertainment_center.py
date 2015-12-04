import media
import lib.fresh_tomatoes as ft
import lib.movie_io as movie_io


# Styles and scripting for the page
main_page_head = ft.read_template_file("templates/header_partial.html")

# The main page layout and title bar
main_page_content = ft.read_template_file("templates/content_partial.html")

# A single movie entry html template
movie_tile_content = ft.read_template_file("templates/movie_partial.html")

movies = []

movie_list = movie_io.get_movies("data/movie_data.xml")
for movie in movie_list:
    title_node = movie.getElementsByTagName("title")[0]
    title = title_node.childNodes[0].nodeValue

    poster_image_node = movie.getElementsByTagName("poster-image-url")[0]
    poster_image = poster_image_node.childNodes[0].nodeValue

    youtube_trailer_node = movie.getElementsByTagName("youtube-trailer-url")[0]
    youtube_trailer = youtube_trailer_node.childNodes[0].nodeValue

    movies.append(
        media.MovieEssence()
        .set_title(title)
        .set_poster_image_url(poster_image)
        .set_trailer_youtube_url(youtube_trailer)
        .get_movie()
    )


# Write movies out to a html document
# and display it in the browser.
ft.open_movies_page(movies,
                    main_page_head,
                    main_page_content,
                    movie_tile_content)
