import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

avengers = media.Movie("Avengers: Infinity War",
                    "The Avengers and their Super Hero allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos.",
                    "https://www.movieinsider.com/images/p/600//488741_m1522889808.jpg",
                    "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

#print(toy_story.storyline)
#print(avatar.storyline)
#avatar.show_trailer()
avengers.show_trailer()