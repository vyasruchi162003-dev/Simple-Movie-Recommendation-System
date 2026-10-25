# Simple Movie Recommendation System

**Project:** Simple Movie Recommendation System 
**Type:** Beginner-friendly content-based recommendation system  
**Language:** Python 3  
**Dependencies:** Python standard library only

## 1. Overview

This command-line application recommends movies with genres similar to a movie selected by the user. It uses a small example dataset included in `recommendation_system.py` and Jaccard similarity to compare genre overlap.

This is a learning project. It does not use a trained machine-learning model, online movie database, user ratings, or internet connection.

## 2. Features

- Lists all movies available in the sample dataset.
- Accepts movie titles without case sensitivity or extra surrounding spaces.
- Calculates similarity based on shared genres.
- Displays the three highest-scoring recommendations.
- Handles unknown titles and empty input.
- Lets the user list movies again or quit safely.
- Includes automated unit tests.

## 3. Requirements

- Python 3.9 or newer recommended.
- No third-party packages are required.

## 4. Run the application

Open a terminal in this project folder and run:

```bash
python recommendation_system.py
```

Depending on your system, you may need to use `python3` instead of `python`.

Enter a movie title exactly as shown in the available list (capitalization does not matter). Type `list` to show titles again, or `q` to exit.

## 5. Example

```text
================================================
       SIMPLE MOVIE RECOMMENDATION SYSTEM
              CodeOrbitTech — Task 4
================================================

Available movies:
 1. Interstellar
 2. The Martian
 3. Gravity
 4. Arrival
 5. Inception
 6. The Dark Knight
 7. Titanic
 8. The Notebook
 9. Superbad
10. The Hangover

Enter a movie title (or type 'list' to show movies, 'q' to quit): Interstellar

Recommendations for: Interstellar
------------------------------------------------
1. The Martian            Similarity: 100.0%
2. Gravity                Similarity: 50.0%
3. Arrival                Similarity: 50.0%

Note: Scores compare genre overlap, not audience ratings or overall quality.
```

## 6. How it works

Each movie is represented by a list of genres. The Jaccard similarity score is:

`similarity = number of shared genres / number of unique genres across both movies`

The score ranges from 0 to 1. A score of 1 (100%) means both movies have identical genre sets. A score of 0 means they share no genres. The program excludes the selected movie, sorts other titles by score from highest to lowest, and returns the top three.

## 7. Run automated tests

From the project folder:

```bash
python -m unittest discover -s tests -v
```

Tests cover similarity calculations, exact matches, case-insensitive input, unknown titles, result limits, and score ranges.

## 8. Project files

```text
CodeOrbit_RecommendationSystem/
├── recommendation_system.py
├── README.md
├── requirements.txt
├── .gitignore
└── tests/
    └── test_recommendation_system.py
```

## 9. Possible future improvements

- Load a larger movie dataset from a CSV file.
- Add movie descriptions, ratings, and user preferences.
- Create a web interface with Streamlit.
- Evaluate recommendations with real user feedback.

## 10. Internship submission checklist

- [ ] Run the application and test multiple movie choices.
- [ ] Run the automated tests.
- [ ] Capture a screenshot of a successful run.
- [ ] Upload the project folder to GitHub or Google Drive as instructed by the internship coordinator.
- [ ] Share the repository or folder link in the required submission form.
- [ ] Be prepared to explain the dataset, Jaccard similarity, and limitations.

**Academic integrity note:** Review the code and make sure you understand how it works before submitting it as your work. Follow the internship's own rules about assistance and AI-generated code.
