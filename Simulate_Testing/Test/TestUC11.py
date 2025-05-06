import unittest
from module import simulate_search_articles

class TestUC11SearchArticles(unittest.TestCase):
    def test_search_articles(self):
        test_cases = [
            ("TC124", "AI", True, None),  # Normal search
            ("TC125", "xyz", False, "No results found"),
            ("TC126", "", False, "Please enter a keyword"),
            ("TC127", "@#$%", False, "No results found"),
            ("TC128", "a" * 300, False, "Keyword too long"),
            ("TC129", "ai", True, None),  # Case-insensitive match
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_search_articles(case[1])
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[2])
                if result["success"]:
                    self.assertIn("results", result)
                    self.assertGreater(len(result["results"]), 0)
                else:
                    self.assertEqual(result["error"], case[3])

if __name__ == "__main__":
    unittest.main(verbosity=2)
