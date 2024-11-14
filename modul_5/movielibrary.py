import random
from datetime import datetime
from faker import Faker

# Base class for common attributes
class Media:
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
        self.views = 0

    def play(self):
        self.views += 1

    def __str__(self):
        return f"{self.title} ({self.release_year})"

    def __repr__(self):
        return f"Media(title={self.title!r}, release_year={self.release_year!r}, genre={self.genre!r}, views={self.views!r})"

class Movie(Media):
    def __str__(self):
        return f"{self.title} ({self.release_year})"

    def __repr__(self):
        return f"Movie(title={self.title!r}, release_year={self.release_year!r}, genre={self.genre!r}, views={self.views!r})"

class Series(Media):
    def __init__(self, title, release_year, genre, season, episode):
        super().__init__(title, release_year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"

    def __repr__(self):
        return (f"Series(title={self.title!r}, release_year={self.release_year!r}, genre={self.genre!r}, "
                f"season={self.season!r}, episode={self.episode!r}, views={self.views!r})")

# Library to store movies and series
library = []

def add_full_season(title, release_year, genre, season, num_episodes):
    for episode in range(1, num_episodes + 1):
        library.append(Series(title, release_year, genre, season, episode))

# Populate the library with Faker
fake = Faker()

# Adding 10 movies to the library
for _ in range(10):
    title = fake.sentence(nb_words=3).replace('.', '')
    release_year = fake.year()
    genre = fake.word()
    library.append(Movie(title, release_year, genre))

# Adding 5 series to the library
for _ in range(5):
    title = fake.sentence(nb_words=3).replace('.', '')
    release_year = fake.year()
    genre = fake.word()
    season = random.randint(1, 5)
    num_episodes = random.randint(5, 10)
    add_full_season(title, release_year, genre, season, num_episodes)

def get_movies():
    return sorted([media for media in library if isinstance(media, Movie)], key=lambda m: m.title)

def get_series():
    return sorted([media for media in library if isinstance(media, Series)], key=lambda s: s.title)

def search(title):
    return [media for media in library if media.title.lower() == title.lower()]

def generate_views():
    media = random.choice(library)
    media.views += random.randint(1, 1000)

def run_generate_views(times=1000):
    for _ in range(times):
        generate_views()

def top_titles(n=3, content_type=None):
    if content_type == "movies":
        content = get_movies()
    elif content_type == "series":
        content = get_series()
    else:
        content = library
    return sorted(content, key=lambda m: m.views, reverse=True)[:n]

def count_episodes(title):
    return len([media for media in library if isinstance(media, Series) and media.title.lower() == title.lower()])

if __name__ == "__main__":
    print("Biblioteka filmów")

    # Fill the library with content and generate views
    run_generate_views()

    # Display top titles
    today = datetime.now().strftime("%d.%m.%Y")
    print(f"\nNajpopularniejsze filmy i seriale dnia {today}")
    for media in top_titles():
        print(f"{media} - {media.views} odtworzeń")

