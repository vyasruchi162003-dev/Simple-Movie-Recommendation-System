"""
Simple Movie Recommendation System
CodeOrbitTech AI Internship — Task 4

A beginner-friendly content-based recommender using movie genres and
Jaccard similarity. Uses only Python's standard library.
"""

from typing import Dict, Iterable, List, Tuple

MOVIES: Dict[str, List[str]] = {
    "Interstellar": ["Sci-Fi", "Adventure", "Drama"],
    "The Martian": ["Sci-Fi", "Adventure", "Drama"],
    "Gravity": ["Sci-Fi", "Adventure", "Thriller"],
    "Arrival": ["Sci-Fi", "Drama", "Mystery"],
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Titanic": ["Romance", "Drama"],
    "The Notebook": ["Romance", "Drama"],
    "Superbad": ["Comedy"],
    "The Hangover": ["Comedy", "Adventure"],
}


def jaccard_similarity(genres_a: Iterable[str], genres_b: Iterable[str]) -> float:
    """Return the Jaccard similarity of two genre collections, from 0.0 to 1.0."""
    set_a, set_b = set(genres_a), set(genres_b)
    union = set_a | set_b
    if not union:
        return 0.0
    return len(set_a & set_b) / len(union)


def recommend_movies(
    selected_movie: str,
    movies: Dict[str, List[str]] = MOVIES,
    limit: int = 3,
) -> List[Tuple[str, float]]:
    """
    Return (movie title, similarity score) pairs, sorted by score descending.
    The selected movie is excluded. Matching is case-insensitive and ignores
    surrounding whitespace. Unknown titles return an empty list.
    """
    if limit <= 0:
        return []

    normalized_titles = {title.casefold(): title for title in movies}
    canonical_title = normalized_titles.get(selected_movie.strip().casefold())
    if canonical_title is None:
        return []

    selected_genres = movies[canonical_title]
    results = []
    for title, genres in movies.items():
        if title == canonical_title:
            continue
        score = jaccard_similarity(selected_genres, genres)
        results.append((title, score))

    # Stable sorting keeps the dataset order when scores are tied.
    results.sort(key=lambda item: item[1], reverse=True)
    return results[:limit]


def display_recommendations(selected_movie: str, movies: Dict[str, List[str]] = MOVIES) -> None:
    """Print recommendations for one selected movie."""
    matches = {title.casefold(): title for title in movies}
    canonical_title = matches.get(selected_movie.strip().casefold())

    if canonical_title is None:
        print(f"\nSorry, '{selected_movie.strip()}' is not in our dataset.")
        print("Please choose a title from the available movie list.")
        return

    recommendations = recommend_movies(canonical_title, movies=movies)
    print(f"\nRecommendations for: {canonical_title}")
    print("-" * 48)
    if not recommendations:
        print("No recommendations are available.")
        return

    for index, (title, score) in enumerate(recommendations, start=1):
        print(f"{index}. {title:<22} Similarity: {score * 100:5.1f}%")

    print("\nNote: Scores compare genre overlap, not audience ratings or overall quality.")


def main() -> None:
    """Run the interactive command-line application."""
    print("=" * 48)
    print("       SIMPLE MOVIE RECOMMENDATION SYSTEM")
    print("              CodeOrbitTech — Task 4")
    print("=" * 48)
    print("\nAvailable movies:")
    for index, title in enumerate(MOVIES, start=1):
        print(f"{index:2}. {title}")

    while True:
        try:
            choice = input(
                "\nEnter a movie title (or type 'list' to show movies, 'q' to quit): "
            ).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting. Thank you!")
            break

        if choice.casefold() in {"q", "quit", "exit"}:
            print("Thank you for using the Movie Recommendation System!")
            break
        if choice.casefold() == "list":
            print("\nAvailable movies:")
            for title in MOVIES:
                print(f"- {title}")
            continue
        if not choice:
            print("Please enter a movie title.")
            continue

        display_recommendations(choice)


if __name__ == "__main__":
    main()
