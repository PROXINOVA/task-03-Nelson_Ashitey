# task-03-Nelson_Ashitey
This GitHub repository contains my third project assignment during my internship period at DecodeLabs
[README_recommender.md](https://github.com/user-attachments/files/32692145/README_recommender.md)
# Simple Recommendation System

A rule-based movie recommendation system that suggests titles based on a
user's preferred genres, using basic similarity matching between the
user's interests and each movie's tags.

## Overview

This project demonstrates the core ideas behind a **content-based
recommendation system**:

1. **Take user input** – the user selects genres/interests from a
   numbered list.
2. **Match preferences using similarity logic** – each movie in a small
   built-in catalogue is tagged with genres; the system scores every movie
   by counting how many tags overlap with the user's selected interests.
3. **Display recommendations** – movies are ranked by match score
   (highest overlap first) and the top results are shown, along with
   their genres.

The program runs in a loop, so the user can try different combinations of
interests and get new recommendations each time.

## How It Works

- A small catalogue (`MOVIES`) stores 12 movies, each with a set of genre
  tags (e.g. `{"sci-fi", "action", "thriller"}`).
- The user picks one or more genres from the full list of available tags.
- For each movie, a **similarity score** is calculated as the number of
  tags it shares with the user's selected interests (set intersection).
- Movies are sorted by score, and the top 5 matches are displayed.
- If no movies match the selected genres, the user is prompted to try
  different interests.

This is a simple form of **content-based filtering**, one of the
foundational concepts in recommendation systems (as opposed to
collaborative filtering, which relies on other users' behaviour).

## Requirements

- Python 3.7+
- No external libraries required — pure Python logic only.

## How to Run

```bash
python recommender.py
```

You'll be shown a numbered list of genres. Enter the numbers of the ones
you like, separated by commas (e.g. `1,3,5`), and press Enter to see your
recommendations.

## Example Interaction

```
Available interests/genres:
  1. action
  2. animation
  3. comedy
  ...
  11. sci-fi
  ...

Enter the numbers of genres you like, separated by commas (e.g. 1,3,5): 1,3,10

Your selected interests: action, comedy, romance

==================================================
 YOUR RECOMMENDATIONS
==================================================

1. The Matrix
   Match score: 1
   Genres: action, sci-fi, thriller

2. The Notebook
   Match score: 1
   Genres: drama, romance

3. Superbad
   Match score: 1
   Genres: comedy, coming-of-age
...

Would you like more recommendations? (yes/no):
```

## Key Skills Demonstrated

- Logic building with sets and control flow
- Pattern matching between user preferences and item attributes
- Core recommendation system concepts (content-based filtering,
  similarity scoring, ranking)
- Interactive input handling and looped program flow

## Project Structure

```
.
├── recommender.py   # Main script: user input, matching logic, and display
└── README.md        # Project documentation
```

## Possible Extensions

- Expand the movie catalogue with more titles and tags.
- Weight rarer/more specific tags more heavily than common ones.
- Replace overlap counting with a proper similarity metric (e.g. cosine
  similarity or Jaccard similarity) for more nuanced scoring.
- Apply the same approach to a different domain, such as books, music,
  or products.
- Swap the fixed catalogue for a real dataset (e.g. from a CSV file or an
  API) to scale beyond a handful of hardcoded items.
