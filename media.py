
import webbrowser


class Movie():
    """[Docstring about the Movie class]"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_rating, movie_release_date, movie_director, movie_review_score):
        """[Special function that creates space in memory to remember things in class]"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
        self.release_date = movie_release_date
        self.director = movie_director
        self.review_score = movie_review_score

    def show_trailer(self):
        """[Instance method opens webbroswer with correct url that is stored in instance variable]"""
        webbrowser.open(self.trailer_youtube_url)
