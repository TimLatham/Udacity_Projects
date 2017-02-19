import fresh_tomatoes
import media

inception = media.Movie("Inception",
                        "The dream is real",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

matrix = media.Movie("The Matrix",
                     "What is real?",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

stranger_than_fiction = media.Movie("Stranger than Fiction",
                                    "Am I real?",
                                    "https://upload.wikimedia.org/wikipedia/en/f/ff/Stranger_Than_Fiction_%282006_movie_poster%29.jpg",
                                    "https://www.youtube.com/watch?v=26FBhM_pjoc")

fight_club = media.Movie("Fight Club",
                       "Are my friends real?",
                       "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                       "https://www.youtube.com/watch?v=SUXWAEX2jlg")

clue = media.Movie("Clue",
                   "Who really did it?",
                   "https://upload.wikimedia.org/wikipedia/en/1/18/Clue_Poster.jpg",
                   "https://www.youtube.com/watch?v=cDDdeHtrxfA")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

my_movies = [stranger_than_fiction, fight_club, clue, matrix, inception, hunger_games]
fresh_tomatoes.open_movies_page(my_movies)
