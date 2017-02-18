import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print(avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")




inception = media.Movie("Inception",
                        "The dream is real",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")
#inception.show_trailer()
#inception.show_poster()

matrix = media.Movie("The Matrix",
                     "What is real?",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

stranger_than_fiction = media.Movie("Stranger than Fiction",
                                    "Am I real or not?",
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


movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
my_movies = [inception, matrix, stranger_than_fiction, fight_club, clue, hunger_games]
fresh_tomatoes.open_movies_page(my_movies)
