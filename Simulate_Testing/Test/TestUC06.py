import unittest
from module import simulate_read_article, simulate_search

class TestUC06ReadNews(unittest.TestCase):
    def test_read_article(self):
        test_cases = [
            ("TC82", "article123", True, False, False, True, None),  # personalized
            ("TC83", "deleted123", True, True, False, False, "Article not found"),
            ("TC88", "guest123", False, False, False, True, "Guest view or login required"),
            ("TC89", None, True, False, False, False, "Invalid article ID"),
            ("TC90", "limit123", True, False, True, False, "Reading limit exceeded"),
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_read_article(
                    article_id=case[1],
                    logged_in=case[2],
                    is_deleted=case[3],
                    read_limit_exceeded=case[4]
                )
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[5])
                if not case[5]:
                    self.assertEqual(result["error"], case[6])

    def test_search_article(self):
        test_cases = [
            ("TC84", "AI", True, None),
            ("TC85", "", False, "Please enter a keyword"),
            ("TC86", "@#$%^&*", False, "No results found"),
            ("TC87", "a"*1000, False, "Keyword length limit exceeded"),
            ("TC91", "a"*255, True, None),
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_search(case[1])
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[2])
                if not case[2]:
                    self.assertEqual(result["error"], case[3])
                else:
                    self.assertIn("results", result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
