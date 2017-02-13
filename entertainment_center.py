import fresh_tomatoes
import media


# __init__ function gets called from Movie class in media.py
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "Rated: " + str(media.Movie.VALID_RATINGS[0]),
                        "Release date: November 22, 1995(USA)",
                        "Director: John Lasseter",
                        "Review Score: 100% on Rotten Tomatoes")



avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8",
                     "Rated: " + str(media.Movie.VALID_RATINGS[2]),
                     "Release date: December 18, 2009 (USA)",
                     "Director: James Cameron",
                     "Review Score: 83% on Rotten Tomatoes")



the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                   "A banker who is sentenced to life in Shawshank State Penitentiary for the murder of his wife and her lover, despite his claims of innocence",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco",
                                    "Rated: " + str(media.Movie.VALID_RATINGS[3]),
                                    "Release date: September 23, 1994 (USA)",
                                    "Director: Frank Darabont",
                                    "Review Score: 91% on Torrten Tomatoes")



doctor_strange = media.Movie("Doctor Strange",
                             "Surgeon Stephen Strange learns the mystic arts from the Ancient One after a career-ending car accident",
                             "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
                             "https://www.youtube.com/watch?v=HSzx-zryEgM",
                             "Rated: " + str(media.Movie.VALID_RATINGS[2]),
                             "Release date: October 20, 2016 (Los Angeles)",
                             "Director: Scott Derrickson",
                             "Review Score: 90% on Rotten Tomatoes")
                             


fantastic_beasts_and_where_to_find_them = media.Movie("Fantastic Beasts and Where to Find Them",
                                                      "In 1926, British wizard Newt Scamander arrives by boat to New York City en route to Arizona",
                                                      "http://i.dailymail.co.uk/i/pix/2016/06/21/14/3583D0B000000578-3652288-image-a-8_1466514272583.jpg",
                                                      "https://www.youtube.com/watch?v=FEKYSXArjEo",
                                                      "Rated: " + str(media.Movie.VALID_RATINGS[2]),
                                                      "Release date: November 18, 2016 (USA)",
                                                      "Director: David Yates",
                                                      "Review Score: 74% on Rotten Tomatoes")                                                     



guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy",
                                      "Peter Quill forms an uneasy alliance with a group of extraterrestrial misfits who are fleeing after stealing a powerful artifact",
                                      "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
                                      "https://www.youtube.com/watch?v=d96cjJhvlMA",
                                      "Rated: " + str(media.Movie.VALID_RATINGS[2]),
                                      "Release date: August 1, 2014 (USA)",
                                      "Director: James Gunn",
                                      "Review Score:  91% on Rotten Tomatoes")



deadpool = media.Movie("Deadpool",
                       "Antihero Deadpool hunts the man who nearly destroyed his life while also trying to reunite with his lost love",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk",
                       "Rated: " + str(media.Movie.VALID_RATINGS[3]),
                       "Release date: February 12, 2016 (USA)",
                       "Director: Tim Miller",
                       "Review Score:  84% on Rotten Tomatoes")                   



warcraft = media.Movie("Warcraft",
                       "The initial encounters between the humans and the orcs and takes place in a variety of locations established in the video game series",
                       "https://upload.wikimedia.org/wikipedia/en/5/56/Warcraft_Teaser_Poster.jpg",
                       "https://www.youtube.com/watch?v=2Rxoz13Bthc",
                       "Rated: " + str(media.Movie.VALID_RATINGS[2]),
                       "Release date: June 10, 2016 (USA)",
                       "Director: Duncan Jones",
                       "Review Score: 28% on Rotten Tomatoes")


                       
the_hateful_eight = media.Movie("The Hateful Eight",
                                "Eight strangers who seek refuge from a blizzard in a stagecoach stopover some time after the American Civil War",
                                "https://upload.wikimedia.org/wikipedia/en/d/d4/The_Hateful_Eight.jpg",
                                "https://www.youtube.com/watch?v=gnRbXn4-Yis",
                                "Rated: " + str(media.Movie.VALID_RATINGS[3]),
                                "Release date: December 25, 2015 (USA)",
                                "Director: Quentin Tarantino",
                                "Review Score:  75% on Rotten Tomatoes")



finding_dory = media.Movie("Finding Dory",
                           "The amnesiac fish Dory, who journeys to be reunited with her parents",
                           "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
                           "https://www.youtube.com/watch?v=0tkLUap7oGQ",
                           "Rated: " + str(media.Movie.VALID_RATINGS[1]),
                           "Release date: June 17, 2016 (USA)",
                           "Director: Andrew Stanton",
                           "Review Score:  94% on Rotten Tomatoes")



fury = media.Movie("Fury",
                   "US tank crews in Nazi Germany during the final days of World War II",
                   "https://upload.wikimedia.org/wikipedia/en/1/17/Fury_2014_poster.jpg",
                   "https://www.youtube.com/watch?v=-OGvZoIrXpg",
                   "Rated: " + str(media.Movie.VALID_RATINGS[3]),
                   "Release date: October 15, 2014 (USA)",
                   "Director: David Ayer",
                   "Review Score:  77% on Rotten Tomatoes")



interstellar = media.Movie("Interstellar",
                           "A crew of astronauts travel through a wormhole in search of a new home for humanity",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA",
                           "Rated: " + str(media.Movie.VALID_RATINGS[2]),
                           "Release date: October 26, 2014 (USA)",
                           "Director: Christopher Nolan",
                           "Review Score:  71% on Rotten Tomatoes")
                           
                           
                               


movies = [toy_story, avatar, the_shawshank_redemption, doctor_strange, fantastic_beasts_and_where_to_find_them, guardians_of_the_galaxy, deadpool, warcraft, the_hateful_eight, finding_dory, fury, interstellar]
# Uses list of movie instances as input to generate an HTML file
# and opens it in the webbrowser
fresh_tomatoes.open_movies_page(movies)

