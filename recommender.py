"""
Project 3: Simple Recommendation System
-----------------------------------------
Recommends movies based on the user's preferred genres, using basic
similarity matching (counting overlapping tags between the user's
interests and each item's tags). Demonstrates:
  - Taking user input (interests/choices)
  - Matching preferences using logic/similarity
  - Displaying ranked recommendations
"""

# A small catalog of movies, each tagged with genres/interests.
MOVIES = [
    {"title": "The Matrix",         "tags": {"sci-fi", "action", "thriller"}},
    {"title": "Inception",          "tags": {"sci-fi", "thriller", "mystery"}},
    {"title": "The Notebook",       "tags": {"romance", "drama"}},
    {"title": "Superbad",           "tags": {"comedy", "coming-of-age"}},
    {"title": "John Wick",          "tags": {"action", "thriller"}},
    {"title": "La La Land",         "tags": {"romance", "musical", "drama"}},
    {"title": "The Hangover",       "tags": {"comedy"}},
    {"title": "Interstellar",       "tags": {"sci-fi", "drama", "space"}},
    {"title": "Get Out",            "tags": {"horror", "thriller", "mystery"}},
    {"title": "Toy Story",          "tags": {"animation", "family", "comedy"}},
    {"title": "The Conjuring",      "tags": {"horror", "thriller"}},
    {"title": "Pride and Prejudice", "tags": {"romance", "drama"}},
]

ALL_TAGS = sorted({tag for movie in MOVIES for tag in movie["tags"]})


def get_user_interests():
    """Take user input: let them pick from a list of available interests."""
    print("Available interests/genres:")
    for i, tag in enumerate(ALL_TAGS, start=1):
        print(f"  {i}. {tag}")

    raw = input(
        "\nEnter the numbers of genres you like, separated by commas "
        "(e.g. 1,3,5): "
    )

    selected = set()
    for piece in raw.split(","):
        piece = piece.strip()
        if piece.isdigit():
            index = int(piece) - 1
            if 0 <= index < len(ALL_TAGS):
                selected.add(ALL_TAGS[index])

    return selected


def score_movie(user_tags, movie_tags):
    """Similarity score = number of overlapping tags between user & movie."""
    return len(user_tags & movie_tags)


def get_recommendations(user_tags, top_n=5):
    """Match preferences using overlap-based similarity and rank results."""
    scored = []
    for movie in MOVIES:
        score = score_movie(user_tags, movie["tags"])
        if score > 0:
            scored.append((movie["title"], score, movie["tags"]))

    # Sort by score (highest similarity first)
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]


def display_recommendations(recommendations):
    """Display the recommended items nicely."""
    print("\n" + "=" * 50)
    print(" YOUR RECOMMENDATIONS")
    print("=" * 50)

    if not recommendations:
        print("\nNo strong matches found. Try selecting different genres!")
        return

    for rank, (title, score, tags) in enumerate(recommendations, start=1):
        tag_list = ", ".join(sorted(tags))
        print(f"\n{rank}. {title}")
        print(f"   Match score: {score}")
        print(f"   Genres: {tag_list}")


def main():
    print("=" * 50)
    print(" Welcome to the Movie Recommendation System!")
    print("=" * 50)

    while True:
        user_tags = get_user_interests()

        if not user_tags:
            print("\nNo valid genres selected. Please try again.")
        else:
            print(f"\nYour selected interests: {', '.join(sorted(user_tags))}")
            recommendations = get_recommendations(user_tags)
            display_recommendations(recommendations)

        again = input("\nWould you like more recommendations? (yes/no): ")
        if again.strip().lower() not in ("yes", "y"):
            print("\nThanks for using the recommender. Goodbye!")
            break


if __name__ == "__main__":
    main()
