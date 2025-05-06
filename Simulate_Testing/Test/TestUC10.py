import unittest
from module import simulate_statistics_view, simulate_article_comparison

class TestUC10ViewStatistics(unittest.TestCase):
    def test_statistics_view(self):
        test_cases = [
            ("TC117", "all", "success", True, True, None),  # View full stats
            ("TC118", "week", "success", True, True, "week"),  # Filter by week
            ("TC120", "all", "load_error", True, False, "Data loading error"),
            ("TC121", "month", "success", False, False, "No data available"),
            ("TC123", "day", "success", True, True, "day")  # Rapid filter (same as normal)
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_statistics_view(filter_type=case[1], simulate=case[2], dataset_exists=case[3])
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[4])
                if result["success"]:
                    self.assertIn("statistics", result)
                    if case[5]:
                        self.assertEqual(result["statistics"]["filter"], case[5])
                else:
                    self.assertEqual(result["error"], case[5])

    def test_article_comparison(self):
        test_cases = [
            ("TC119", True, True, True, None),  # Compare valid articles
            ("TC122", True, False, False, "One or more articles not found")
        ]

        for case in test_cases:
            with self.subTest(case=case[0]):
                result = simulate_article_comparison(article_a_exists=case[1], article_b_exists=case[2])
                print(f"{case[0]} =>", result)
                self.assertEqual(result["success"], case[3])
                if not case[3]:
                    self.assertEqual(result["error"], case[4])
                else:
                    self.assertIn("comparison", result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
