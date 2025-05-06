import unittest
from module import simulate_reading_history, simulate_delete_history, reading_history_mock

class TestUC14ReadingHistory(unittest.TestCase):
    def setUp(self):
        self.history = ["Article 1", "Article 2", "Article 3"]

    def test_view_history(self):
        result = simulate_reading_history(self.history.copy())
        print("TC140 =>", result)
        self.assertTrue(result["success"])
        self.assertIn("history", result)
        self.assertEqual(len(result["history"]), 3)

    def test_delete_all_history(self):
        result = simulate_delete_history(self.history, confirm=True)
        print("TC141 =>", result)
        self.assertTrue(result["success"])
        self.assertEqual(result["message"], "All history deleted")
        self.assertEqual(result["remaining"], [])

    def test_view_empty_history(self):
        result = simulate_reading_history([])
        print("TC142 =>", result)
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "No reading history available")

    def test_delete_without_confirmation(self):
        result = simulate_delete_history(self.history, confirm=False)
        print("TC143 =>", result)
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "Deletion not confirmed")

    def test_delete_individual_entry(self):
        history = self.history.copy()
        result = simulate_delete_history(history, confirm=True, delete_one=True, index_to_delete=1)
        print("TC144 =>", result)
        self.assertTrue(result["success"])
        self.assertEqual(result["message"], "Deleted: Article 2")
        self.assertEqual(result["remaining"], ["Article 1", "Article 3"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
