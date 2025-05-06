import unittest
from module import simulate_filter_articles

class TestUC12FilterArticles(unittest.TestCase):
    def test_filter_articles(self):
        test_cases = [
            ("TC130", "Technology", True, None),
            ("TC131", "", False, "No matching articles found"),
            ("TC132", "All", True, None),
            ("TC133", "@@invalid", False, "Invalid category"),
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_filter_articles(case[1])
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[2])
                if result["success"]:
                    self.assertIn("articles", result)
                    self.assertGreater(len(result["articles"]), 0)
                else:
                    self.assertEqual(result["error"], case[3])

if __name__ == "__main__":
    unittest.main(verbosity=2)
