import json
from istorage import IStorage


class StorageJson(IStorage):
    """
    A class to handle movie storage in a JSON file.

    Inherits from IStorage and provides methods for loading, saving,
    and modifying movie data stored in a JSON file.
    """

    def __init__(self, file_path):
        """
        Initializes the StorageJson with the provided file path.

        Args:
            file_path (str): The path to the JSON file that will store movie data.
        """
        self.file_path = file_path

    def _load_data(self):
        """
        Loads movie data from the JSON file.

        Returns:
            dict: A dictionary of movies with title as key and movie details as value.
                  Returns an empty dictionary if the file is not found or empty.
        """
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # If the file does not exist, return an empty dictionary.

    def _save_data(self, data):
        """
        Saves movie data to the JSON file.

        Args:
            data (dict): The movie data to be saved in the JSON file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def list_movies(self):
        """
        Returns all movies stored in the JSON file.

        Returns:
            dict: A dictionary of movies with title as key and movie details as value.
        """
        return self._load_data()

    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the JSON file.

        Args:
            title (str): The title of the movie.
            year (int): The release year of the movie.
            rating (float): The IMDb rating of the movie.
            poster (str): The URL or path of the movie poster.
        """
        movies = self._load_data()
        movies[title] = {
            "year": year,
            "rating": rating,
            "poster": poster
        }
        self._save_data(movies)

    def delete_movie(self, title):
        """
        Deletes a movie from the JSON file by its title.

        Args:
            title (str): The title of the movie to be deleted.
        """
        movies = self._load_data()
        if title in movies:
            del movies[title]
            self._save_data(movies)

    def update_movie(self, title, rating):
        """
        Updates the rating of an existing movie in the JSON file.

        Args:
            title (str): The title of the movie to update.
            rating (float): The new rating for the movie.
        """
        movies = self._load_data()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_data(movies)