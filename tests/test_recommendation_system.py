import unittest

from recommendation_system import MOVIES, jaccard_similarity, recommend_movies


class SimilarityTests(unittest.TestCase):
    def test_identical_genres_are_100_percent(self):
        self.assertEqual(jaccard_similarity(["Sci-Fi", "Drama"], ["Drama", "Sci-Fi"]), 1.0)

    def test_no_shared_genres_are_zero(self):
        self.assertEqual(jaccard_similarity(["Comedy"], ["Romance"]), 0.0)

    def test_partial_overlap(self):
        self.assertAlmostEqual(jaccard_similarity(["A", "B"], ["B", "C"]), 1 / 3)

    def test_empty_genres(self):
        self.assertEqual(jaccard_similarity([], []), 0.0)


class RecommendationTests(unittest.TestCase):
    def test_best_match_is_the_martian_for_interstellar(self):
        results = recommend_movies("Interstellar")
        self.assertTrue(results)
        self.assertEqual(results[0][0], "The Martian")
        self.assertEqual(results[0][1], 1.0)

    def test_case_and_whitespace_are_ignored(self):
        self.assertEqual(recommend_movies("  interstellar  ")[0][0], "The Martian")

    def test_selected_movie_is_not_recommended(self):
        titles = [title for title, _ in recommend_movies("Titanic")]
        self.assertNotIn("Titanic", titles)

    def test_unknown_movie_returns_empty_list(self):
        self.assertEqual(recommend_movies("Unknown Film"), [])

    def test_limit_is_respected(self):
        self.assertEqual(len(recommend_movies("Interstellar", limit=2)), 2)

    def test_non_positive_limit_returns_empty_list(self):
        self.assertEqual(recommend_movies("Interstellar", limit=0), [])

    def test_all_results_are_from_dataset(self):
        for title, score in recommend_movies("Gravity", limit=20):
            self.assertIn(title, MOVIES)
            self.assertGreaterEqual(score, 0.0)
            self.assertLessEqual(score, 1.0)


if __name__ == "__main__":
    unittest.main()
