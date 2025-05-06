import unittest
from module import simulate_article_rating

class TestUC13ArticleRating(unittest.TestCase):
    def test_article_rating_feedback(self):
        test_cases = [
            ("TC134", 5, "Great article!", "success", False, False, True, "Rating saved successfully"),
            ("TC135", 4, "Updated review", "success", True, False, True, "Rating updated successfully"),
            ("TC136", None, "Comment without rating", "success", False, False, False, "Please select a rating"),
            ("TC137", 4, "a" * 1001, "success", False, False, False, "Comment too long"),
            ("TC138", 5, "Amazing post! 😊 <script>", "sanitize", False, False, True, "Rating saved with sanitized comment"),
            ("TC139", 5, "Trying to spam", "success", False, True, False, "Duplicate submission detected"),
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_article_rating(
                    rating=case[1],
                    comment=case[2],
                    simulate=case[3],
                    is_update=case[4],
                    rapid_submit=case[5]
                )
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[6])
                if result["success"]:
                    self.assertIn(case[7], result["message"])
                else:
                    self.assertEqual(result["error"], case[7])

if __name__ == "__main__":
    unittest.main(verbosity=2)
